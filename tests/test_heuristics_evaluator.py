import sys
import os
import unittest
# Agregar carpeta src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.ai.heuristics import generar_regex_heuristica
from src.ai.evaluator import evaluar_regex

class TestHeuristics(unittest.TestCase):
    def test_generar_regex_heuristica(self):
        positivos = ["abc123", "abc456", "abc789"]
        regex = generar_regex_heuristica(positivos)
        self.assertTrue(regex.startswith("^abc"))

class TestEvaluator(unittest.TestCase):
    def test_evaluar_regex(self):
        regex = r"^abc\\d{3}$"
        positivos = ["abc123", "abc456"]
        negativos = ["ab123", "abc12", "xyz123"]
        resultado = evaluar_regex(regex, positivos, negativos)
        self.assertTrue(resultado["positivos_ok"])
        self.assertTrue(resultado["negativos_ok"])
        self.assertTrue(resultado["validez"])

if __name__ == "__main__":
    unittest.main()
