# Carlos Massato Horibe Chinen - 22.221.010-6
# Gabriel Nunes Missima - 
# Vinicius Alves Pedro - 

import unittest
import os
from parser_init import Parser, gerar_pdf

class TestParser(unittest.TestCase):
    """Testes Unitários"""
    
    def setUp(self):
        self.parser = Parser("artigo.xml")
    
    def test_get_titulo(self):
        titulo = self.parser.get_titulo()
        self.assertEqual(titulo, "Uma Abordagem para Testes de Software Baseados em Inteligência Artificial")
        print("\nUT-01:", titulo)

    def test_get_autores(self):
        autores = self.parser.get_autores()
        self.assertEqual(autores, ["João Silva", "Maria Oliveira"])
        print("\nUT-02:", autores)
    
    def test_get_resumo(self):
        resumo = self.parser.get_resumo()
        self.assertTrue("inteligência artificial" in resumo)
        print("\nUT-03:", resumo)
    
    def test_get_secoes(self):
        secoes = self.parser.get_secoes()
        self.assertGreater(len(secoes), 0)
        print("\nUT-04:", secoes)
    
    def test_get_referencias(self):
        referencias = self.parser.get_referencias()
        self.assertGreater(len(referencias), 0)
        print("\nUT-05:", referencias)

    def test_fluxo_xml_malformado(self):
        self.parser = Parser("xml_malformado.xml")
        print("\nUT-06: XML malformado testado")
    
    def test_get_titulo_sem_titulo(self):
        parser_sem_titulo = Parser("xml_sem_titulo.xml")
        titulo = parser_sem_titulo.get_titulo()
        self.assertIsNone(titulo)
        print("\nUT-07:", titulo)
    
    def test_get_autores_sem_autores(self):
        parser_sem_autores = Parser("xml_sem_autores.xml")
        autores = parser_sem_autores.get_autores()
        self.assertEqual(autores, [])
        print("\nUT-08:", autores)
    
    def test_get_referencias_incompletas(self):
        parser_referencias = Parser("xml_referencias_incompletas.xml")
        referencias = parser_referencias.get_referencias()
        self.assertTrue("Título desconhecido" in referencias[0])
        print("\nUT-09:", referencias)
    
    def test_titulo_longo(self):
        parser_titulo_longo = Parser("xml_titulo_longo.xml")
        titulo = parser_titulo_longo.get_titulo()
        self.assertGreater(len(titulo), 100)
        print("\nUT-10:", titulo)
    
    def test_resumo_e_secoes_vazias(self):
        parser_vazio = Parser("xml_vazio.xml")
        resumo = parser_vazio.get_resumo()
        secoes = parser_vazio.get_secoes()
        self.assertEqual(resumo, "")
        print("\nUT-11:", resumo)
        print("\nUT-11:", secoes)
    
    def test_resumo_longo(self):
        parser_resumo_longo = Parser("xml_resumo_longo.xml")
        resumo = parser_resumo_longo.get_resumo()
        self.assertGreater(len(resumo), 500)
        print("\nUT-12:", resumo)


if __name__ == "__main__":
    unittest.main()
