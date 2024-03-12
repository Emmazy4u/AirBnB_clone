import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """General test for the FileStorage"""
    def setUp(self):
        """create a temp test file for saving data"""
        self.test_f = "test_file.json"

    def tearDown(self):
        """remove the temp test file after test completion"""
        if os.path.exists(self.test_f):
            os.remove(self.test_f)

    def test_all_storage_returns_dict(self):
        """Test whether the all() method returns a dictionary"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """test the new method by creating and storing a new obj"""
        obj = BaseModel()
        models.storage.new(obj)
        all = models.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all)

    def test_new_with_arg(self):
        """test the creation of new obj with more args
        ----it has to raise TypeError-----
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)
    def test_new_with_None(self):
        """test the new method by passing None
        -----it should raise an AttributeError---
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_N_reload(self):
        """test saving and reloading obj to a file"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()
        # creating the new storage instance for reloading
        new_storage = FileStorage()
        new_storage.reload()
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_reload_empty_file(self):
        """Test reloading upon file being empty or doesn't exist"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

    def test_saving_to_file(self):
        """Checks success of saving into file or creating a new one"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

class TestFileStorageInit(unittest.TestCase):
    """Test for the instantiation of the file storage"""
    
    def test_FileStorage_inst_without_args(self):
        """Creating a FileStorage inst without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_inst_with_args(self):
        """Tests creating a FileStorage instance with an arg"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initials(self):
        """Test if the storage variable in models is an instance of fileStorage"""
        self.assertEqual(type(models.storage), FileStorage)

if __name__ == "__main__":
    unittest.main()
