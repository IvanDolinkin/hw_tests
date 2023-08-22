from unittest import TestCase
from Task2 import create_folder, delete_folder, get_info, DISK_TOKEN, path


class TestCreateFolder(TestCase):

    def test_creation(self):
        delete_folder(DISK_TOKEN, path)
        expected = 201
        result = create_folder(DISK_TOKEN, path)
        self.assertEqual(result, expected)

    def test_created(self):
        create_folder(DISK_TOKEN, path)
        expected = 409
        result = create_folder(DISK_TOKEN, path)
        self.assertEqual(result, expected)

    def test_folder_exists(self):
        create_folder(DISK_TOKEN, path)
        expected = 200
        result = get_info(DISK_TOKEN, path).status_code
        self.assertEqual(result, expected)

    def test_folder_not_exists(self):
        delete_folder(DISK_TOKEN, path)
        expected = 404
        result = get_info(DISK_TOKEN, path).status_code
        self.assertEqual(result, expected)
