class TestSet():
    def test_set_1(self, return_set):
        return_set.add('y')
        assert 'y' in return_set, 'Элемент не в списке'

    def test_set_2(self, return_set):
        return_set.remove('h')
        assert 'h' not in return_set, 'Элемент в списке'

    def test_set_3(self, return_set):
        return_set.pop()
        assert len(return_set) < 4, 'Лишний элемент'

    def test_set_4(self, return_set):
        return_set.clear()
        assert len(return_set) == 0, 'Список не пуст'

    def test_set_5(self, return_set, fixture_witch_params_num):
        return_set.add(fixture_witch_params_num)
        assert fixture_witch_params_num in return_set, 'Элемент не в списке'




