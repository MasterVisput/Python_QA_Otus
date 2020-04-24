class TestString():
    def test_string_1(self, return_string):
        assert return_string.isalpha(), 'В строке есть цифры'


    def test_string_2(self, return_string):
        upp_string = return_string.upper()
        assert upp_string.isupper(), 'Строка в нижнем регистре'

    def test_string_3(self, return_string):
        t_string = return_string.title()
        assert t_string.istitle(), 'Первая буква строки не заглавная'

    def test_string_4(self, return_string):
        assert return_string.islower(), 'Строка не в нижнем регистре'

    def test_string_5(self, return_string, fixture_witch_params_word):
        new_word = return_string + fixture_witch_params_word
        assert fixture_witch_params_word in new_word, 'Некорректное содержание'



