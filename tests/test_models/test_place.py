#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_for_no_args_init(self):
        self.assertEqual(Place, type(Place()))

    def test_for_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_for_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_for_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_for_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_for_city_id_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_for_user_id_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_for_name_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_for_description_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("description", pl.__dict__)

    def test_for_number_rooms_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_for_number_bathrooms_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_for_max_guest_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_for_price_by_night_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_for_latitude_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_for_longitude_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_for_amenity_ids_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_for_two_places_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_for_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.04)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_for_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.04)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_for_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_for_unused_args(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_for_init_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_for_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("storage.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("storage.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "storage.json")
        except IOError:
            pass

    def test_for_one_save(self):
        pl = Place()
        sleep(0.04)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_for_two_saves(self):
        pl = Place()
        sleep(0.04)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.04)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_for_save_with_args(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_for_save_updates(self):
        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("storage.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_for_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_for_to_dict_contains_keys(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_for_to_dict_contains_added_attr(self):
        pl = Place()
        pl.middle_name = "Holbert"
        pl.my_number = 985
        self.assertEqual("Holbert", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_for_to_dict_datetime_attr_is_str(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_for_to_dict_output(self):
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_for_contrast_to_dict_dunder_dict(self):
        p = Place()
        self.assertNotEqual(p.to_dict(), p.__dict__)

    def test_for_to_dict_with_arg(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.to_dict(None)


if __name__ == "__main__":
    unittest.main()
