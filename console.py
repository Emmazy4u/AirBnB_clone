#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import sys
import shlex
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    
    def do_greet(self, line):
        """function that prints hello"""
        names = shlex.split(line)
        for name in names:
            print('hello', name)


    def do_EOF(self, line):
        """function that exits the console"""
        print('exit')
        return True
    
    
    def do_quit(self, line):
        """ command that quits the program"""
        print('exit')
        return True
    
    
    def emptyline(self):
       """ returns nothing on ENTER"""
       pass
   
   
    def do_create(self, line):
       """creates a new instance  of BaseModel and prints the id"""
       if !line:
           print("** class name missing **")
       elif line not in storage.classes():
           print("** class doesn't exist **")
       else:
           new_instance = storage.classes[line]()
           new_instance.save()
           print(new_instance.id)

   
    def do_show(self, line):
       """prints the string representation of an instance"""
       if !line:
           print('** class name missing **')
       else:
           className = line.split(' ')
           if className[0] not in storage.classes():
               print("** class doesn't exist **")
           elif len(className) < 2:
               print('** instance id missing **')
           else:
               key = "{}.{}".format(className[0], className[1])
               if key not in storage.all():
                   print('** no instance found **')
               else:
                   print(storage.all()[key])


   def do_destroy(self, line):
      """deletes an instance based on the class name and id"""
      line = line.split(" ")
      if !line:
          print('** class name missing **')
      else:
          className = line[0]
          if className not in storage.classes():
              print("** class doesn't exist **")
          elif len(className) < 2:
              print('** instance id missing **')
              key = f"{className[0]}.{className[1]}"
              if key not in storage.all():
                  print('** no instance found **')
              else:
                  del storage.all()[key]
                  storage.save


    def do_all(self, line):
        """prints all string representation of all instances based or not on the class name"""
        instance_obj = storage.all()
        instance_list = []

        if line != "":
            for key, value in storage.all().items():
                instance_list.append(str[value])
            print(instance_list)
        else:
            if line not in storage.classes():
                print("** class doesn't exist **")


   def do_count(self, line):
        """counts the instances of a class"""
        counter = 0
        for key in storage.all().keys():
            className ,instance_id = key.split(',')
            if line == className:
                counter += 1
         print(counter)


   def do_update(self, line):
       """Updates an instance based on the class name and id by adding or updating attribute"""
       if !line:
           print('** class name missing **')
       else:
           className = line.split(" ")
           if className[0] not in storage.classes():
               print("** class doesn't exist **")
               return
           if len(className) < 2:
               print('** instance id missing **')
               return
           key = f"{className[0]}.{className[1}}"
           for key not in storage.all():
               print('** no instance found **')
               if len(className) < 3:
                   print("** attribute name missing **")
                   return
               if len(className) < 4:
                   print("** value missing **")
                   return







if __name__ == '__main__':
    HBNBCommand().cmdloop()
