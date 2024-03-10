ALX SE PROJECT - 0x00. AirBnB clone - The console
---------------------------------------------------

### Description of the project
The AirBnB clone project is aimed at developing a simplified version of the AirBnB website. The goal is to create a web application that includes a command interpreter, a website with both static and dynamic elements, a database or file storage system to store data, and a RESTful API for communication between the front-end and the data.

### Description of the command interpreter:
The command interpreter is a tool that allows users to manipulate data without a visual interface, similar to a Shell. It serves as the entry point for interacting with the application's functionality, such as creating, updating, and deleting objects, as well as querying data.

### How to start it:
To start the command interpreter, you need to run the `console.py` file. This file serves as the entry point for the command interpreter. You can run it using the following command:

```
python3 console.py OR ./console.py
```

### How to use it:
Once the command interpreter is started, you will see a prompt `(hbnb)`. You can then enter various commands to interact with the application. Some of the commands available include:

- `create`: Create a new instance of a specified object type.
- `show`: Display the string representation of a specific instance.
- `destroy`: Delete a specific instance.
- `all`: Display all instances of a specified object type.
- `update`: Update an instance based on the class name and id.

### Examples:
Here are some examples of how to use the command interpreter:

1. Creating a new instance:
   ```
   (hbnb) create BaseModel
   ```

2. Showing an instance:
   ```
   (hbnb) show BaseModel <valid_id>
   ```

3. Deleting an instance:
   ```
   (hbnb) destroy BaseModel <valid_id>
   ```

4. Displaying all instances:
   ```
   (hbnb) all
   ```

5. Updating an instance:
   ```
   (hbnb) update BaseModel <valid_id> <new_attribute> <new_attribute_value>
   ```

These are just a few examples of the commands available in the command interpreter. You can explore more commands and functionalities as needed for your application.



### PROJECT DETAILS:

Weight: 5

LEARNING OBJECTIVES:
General
*How to create a Python package
*How to create a command interpreter in Python using the cmd module
*What is Unit testing and how to implement it in a large project
*How to serialize and deserialize a Class
*How to write and read a JSON file
*How to manage datetime
*What is an UUID
*What is *args and how to use it
*What is **kwargs and how to use it
*How to handle named arguments in a function

REQUIREMENTS:
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case
GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.