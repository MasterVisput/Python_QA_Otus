
def test_one(first_fixture):
    pass


class TestFunction():
    def test_from_test_class_one(self, second_fixture):
        pass

    def test_from_test_class_two(self,first_fixture, third_fixture):
        pass

    def test_guess_num(self, random_num):
        assert random_num % 2 == 0, 'Число не чётное!'
