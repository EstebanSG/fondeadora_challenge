from scripts.array_flattening import ArrayFlattening


class TestClass:
    def test_correct_input(self):
        af = ArrayFlattening()
        assert af.array_flattening([1, [2, [3, [4, 5]]]]) == [1, 2, 3, 4, 5]

    def test_wrong_input(self):
        af = ArrayFlattening()
        assert af.array_flattening((1, (2, (3, (4, 5))))) == (1, (2, (3, (4, 5))))

    def test_wrong_element_type_one(self):
        af = ArrayFlattening()
        assert af.array_flattening([1, [2, [3, (4, 5)]]]) == [3, (4, 5)]

    def test_wrong_element_type_two(self):
        af = ArrayFlattening()
        assert af.array_flattening([1, [2, [3, [4, "Esto no es un numero"]]]]) == \
               [4, "Esto no es un numero"]


if __name__ == '__main__':
    test = TestClass()
    test.test_correct_input()
    test.test_wrong_input()
    test.test_wrong_element_type_one()
    test.test_wrong_element_type_two()
