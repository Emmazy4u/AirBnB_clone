#!/usr/bin/python3
import cmd

class cmd_console(cmd.Cmd):
	prompt = "(hbnb)"
	def do_test(self, arg):
		print("you typed: {}".format(arg))
	
	def do_exit(self, arg):
		return (True)

if __name__ == "__main__":
	cmd_console().cmdloop()