#!/usr/bin/python3
"""package that contains the modules"""


from models.engine.file_storage import FileStorage

storage = FileStorage() # creates a FileStorage instance
storage.reload() # calls the FileStorage reload method
