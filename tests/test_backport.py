import unittest

from importlib.metadata import version

import backport


class BackportTestCase(unittest.TestCase):
  def test_basic(self):
    self.assertEqual(version("backport"), backport.__version__)


if __name__ == "__main__":
  unittest.main()
