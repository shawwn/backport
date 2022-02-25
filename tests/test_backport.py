from __future__ import annotations

import backport

import abc
from backport import dataclasses
from backport import types
from backport import typing
import unittest

from importlib.metadata import version


class BackportTestCase(unittest.TestCase):
  def test_basic(self):
    self.assertEqual(version("backport"), backport.__version__)
    self.assertRegex(types.__name__, '^backport[.]')
    self.assertRegex(typing.__name__, '^backport[.]')
    self.assertRegex(dataclasses.__name__, '^backport[.]')


if __name__ == "__main__":
  unittest.main()
