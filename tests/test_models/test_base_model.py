#!/usr/bin/python3
"""Test cases for the base_model"""

import unittest
from ...models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
	def setUp(self):
		self.demo_model = BaseModel()

	def test_init(self):
		self.assertIsNotNone(self.demo_model.id)
		self.assertIsNotNone(self.demo_model.created_at)
		self.assertIsNotNone(self.demo_model.updated_at)

	def test_save(self):
		init_updated_at = self.demo_model.updated_at
		current_updated_at = self.demo_model.save()
		self.assertNotEqual(current_updated_at, init_updated_at)
	
	def test_to_dict(self):
		demo_model_dict = self.demo_model.to_dict()
		self.assertIsInstance(demo_model_dict, dict)
		self.assertEqual(demo_model_dict["__class__"], "BaseModel")
		self.assertEqual(demo_model_dict['id'], self.demo_model.id)
		created_at_iso = self.demo_model.created_at.isoformat()
		updated_at_iso = self.demo_model.updated_at.isoformat()
		self.assertEqual(demo_model_dict['created_at'], created_at_iso)
		self.assertEqual(demo_model_dict['updated_at'], updated_at_iso)

	def test_str(self):
		self.assertTrue(str(self.demo_model).startswith('[BaseModel]'))
		self.assertIn(str(self.demo_model.id), str(self.demo_model))
		self.assertIn(str(self.demo_model.__dict__), str(self.demo_model))

if __name__ == "__main__":
	unittest.main()