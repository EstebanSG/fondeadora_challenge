import pytest
from scripts.array_flattening import ArrayFlattening


class TestClass:
    def test_one(self):
        x = [1, [2, [3, [4, 5]]]]
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")