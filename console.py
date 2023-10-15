#!/usr/bin/python3

'''
    this module contains an entry point for a command interpreter
'''


from inspect import isclass
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from json import loads, dumps
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    '''
    this is a class defines the CI
    It inherits from class Cmd int the cmd module
    '''
    prompt = "(hbnb) "
    def do_quit(self, line):
        '''handles the quit command'''
        return True

    def do_EOF(self, line):
        '''handles the end of file condition'''
        return True

    def do_create(self, arg):
        '''Creates a new instance of a class  class_name'''
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
            new = class_()
            new.save()
            print(new.id)
        except KeyError:
            print("** class doesn't exist **")


    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
            if len(args) == 1:
                print("** instance id missing **")
                return
            _id = args[1]
            storage.reload()
            key = str(class_name) + "." + str(_id)
            objects_ = storage.all()
            if key in objects_.keys():
                print(objects_[key])
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")


    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
            if len(args) == 1:
                print("** instance id missing **")
                return
            _id = args[1]
            storage.reload()
            key = str(class_name) + "." + str(_id)
            objects_ = storage.all()

            if key in objects_.keys():
                del objects_[key]
                storage.save()
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not on the'''
        args = arg.split()
        if not args:
            storage.reload()
            objects_ = storage.all()
            list_ = []
            for key, value in objects_.items():
                list_.append(value.__str__())
            print(list_)
        else:
            class_name = args[0]
            try:
                class_ = globals()[class_name]
                storage.reload()
                objects_ = storage.all()
                list_ = []
                for key, value in objects_.items():
                        list_.append(value.__str__())
                print(list_)
                
            except KeyError:
                print("** class doesn't exist **")


    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
            if len(args) == 1:
                print("** instance id missing **")
                return
            id_ = args[1]
            storage.reload()
            objects_ = storage.all()
            key = "{}.{}".format(class_name, id_)
            if key not in objects_.keys():
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            this_key = args[2]
            this_value = loads(args[3])
            to_update = objects_[key]
            to_update.__dict__[this_key] = this_value
            to_update.save()

        except KeyError:
            print("** class doesn't exist **")


    def emptyline(self):
        '''makes sure nothing is executed incase of an empty command'''
        pass

    #help section update for each command
    def help_quit(self):
        '''provides information about the quit command'''
        #print("\nquit\nquits the CI")
        print("Quit command to exit the program\n")
        print("Usage: quit")

    def help_EOF(self):
        '''provides information about the EOF command'''
        print("EOF quits the program at end of file\n")
        print("Usage: Ctrl-D")

    def help_create(self):
        '''provides information about the quit command'''
        print("Usage: create <class-name>")
        print("create a new object/instance of <class-name>")

    def help_update(self):
        '''provides information about the update command'''
        print("Usage: update <class-name> <object-id> <attribute> <value>")
        print("updates a <class-name> object/instance with id <object-id>")
        print("with a new attribute <attribute> of value <value>")

    def help_show(self):
        '''provides information about the show command'''
        print("Usage: show <class-name> <obj-id>")
        print("prints an instance of class <class-name>")
        print("with id <obj-id> if it exists")

    def help_all(self):
        '''provides information about the all command'''
        print("Usage: all <class-name> or all")
        print("prints all instances of class <class-name>")
        print("when no argument is passed all saved instances are printed")

    def help_destroy(self):
        '''provides information about the destroy command'''
        print("Usage: destroy <class-name> <obj-id>")
        print("deletes a <class-name> instance with <obj-id>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
