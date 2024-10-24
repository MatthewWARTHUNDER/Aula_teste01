def soma (a, b):
    return a + b

def subtração (a, b):
    return a - b

def multiplicação (a, b):
    return a * b

def divisão (a, b):
    return a / b

def test_se_a_mais_b():
    assert soma (8, 9) == 17
    assert soma (5, 5) == 10
    assert soma (6, 7) == 13

def test_se_a_menos_b():
    assert subtração (5, 3) == 2
    assert subtração (3, 3) == 0
    assert subtração (4, 2) == 2

def test_se_a_vezes_b():
    assert multiplicação (5, 5) == 25
    assert multiplicação (6, 6) == 36
    assert multiplicação (6, 4) == 24

def test_se_a_dividos_b():
    assert divisão (4, 2) == 2
    assert divisão (6, 2) == 3
    assert divisão (64, 8) == 8