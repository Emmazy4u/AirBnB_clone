#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    available_classes = ["BaseModel", "FileStorage"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        print('exit')
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
        """Creates a new instance of BaseModel into the JSON file and prints the id"""
        if not line:
            print("** class name missing **")
        elif line in HBNBCommand.available_classes:
            new_instance = BaseModel()
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
                instance = FileStorage()
                all_objs = instance.all()
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
                instance = FileStorage()
                all_objs = instance.all()
                if key not in all_objs.keys():
                    print('** no instance found **')
                else:
                    del all_objs[key]
                    instance.save()

    def do_all(self, line):
        """Prints all string representations of all instances"""
        instance = FileStorage()
        all_objs = instance.all()
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
"""
    def do_count(self, line):
        ...Counts the instances of a class...
        counter = 0
        for key in storage.all().keys():
            class_name, instance_id = key.split('.')
            if line == class_name:
                counter += 1
        print(counter)

    def do_update(self, line):
        ...Updates an instance based on the class name and id...
        args = shlex.split(line)
        if not args:
            print('** class name missing **')
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print('** no instance found **')
            elif len(args) < 4:
                print("** attribute name missing **")
            elif len(args) < 5:
                print("** value missing **")
            else:
                instance = instances[key]
                setattr(instance, args[2], eval(args[3]))
                instance.save()
"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
