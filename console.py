#!/usr/bin/python3

'''
    this module contains an entry point for a command interpreter
'''


from inspect import isclass
from models import storage
from models.base_model import BaseModel
from json import loads, dumps
import cmd
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
        else:
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

        else:
            class_name = args[0]
            try:
                class_ = globals()[class_name]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    _id = args[1]
                    storage.reload()
                    key = str(class_name) + "." + str(_id)
                    objects_ = storage.all()
                    print("========================================")
                    print(objects_)
                    print("========================================")
                    if key in objects_.keys():
                        objects_cp = objects_[key]
                        del objects_cp["__class__"]
                        _str_ = "[{}] ({}) {}".format(class_name, _id, objects_cp)
                        print(_str_)
                    else:
                        print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")


    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        args = arg.split()
        if not args:
            print("** class name missing **")

        else:
            class_name = args[0]
            try:
                class_ = globals()[class_name]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
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
                name = value["__class__"]
                id_ = value["id"]
                '''
                since the dict in our storage is gotten
                from to_dict
                it contains an attribute __class__ 
                which we do not want in our instance string
                so we make a copy of the dictionary 
                and delete the class attribute
                '''
                objects_cp = value
                del objects_cp["__class__"]
                _str_ = "[{}] ({}) {}".format(name, id_, objects_cp)
                list_.append(_str_)
            print(list_)
        else:
            class_name = args[0]
            try:
                class_ = globals()[class_name]
                storage.reload()
                objects_ = storage.all()
                list_ = []
                for key, value in objects_.items():
                    if value["__class__"] == class_name:
                        id_ = value["id"]
                        objects_cp = value
                        del objects_cp["__class__"]
                        _str_ = "[{}] ({}) {}".format(class_name, id_, objects_cp)
                        list_.append(_str_)
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
            return(self.cmdloop())
        class_name = args[0]
        try:
            class_ = globals()[class_name]
            if len(args) == 1:
                print("** instance id missing **")
                return(self.cmdloop())
            id_ = args[1]
            storage.reload()
            objects_ = storage.all()
            key = "{}.{}".format(class_name, id_)
            if key not in objects_.keys():
                print("** no instance found **")
                return(self.cmdloop())
            if len(args) == 2:
                print("** attribute name missing **")
                return(self.cmdloop())
            if len(args) == 3:
                print("** value missing **")
                return(self.cmdloop())
            this_key = args[2]
            this_value = loads(args[3])
            (objects_[key])[this_key] = this_value
            storage.save()

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

    def help_EOF(self):
        '''provides information about the EOF command'''
        print("EOF quits the program at end of file\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
