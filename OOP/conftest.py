from OOP.GeometricalFigure import Triangle, Rectangle, Quadrate, Circle, FakeClass
import pytest


@pytest.fixture()
def trin_obj():
    trin_obj = Triangle(name='my_trin', a=12, b=13, c=5, h=12)
    return trin_obj


@pytest.fixture()
def rect_obj():
    rect_obj = Rectangle(name='my_rect', a=12, b=13)
    return rect_obj


@pytest.fixture()
def quad_obj():
    quad_obj = Quadrate(name='my_quad', a=12)
    return quad_obj


@pytest.fixture()
def circl_obj():
    circl_obj = Circle(name='my_circl', r=6)
    return circl_obj

@pytest.fixture()
def fake_obj():
    fake_obj = FakeClass()
    return fake_obj