import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_base_instance(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b = Base()
        self.assertEqual(b.id, 2)

        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_rectangle_instance(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(3, 4, 1, 2, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_invalid_rectangle_arguments(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle("invalid", 4)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 4)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(2, 4)
            r.width = "invalid"
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(2, 4)
            r.width = 0
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(2, 4)
            r.x = "invalid"
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(2, 4, -1, 0)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(2, 4)
            r.y = "invalid"
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(2, 4, 0, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")


if __name__ == "__main__":
    unittest.main()
