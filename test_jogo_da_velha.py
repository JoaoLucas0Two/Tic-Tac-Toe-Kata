import unittest
from jogo_da_velha import verificar_vitoria, verificar_empate

class TestJogoDaVelha(unittest.TestCase):
    def test_vitoria_linha(self):
        tabuleiro = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertTrue(verificar_vitoria(tabuleiro, "X"))
        self.assertFalse(verificar_vitoria(tabuleiro, "O"))

    def test_vitoria_coluna(self):
        tabuleiro = [
            ["O", "X", " "],
            ["O", "X", " "],
            ["O", " ", "X"]
        ]
        self.assertTrue(verificar_vitoria(tabuleiro, "O"))
        self.assertFalse(verificar_vitoria(tabuleiro, "X"))

    def test_vitoria_diagonal_principal(self):
        tabuleiro = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertTrue(verificar_vitoria(tabuleiro, "X"))

    def test_vitoria_diagonal_secundaria(self):
        tabuleiro = [
            [" ", "O", "X"],
            ["O", "X", " "],
            ["X", " ", " "]
        ]
        self.assertTrue(verificar_vitoria(tabuleiro, "X"))

    def test_empate(self):
        tabuleiro = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(verificar_empate(tabuleiro))
        self.assertFalse(verificar_vitoria(tabuleiro, "X"))
        self.assertFalse(verificar_vitoria(tabuleiro, "O"))

    def test_nao_empatou_espaco_vazio(self):
        tabuleiro = [
            ["X", "O", "X"],
            ["O", " ", "O"],
            ["O", "X", "X"]
        ]
        self.assertFalse(verificar_empate(tabuleiro))

if __name__ == '__main__':
    unittest.main()
