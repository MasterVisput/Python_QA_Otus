import pytest

class TestList():
    def test_list_1(self, return_list, random_num):
        return_list.append(random_num)
        assert random_num in return_list, 'Число не в списке'

    def test_list_2(self, return_list):
        return_list.pop()
        assert len(return_list) == 9, 'В списке 9 элементов.'

    def test_list_3(self, return_list):
        return_list.sort()
        assert return_list[0] < return_list[9], 'Список отсортирован не корректно.'


    def test_list_4(self, return_list):
        test_list = return_list.copy()
        return_list.extend(test_list)
        assert len(return_list) == 20, 'Некорректная длинна списка'

    @pytest.mark.parametrize('data', ['a', 'b', 'c', 'r', 'k'])
    def test_list_5(self, return_list, data):
        return_list.insert(0, data)
        assert data in return_list, 'Данные не добавлены'


