#!/usr/bin/python3

'''
    this module contains an entry point for a command interpreter
'''


from inspect import isclass
from models import storage
from models.base_model import BaseModel
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
