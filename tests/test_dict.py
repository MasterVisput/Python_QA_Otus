class TestDict():
    def test_dict_1(self, return_dict):
        cost = return_dict.get('банан')
        assert cost == 1, 'Некорректная цена'

    def test_dict_2(self, return_dict):
        products = return_dict.keys()
        assert 'яблоко' in products, 'Продукта нет в списке'

    def test_dict_3(self, return_dict):
        costs = return_dict.values()
        assert 4 in costs, 'Некорректная цена'

    def test_dict_4(self, return_dict):
        return_dict.pop('груша')
        assert 'груша' not in return_dict, 'Лишний элемент в списке'

    def test_dict_5(self, return_dict, fixture_witch_params_num, fixture_witch_params_word):
        return_dict[fixture_witch_params_word] = fixture_witch_params_num
        assert return_dict.get(fixture_witch_params_word) > 10, 'Некорректная цена'




