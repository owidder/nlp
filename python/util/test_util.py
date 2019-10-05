import unittest

from .util import rel_path_from_abs_path


class UtilTestCase(unittest.TestCase):
    def test_with_trailing_slash(self):
        rel_path = rel_path_from_abs_path("/a/b/", "/a/b/c/d")
        self.assertEqual(rel_path, "c/d")

    def test_with_no_trailing_slash(self):
        rel_path = rel_path_from_abs_path("/a/b", "/a/b/c/d")
        self.assertEqual(rel_path, "c/d")


if __name__ == '__main__':
    unittest.main()
