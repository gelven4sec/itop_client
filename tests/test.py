import unittest

import tests.parameters as param
from itop_client import ITopClient


class TestITopClient(unittest.TestCase):
    def test_check_credentials(self):
        """
        Test credentials in parameters.py
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        is_valid = client.check_credentials()
        self.assertEqual(is_valid, True)

    def test_get_object_by_id(self):
        """
        Test getting the content an object by dictonary from the reference in parameters.py
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        ref = param.ID

        objects = client.get_object(param.CLASS, ref)
        self.assertNotEqual(len(objects), 0)

    def test_get_object_by_disctonary(self):
        """
        Test getting the content an object by dictonary from the reference in parameters.py
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        ref = {"ref": param.REF}

        objects = client.get_object(param.CLASS, ref)
        self.assertNotEqual(len(objects), 0)

    def test_get_object_by_oql(self):
        """
        Test getting the content an object by oql from the reference in parameters.py
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        ref = f"SELECT {param.CLASS} WHERE ref = '{param.REF}'"

        objects = client.get_object(param.CLASS, ref)
        self.assertNotEqual(len(objects), 0)

    def test_get_object_with_output_fields(self):
        """
        Test getting the content an object with specific output fields
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        ref = param.ID
        output_fields = ["status", "caller_id"]

        objects = client.get_object(param.CLASS, ref, output_fields)
        self.assertTrue(list(objects[0]["fields"].keys()) == output_fields)

    def test_update_object(self):
        """
        Test updating an object
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        ref = param.ID
        fields = {"status": "resolved"}
        output_fields = "status"

        objects = client.update_object(param.CLASS, ref, fields, output_fields)
        self.assertEqual(objects[0]["fields"]["status"], "resolved")

    def test_create_object(self):
        """
        Test creating an object
        """
        client = ITopClient(param.BASE_URL, param.USER, param.PASS, param.VERIFY)

        fields = param.FIELDS

        objects = client.create_object(param.CLASS, fields, output_fields=[])
        self.assertEqual(objects[0]["code"], 0)


if __name__ == '__main__':
    unittest.main()
