#!/usr/bin/python3
"""Console Module - contains the entry point of the command interpreter
class: HBNBCommand
"""
import cmd


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

if __name__ == "__main__":
    mycmd = HBNBCommand()
    mycmd.cmdloop()
