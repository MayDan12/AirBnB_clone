import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_uuid(self):
        """ tests on the uuid """
        model1 = BaseModel()
        model2 = BaseModel()
        
        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model2, BaseModel)
        self.assertTrue(hasattr(model1, "id"))
        self.assertNotEqual(model1.id, model2.id, "")
    