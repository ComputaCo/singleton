import unittest

from singleton import Singleton


class TestSingleton(unittest.TestCase):
    def test_subclassing(self):
        """
        Tests that the Singleton class works via subclassing.
        """

        class Foo(Singleton):
            pass

        foo1 = Foo()
        foo2 = Foo.Singleton()
        self.assertEqual(foo1, foo2, "Singleton class doesn't work via subclassing.")

    def test_wrapping(self):
        """
        Tests that the Singleton class works via wrapping.
        """

        @Singleton.wrap
        class Foo:
            pass

        foo1 = Foo()
        foo2 = Foo.Singleton()
        self.assertEqual(foo1, foo2, "Singleton class doesn't work via wrapping.")


if __name__ == "__main__":
    unittest.main()
