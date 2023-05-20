import pytest
from app.calculator import Calculator

class TestCalcul:
    def setup(self):
        self.calcul = Calculator

    def test_multiply(self):
        assert self.calcul.multiply(self, 5, 2) == 10

    def test_division(self):
        assert self.calcul.division(self, 12, 6) == 2

    def test_subtraction(self):
        assert self.calcul.subtraction(self, 10, 7) == 3

    def test_adding(self):
        assert  self.calcul.adding(self, 3, 2) == 5