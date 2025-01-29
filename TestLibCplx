import unittest
import libcplx as lb
import math

class TestLibCplx(unittest.TestCase):
    def test_sumaCplx(self):
        self.assertEqual(lb.sumaCplx((1, 2), (3, 4)), (4, 6))
        self.assertEqual(lb.sumaCplx((-1, -2), (3, 5)), (2, 3))

    def test_restaCplx(self):
        self.assertEqual(lb.restaCplx((5, 7), (3, 4)), (2, 3))
        self.assertEqual(lb.restaCplx((-2, -3), (-1, -1)), (-1, -2))

    def test_multiplicarCplx(self):
        self.assertEqual(lb.multiplicarCplx((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(lb.multiplicarCplx((2, -3), (-1, 4)), (10, 11))

    def test_dividirCplx(self):
        self.assertEqual(lb.dividirCplx((4, 2), (3, -1)), (1, 1))
        self.assertEqual(lb.dividirCplx((2, 3), (1, -1)), (-0.5, 2.5))

    def test_moduloCplx(self):
        self.assertEqual(lb.moduloCplx((3, 4)), 5.0)
        self.assertEqual(lb.moduloCplx((1, 1)), round(math.sqrt(2), 4))

    def test_conjugadoCplx(self):
        self.assertEqual(lb.conjugadoCplx((3, 4)), (3, -4))
        self.assertEqual(lb.conjugadoCplx((-2, -5)), (-2, 5))

    def test_convertirCoordenadas(self):
        cart = lb.convertirCoordenadas((1, math.pi / 4), "cartesiano")
        self.assertAlmostEqual(cart[0], math.sqrt(2) / 2)
        self.assertAlmostEqual(cart[1], math.sqrt(2) / 2)

        polar = lb.convertirCoordenadas((3, 4), "polar")
        self.assertAlmostEqual(polar[0], 5.0)
        self.assertAlmostEqual(polar[1], lb.calcularFaseCplx((3, 4)))

    def test_calcularFaseCplx(self):
        self.assertEqual(lb.calcularFaseCplx((1, 1)), round(math.atan2(1, 1), 4))
        self.assertEqual(lb.calcularFaseCplx((0, 1)), round(math.pi / 2, 4))


if __name__ == "__main__":
    unittest.main()
