#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import shlex
#from models.base_model import BaseModel
#from models.engine import file_storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

    # def do_create(self, line):
        """Creates a new instance of BaseModel and prints the id"""
        """if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[line]()
            new_instance.save()
            print(new_instance.id)
        """
"""
    def do_show(self, line):
        ....Prints the string representation of an instance...
        if not line:
            print('** class name missing **')
        else:
            args = shlex.split(line)
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print('** instance id missing **')
            else:
                key = "{}.{}".format(args[0], args[1])
                instances = storage.all()
                if key not in instances:
                    print('** no instance found **')
                else:
                    print(instances[key])

    def do_destroy(self, line):
        ...Deletes an instance based on the class name and id...
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
            else:
                del instances[key]
                storage.save()

    def do_all(self, line):
        ...Prints all string representations of all instances...
        if not line or line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            f_instances = [str(value) for key, value in instances.items()
                           if line in key]
            print(f_instances)

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
