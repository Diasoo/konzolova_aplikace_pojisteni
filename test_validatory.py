from unittest import TestCase
from validatory import zadej_beznou_hodnotu, zadej_vek, zadej_telefon

class Test(TestCase):
    def test_zadej_beznou_hodnotu(self):
        self.assertTrue(zadej_beznou_hodnotu("test", "test"))
        self.assertFalse(zadej_beznou_hodnotu("", "test"))
        self.assertFalse(zadej_beznou_hodnotu(" ", "test"))

    def test_zadej_vek(self):
        self.assertTrue(zadej_vek("25"))
        self.assertFalse(zadej_vek("0"))
        self.assertFalse(zadej_vek("121"))
        self.assertFalse(zadej_vek("-5"))

    def test_zadej_telefon(self):
        self.assertTrue(zadej_telefon("123456789"))
        self.assertTrue(zadej_telefon("123456789012aaa"))
        self.assertFalse(zadej_telefon("12345678"))
        self.assertFalse(zadej_telefon("1234567890123456"))