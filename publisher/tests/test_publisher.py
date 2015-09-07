import unittest2

from publisher import publisher as pp


class TestPublisher(unittest2.TestCase):
    def test_positive(self):
        assert pp.MyFunction(1) == 2

    def test_negative(self):
        assert pp.MyFunction(1) == 1
