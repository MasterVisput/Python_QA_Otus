
class TestTriangle:

    def test_name(self,trin_obj):
        assert trin_obj.name == 'my_trin', 'Некорректное содержание атрибута name'

    def test_area(self, trin_obj):
        assert trin_obj.get_area() == 78.0, f'Некорректное значение площади фигуры, ответ системы: {trin_obj.get_area()}'

    def test_angles(self, trin_obj):
        assert trin_obj.get_angles() == 3, f'Некорректный ответ, ожидалось углов = 3, ответ = {trin_obj.get_angles()}'

    def test_perimeter(self, trin_obj):
        assert trin_obj.get_perimeter() == 30, f'Некорректный ответ, ожидалось периметер = 30, ответ = {trin_obj.get_perimeter()}'

    def test_add_square(self, trin_obj, quad_obj):
        sum_area = trin_obj.add_square(quad_obj)
        assert sum_area == 174, f'Некорректный ответ, ожидалось сумма площадей = 174, ответ = {sum_area}'

    def test_add_fake_object(self, trin_obj, fake_obj):
        sum_area = trin_obj.add_square(fake_obj)
        assert sum_area == 'Переданный объект не является экземпляром класса GeometricalFigure!', 'Ожидалось сообещние об ошибке'

class TestRectangle:

    def test_name(self,rect_obj):
        assert rect_obj.name == 'my_rect', 'Некорректное содержание атрибута name'

    def test_area(self, rect_obj):
        assert rect_obj.get_area() == 156, f'Некорректное значение площади фигуры, ответ системы: {rect_obj.get_area()}'

    def test_angles(self, rect_obj):
        assert rect_obj.get_angles() == 4, f'Некорректный ответ, ожидалось углов = 3, ответ = {rect_obj.get_angles()}'

    def test_perimeter(self, rect_obj):
        assert rect_obj.get_perimeter() == 50, f'Некорректный ответ, ожидалось периметер = 30, ответ = {rect_obj.get_perimeter()}'

    def test_add_square(self, rect_obj, quad_obj):
        sum_area = rect_obj.add_square(quad_obj)
        assert sum_area == 194, f'Некорректный ответ, ожидалось сумма площадей = 174, ответ = {sum_area}'

    def test_add_fake_object(self, rect_obj, fake_obj):
        sum_area = rect_obj.add_square(fake_obj)
        assert sum_area == 'Переданный объект не является экземпляром класса GeometricalFigure!', 'Ожидалось сообещние об ошибке'


class TestQuadrate:

    def test_name(self,quad_obj):
        assert quad_obj.name == 'my_quad', 'Некорректное содержание атрибута name'

    def test_area(self, quad_obj):
        assert quad_obj.get_area() == 144, f'Некорректное значение площади фигуры, ответ системы: {quad_obj.get_area()}'

    def test_angles(self, quad_obj):
        assert quad_obj.get_angles() == 4, f'Некорректный ответ, ожидалось углов = 3, ответ = {quad_obj.get_angles()}'

    def test_perimeter(self, quad_obj):
        assert quad_obj.get_perimeter() == 48, f'Некорректный ответ, ожидалось периметер = 30, ответ = {quad_obj.get_perimeter()}'

    def test_add_square(self, trin_obj, quad_obj):
        sum_area = trin_obj.add_square(quad_obj)
        assert sum_area == 174, f'Некорректный ответ, ожидалось сумма площадей = 174, ответ = {sum_area}'

    def test_add_fake_object(self, quad_obj, fake_obj):
        sum_area = quad_obj.add_square(fake_obj)
        assert sum_area == 'Переданный объект не является экземпляром класса GeometricalFigure!', 'Ожидалось сообещние об ошибке'

class TestCircle:

    def test_name(self,circl_obj):
        assert circl_obj.name == 'my_circl', 'Некорректное содержание атрибута name'

    def test_area(self, circl_obj):
        assert int(circl_obj.get_area()) == 113, f'Некорректное значение площади фигуры, ответ системы: {circl_obj.get_area()}'

    def test_angles(self, circl_obj):
        assert circl_obj.get_angles() == 0, f'Некорректный ответ, ожидалось углов = 3, ответ = {circl_obj.get_angles()}'

    def test_perimeter(self, circl_obj):
        assert int(circl_obj.get_perimeter()) == 37, f'Некорректный ответ, ожидалось периметер = 30, ответ = {circl_obj.get_perimeter()}'

    def test_add_square(self, circl_obj, quad_obj):
        sum_area = int(circl_obj.add_square(quad_obj))
        assert sum_area == 181, f'Некорректный ответ, ожидалось сумма площадей = 174, ответ = {sum_area}'

    def test_add_fake_object(self, fake_obj, circl_obj):
        sum_area = circl_obj.add_square(fake_obj)
        assert sum_area == 'Переданный объект не является экземпляром класса GeometricalFigure!', 'Ожидалось сообещние об ошибке'

