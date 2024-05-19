#!/usr/bin/python3


"""HBNB Console module"""
import cmd
import os
from models.base_model import BaseModel
from models import storage
from shlex import split as split
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """A class that handles the HBNB console."""

    __class_dict = {'BaseModel': BaseModel, 'User': User,
                    'State': State, 'Amenity': Amenity,
                    'Place': Place, 'City': City,
                    'Review': Review}

    prompt = '(hbnb) '

    def do_create(self, clss):
        """Create a new instance"""
        if not clss:
            print("** class name missing **")
        elif clss not in self.__class_dict:
            print("** class doesn't exist **")
        else:
            clss = self.__class_dict[clss]
            obj = clss()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """Display the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return False

        parts = line.split(" ", 1)
        clss = parts[0]

        if clss not in self.__class_dict:
            print("** class doesn't exist **")
            return False

        try:
            clss_id = parts[1]
        except IndexError:
            print("** instance id missing **")
            return False

        obj_key = "{}.{}".format(clss, clss_id)
        objs = storage.all()

        if obj_key not in objs:
            print("** no instance found **")
            return False
        else:
            print(objs[obj_key])

    def do_destroy(self, line):
        """Delete an instance"""
        if not line:
            print("** class name missing **")
            return False

        parts = line.split(" ", 1)
        clss = parts[0]

        if clss not in self.__class_dict:
            print("** class doesn't exist **")
            return False

        try:
            clss_id = parts[1]
        except IndexError:
            print("** instance id missing **")
            return False

        obj_key = "{}.{}".format(clss, clss_id)
        objs = storage.all()

        if obj_key not in objs:
            print("** no instance found **")
            return False
        else:
            del objs[obj_key]
            storage.save()

    def do_all(self, line):
        """
        Display string representation of all instances
        based on the class name(optional)
        """
        obj_list = []
        obj_dict = storage.all()

        if not line:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            clss = line

            if clss in self.__class_dict:
                for key, value in obj_dict.items():
                    if value.__class__.__name__ == clss:
                        obj_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return
        print(obj_list)

    def do_update(self, line):
        """Add new attribute to an instance"""

        arg = split(line)

        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__class_dict:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(arg[0], arg[1])
            objs = storage.all()

            if obj_key not in objs:
                print("** no instance found **")
            else:
                setattr(objs[obj_key], arg[2], arg[3])
                storage.save()

    def do_clear(self, line):
        """Clear the terminal"""
        if not line:
            os.system("clear")
        else:
            print("Enter 'clear' without any additional argument")

    def emptyline(line):
        """Dn nothing when nothing is passed"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file command to exit the program"""
        print("")
        return True

    def default(self, line):
        """Default command to handle unknown commands"""
        if '.' in line:
            parts = line.split('.')
            if len(parts) != 2:
                print("** Unknown command **")
                return
            clss_name = parts[0]
            command = parts[1]

            if clss_name not in self.__class_dict:
                print("** class doesn't exist **")
                return False

            method = command.split('(')[0]
            start_index = command.find('(') + 1
            command_str = command[start_index:-1]
            args = split(command_str)

            if method == "all":
                self.do_all(clss_name)

            elif method == "count":
                obj_dict = storage.all()
                count = 0

                for key in obj_dict:
                    if clss_name == key.split(".")[0]:
                        count += 1
                print(count)
            elif method == "show":
                if len(args) != 1:
                    print("** instance id missing **")
                    return False
                self.do_show(clss_name + " " + args[0])
            elif method == "destroy":
                if len(args) != 1:
                    print("** instance id missing **")
                    return False
                self.do_destroy(clss_name + " " + args[0])
            elif method == "update":
                if len(command_str) == 0:
                    print("** instance id missing **")
                    return False
                self.do_update(clss_name + " " + command_str)
        else:
            print("** Unknown command **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
