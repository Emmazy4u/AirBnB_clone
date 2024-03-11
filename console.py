#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import shlex
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    available_classes = {"BaseModel": BaseModel,
                         "User": User,
                         "State": State,
                         "City": City,
                         "Place": Place,
                         "Amenity": Amenity,
                         "Review": Review
                         }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the console upon EOF condition"""
        print('exit')
        return True

    def default(self, line):
        """default setting for cmd module if input is not valid"""
        print("invalid command: {}".format(line))
        return False

    def emptyline(self):
        """Does nothing when space or ENTER is typed"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel into
        the JSON file and prints the id"""
        if not line:
            print("** class name missing **")
        elif line in HBNBCommand.available_classes:
            new_instance = self.available_classes[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        valid_classes = HBNBCommand.available_classes
        if not line:
            print('** class name missing **')
        else:
            cmd_tokens_list = shlex.split(line)
            if cmd_tokens_list[0] not in valid_classes:
                print("** class doesn't exist **")
            elif len(cmd_tokens_list) < 2:
                print('** instance id missing **')
            else:
                class_name = cmd_tokens_list[0]
                instance_id = cmd_tokens_list[1]
                key = "{}.{}".format(class_name, instance_id)
                all_objs = FileStorage().all()
                if key not in all_objs.keys():
                    print('** no instance found **')
                else:
                    print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        valid_classes = HBNBCommand.available_classes
        if not line:
            print('** class name missing **')
        else:
            cmd_tokens_list = shlex.split(line)
            if cmd_tokens_list[0] not in valid_classes:
                print("** class doesn't exist **")
            elif len(cmd_tokens_list) < 2:
                print('** instance id missing **')
            else:
                class_name = cmd_tokens_list[0]
                instance_id = cmd_tokens_list[1]
                key = "{}.{}".format(class_name, instance_id)
                all_objs = FileStorage().all()
                if key not in all_objs.keys():
                    print('** no instance found **')
                else:
                    del all_objs[key]
                    FileStorage().save()

    def do_all(self, line):
        """Prints all string representations of all instances"""
        all_objs = FileStorage().all()
        valid_classes = HBNBCommand.available_classes
        cmd_tokens_list = shlex.split(line)
        if len(cmd_tokens_list) == 1:
            if cmd_tokens_list[0] not in valid_classes:
                print("** class doesn't exist **")
            else:
                """print a string rep. of the provided class"""
                for key, value in all_objs.items():
                    if key.split('.')[0] == cmd_tokens_list[0]:
                        print(str(value))
        elif len(cmd_tokens_list) > 1:
            print("you entered too many arguments")
        else:
            for key, value in all_objs.items():
                print(str(value))

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        all_objs = FileStorage().all()
        valid_classes = HBNBCommand.available_classes
        cmd_tokens_list = shlex.split(line)
        tok_len = len(cmd_tokens_list)
        if not cmd_tokens_list:
            print('** class name missing **')
        elif cmd_tokens_list[0] not in valid_classes:
            print("** class doesn't exist **")
        elif tok_len < 2:
            print('** instance id missing **')
        else:
            class_name = cmd_tokens_list[0]
            instance_id = cmd_tokens_list[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in all_objs.keys():
                print('** no instance found **')
            elif tok_len < 3:
                print("** attribute name missing **")
            elif tok_len < 4:
                print("** value missing **")
            else:
                new_name = cmd_tokens_list[2]
                new_value = cmd_tokens_list[3]
                if new_name in ["created_at", "updated_at", "id"]:
                    print("updating {} is not allowed".format(new_name))
                else:
                    new_instance = BaseModel()
                    setattr(new_instance, new_name, new_value)
                    new_instance.save()

"""
    def do_count(self, line):
        ...Counts the instances of a class...
        counter = 0
        for key in storage.all().keys():
            class_name, instance_id = key.split('.')
            if line == class_name:
                counter += 1
        print(counter)
"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
