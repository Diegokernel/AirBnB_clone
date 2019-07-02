#!/usr/bin/python3
"""Console Module - contains the entry point of the command interpreter
class: HBNBCommand
"""
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand - contains the entry point of the command interprete
    attributes: prompt
    methods: do_quit, do_EOF.
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return(True)

    def do_EOF(self, line):
        """EOF command (ctrl + d) to exit the program
        """
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        args_list = args.split()

        if len(args_list) == 0:
            print("** class name missing **")
        else:
            try:
                new_object = eval(args_list[0])()
                new_object.save()
                print(new_object.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id
        """
        args_list = args.split()
        list_class = ["BaseModel"]

        if len(args_list) == 0:
            print("** class name missing **")
        elif len(args_list) == 1:
            if not args_list[0] in list_class:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
        else:
            if not args_list[0] in list_class:
                print("** class doesn't exist **")
            else:
                id_to_check = args_list[0] + "." + args_list[1]
                all_objects = models.storage.all()

                if not id_to_check in all_objects:
                    print("** no instance found **")
                else:
                    print(all_objects[id_to_check])

    def do_destroy(self, args):
        """Prints the string representation of an instance based on the class
        name and id
        """
        args_list = args.split()
        list_class = ["BaseModel"]

        if len(args_list) == 0:
            print("** class name missing **")
        elif len(args_list) == 1:
            if not args_list[0] in list_class:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
        else:
            if not args_list[0] in list_class:
                print("** class doesn't exist **")
            else:
                id_to_check = args_list[0] + "." + args_list[1]
                all_objects = models.storage.all()

                if not id_to_check in all_objects:
                    print("** no instance found **")
                else:
                    del all_objects[id_to_check]
                    models.storage.save()
                    models.storage.reload()

if __name__ == "__main__":
    mycmd = HBNBCommand()
    mycmd.cmdloop()
