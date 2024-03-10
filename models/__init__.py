#!/usr/bin/python3
"""package that contains the modules"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
