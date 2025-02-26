# Carlos Massato Horibe Chinen - 22.221.010-6
# Gabriel Nunes Missima - 
# Vinicius Alves Pedro - 

import unittest
import os
from parser_init import Parser, gerar_pdf

class TestIntegracao(unittest.TestCase):
    """Testes de Integração"""
    
    def setUp(self):
        self.parser = Parser("artigo.xml")
    
    def test_extracao_e_formatacao(self):
        dados = self.parser.get_dados_completos()
        self.assertEqual(dados["titulo"], "Uma Abordagem para Testes de Software Baseados em Inteligência Artificial")
        gerar_pdf("test_extracao_e_formatacao.pdf", dados)
        print("\nIT-01: Extração e formatação dos dados:", dados)
    
    def test_geracao_pdf(self):
        dados = self.parser.get_dados_completos()
        gerar_pdf("it2_teste_geracao.pdf", dados)
        print("\nIT-02: Geração do PDF 'it2_test_geracao.pdf' - Existência:", os.path.exists("it2_test_geracao.pdf"))
    
    def test_integracao_sem_titulo(self):
        parser_sem_titulo = Parser("xml_sem_titulo.xml")
        dados = parser_sem_titulo.get_dados_completos()
        self.assertIsNone(dados["titulo"])
        gerar_pdf("it3_test_integracao_sem_titulo.pdf", dados)
        print("\nIT-03: Integração sem título:", dados)
    
    def test_artigo_sem_autores(self):
        parser_sem_autores = Parser("xml_sem_autores.xml")
        dados = parser_sem_autores.get_dados_completos()
        self.assertEqual(dados["autores"], [])
        gerar_pdf("it4_test_artigo_sem_autores.pdf", dados)
        print("\nIT-04: Artigo sem autores:", dados)
    
    def test_artigo_sem_resumo(self):
        parser_sem_resumo = Parser("xml_sem_resumo.xml")
        dados = parser_sem_resumo.get_dados_completos()
        self.assertEqual(dados["resumo"], "")
        gerar_pdf("it5_test_artigo_sem_resumo.pdf", dados)
        print("\nIT-05: Artigo sem resumo:", dados)
    
    def test_artigo_referencias_incompletas(self):
        parser_referencias = Parser("xml_referencias_incompletas.xml")
        dados = parser_referencias.get_dados_completos()
        gerar_pdf("it6_test_artigo_referencias_incompletas.pdf", dados)
        print("\nIT-06: Artigo com referências incompletas:", dados)
    
    def test_artigo_titulo_longo(self):
        parser_titulo_longo = Parser("xml_titulo_longo.xml")
        dados = parser_titulo_longo.get_dados_completos()
        gerar_pdf("it7_test_artigo_titulo_longo.pdf", dados)
        print("\nIT-07: Artigo com título longo:", dados)
    
    def test_artigo_resumo_longo(self):
        parser_resumo_longo = Parser("xml_resumo_longo.xml")
        dados = parser_resumo_longo.get_dados_completos()
        gerar_pdf("it8_test_artigo_resumo_longo.pdf", dados)
        print("\nIT-08: Artigo com resumo longo:", dados)
    
    def test_integracao_multiplos_autores(self):
        parser_multiautores = Parser("xml_multiautores.xml")
        dados = parser_multiautores.get_dados_completos()
        gerar_pdf("it9_test_artigo_multiplos_autores.pdf", dados)
        print("\nIT-09: Integração com múltiplos autores:", dados)
    
    def test_artigo_sem_secoes(self):
        parser_sem_secoes = Parser("xml_secao_vazia.xml")
        dados = parser_sem_secoes.get_dados_completos()
        gerar_pdf("it10_test_artigo_sem_secoes.pdf", dados)
        print("\nIT-10: Artigo sem seções:", dados)
    
    def test_integracao_sem_referencias(self):
        parser_sem_ref = Parser("xml_sem_referencias.xml")
        dados = parser_sem_ref.get_dados_completos()
        gerar_pdf("it11_test_artigo_sem_referencias.pdf", dados)
        print("\nIT-11: Integração sem referências:", dados)
    
    def test_integracao_multiplos_arquivos(self):
        arquivos = ["artigo.xml", "xml_titulo_longo.xml", "xml_sem_referencias.xml"]
        for arquivo in arquivos:
            parser = Parser(arquivo)
            dados = parser.get_dados_completos()
            pdf_name = f"teste_{arquivo}.pdf"
            gerar_pdf(pdf_name, dados)
            print(f"\nIT-12: Arquivo '{pdf_name}' gerado com sucesso!")

if __name__ == "__main__":
    unittest.main()
