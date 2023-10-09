#!/usr/bin/python3
'''
    this module contains an entry point for a command interpreter
'''

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

    def help_emptyline(self):
        '''provides info about an emptyline cmd'''
        print("Emptyline makes sure nothing is executed incase of an empty command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
