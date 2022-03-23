import unittest
import requests
from api import YaDiskUser


tester = YaDiskUser()


class TestFunctions(unittest.TestCase):
    def test_get_token_1(self):
        self.assertIsInstance(tester.get_token('token.txt'), str)
    @unittest.expectedFailure
    def test_get_token_2(self):
        self.assertIsInstance(tester.get_token(''), str)

    def test_get_folder_info(self):
        self.assertIsInstance(tester.get_folder_info(''), requests.models.Response)

    def test_delete_folder(self):
        self.assertIsInstance(tester.delete_folder(''), requests.models.Response)


class TestFolderCreation(unittest.TestCase):
    @classmethod
    def setUpClass(TestFolderCreation):
        tester.delete_folder('test')

    @classmethod
    def tearDownClass(TestFolderCreation):
        tester.delete_folder('test')
    
    def test_create_folder_1(self):
        self.assertEqual(tester.create_folder('test').status_code, 201)
    
    def test_create_folder_2(self):
        self.assertEqual(tester.get_folder_info('test').status_code, 200)
