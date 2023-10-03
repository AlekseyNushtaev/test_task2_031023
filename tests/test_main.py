from unittest import TestCase
from main import yadisk_folder_create, yadisk_folder_delete

class TestFolder(TestCase):
    def setUp(self):
        self.token = '' # Введите свой токен
    def tearDown(self):
        yadisk_folder_delete(self.token)
    def test_1_folder_create(self):
        self.assertIn(yadisk_folder_create(self.token), range(200, 300))
    def test_2_not_auth(self):
        self.assertEqual(yadisk_folder_create(self.token), 401)
    def test_3_alredy_create(self):
        self.assertEqual(yadisk_folder_create(self.token), 409)