from src.first import FirstClass


def test_first_class():
    assert True
    c1 = FirstClass()
    assert c1.name == "FirstClass"