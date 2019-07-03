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
    methods: do_quit, do_EOF, create, show
    """
    prompt = "(hbnb) "

    def emptyline(self):
        'shouldn’t execute anything\n'
        return

    def do_quit(self, args):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF command (ctrl + d) to exit the program\n'
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

                if id_to_check not in all_objects:
                    print("** no instance found **")
                else:
                    print(all_objects[id_to_check])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the change
        into the JSON file).
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

                if not id_to_check not in all_objects:
                    print("** no instance found **")
                else:
                    del all_objects[id_to_check]
                    models.storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances based or not on
        the class name.
        """
        args_list = args.split()
        list_class = ["BaseModel"]
        all_objects = models.storage.all()
        list_of_print = []

        if len(args_list) == 0:
            for key, value in all_objects.items():
                list_of_print.append(value.__str__())
            print(list_of_print)
        else:
            if not args_list[0] in list_class:
                print("** class doesn't exist **")
            else:
                for key, value in all_objects.items():
                    if value.to_dict()["__class__"] == args_list[0]:
                        list_of_print.append(value.__str__())
                print(list_of_print)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if '"' in args:
            args_list_list = args.split('"')  # args[0] | args[1]
            args_list = args_list_list[0].split()
            args_list.append(args_list_list[1].split('"')[0])
        else:
            args_list = args.split()

        list_class = ["BaseModel"]

        if len(args_list) == 0:  # $Update
            print("** class name missing **")
        elif len(args_list) == 1:  # 1.<class name>
            if not args_list[0] in list_class:  # $Update MyModel
                print("** class doesn't exist **")
            else:  # $ update BaseModel
                print("** instance id missing **")
        elif len(args_list) == 2:  # 2.<id>
            if args_list[0] not in list_class:  # $Update MyModel
                print("** class doesn't exist **")
            else:
                id_to_check = args_list[0] + "." + args_list[1]
                all_objects = models.storage.all()

                if id_to_check not in all_objects:  # $update BaseModel 121
                    print("** no instance found **")
                else:  # $ update BaseModel existing-id
                    print("** attribute name missing **")
        elif len(args_list) == 3:  # 3.<attribute name>
            if not args_list[0] in list_class:  # $Update MyModel
                print("** class doesn't exist **")
            else:
                id_to_check = args_list[0] + "." + args_list[1]
                all_objects = models.storage.all()

                if id_to_check not in all_objects:  # $update BaseModel 121212
                    print("** no instance found **")
                else:  # $ update BaseModel existing-id
                    print("** value missing **")  # $ update BaseModel id
        else:  # 4."<attribute value>"
            if not args_list[0] in list_class:  # $Update MyModel
                print("** class doesn't exist **")
            else:
                id_to_check = args_list[0] + "." + args_list[1]
                all_objects = models.storage.all()

                if id_to_check not in all_objects:  # $update BaseModel 121212
                    print("** no instance found **")
                else:  # $ update BaseModel existing-id
                    value_temp = args_list[3]

                    try:
                        if "." in value_temp:  # chrek if is posible float
                            value = float(value_temp)
                        else:
                            value = int(value_temp)  # check if is posible int
                    except:
                        value = value_temp  # assign value how string

                    setattr(all_objects[id_to_check], args_list[2], value)
                    models.storage.save()

if __name__ == "__main__":
    mycmd = HBNBCommand()
    mycmd.cmdloop()
