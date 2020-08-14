#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8
from models.place import Place
import MySQLdb
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class test_User(unittest.TestCase):
    """ """

    def setUp(self):
        """ check for the right type of datastorage otherwise skiptheTest """
        if os.getenv("HBNB_TYPE_STORAGE") != "FileStorage":
            raise unittest.SkipTest("because is not using Filstorage")

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        self.assertTrue(len(User.__init__.__doc__) > 1)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)


class test_User_db_storage(unittest.TestCase):
    """ test for checking deb_storage """

    @classmethod
    def setUpClass(cls):
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            cls.storage = DBStorage()
            cls.storage.reload()
            cls.state = State(name="California")
            cls.state.save()
            # creation of a City
            cls.city = City(state_id=cls.state.id, name="San Francisco")
            cls.city.save()
            # creation of a User
            cls.user = User(email="john@snow.com", password="johnpwd")
            cls.user.save()
            # creation of a place
            cls.place = Place(user_id=cls.user.id,
                              city_id=cls.city.id, name="House 1")
            cls.place.save()

            cls.storage.save()

    def setUp(self):
        """ check for the right type of datastorage otherwise skiptheTest """
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            self.skipTest("because is not using db_storage")
        self.connection()

    def tearDown(self):
        self.cursor.close()
        self.storage.close()

    def connection(self):
        """ set the connection for the database MYSQL """
        my_user = os.getenv("HBNB_MYSQL_USER")
        my_passw = os.getenv("HBNB_MYSQL_PWD")
        my_host = os.getenv("HBNB_MYSQL_HOST")
        my_db = os.getenv("HBNB_MYSQL_DB")

        self.db = MySQLdb.connect(host=my_host, db=my_db, user=my_user,
                                  passwd=my_passw, port=3306)
        # creation of 2 Places
        self.cursor = self.db.cursor()

    def test_Place_id(self):
        """ Test when creating Places """
        self.cursor.execute(
            """SELECT id FROM users""")
        query = self.cursor.fetchall()
        lista = []
        for id in query:
            lista.append(id[0])
        self.assertIn(self.user.id, lista)

        self.cursor.close()

    def test_Place_attribute(self):
        """test Place adds an attribute when instanciating it"""

        self.cursor.execute(
            """SELECT email FROM users""")
        query = self.cursor.fetchall()
        lista = []
        for name in query:
            lista.append(name[0])
        self.assertIn(self.user.email, lista)
        self.cursor.close()

    def test_type(self):
        """test the type of the class """
        self.assertTrue(type(self.user), User)


if __name__ == "__main__":
    unittest.main()
