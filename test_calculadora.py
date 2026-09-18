import unittest

from calculadora import (
    dividir,
    multiplicar,
    porcentagem,
    potencia,
    raiz_quadrada,
    somar,
    subtrair,
)


class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 4), 2.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 10), 1024)

    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(81), 9)

    def test_raiz_negativa(self):
        with self.assertRaises(ValueError):
            raiz_quadrada(-4)

    def test_porcentagem(self):
        self.assertEqual(porcentagem(200, 10), 20)


if __name__ == "__main__":
    unittest.main()
