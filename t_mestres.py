import unittest
import os
from parser_init import Parser, gerar_pdf

class TestMestre(unittest.TestCase):
    """Testes Mestre"""
    
    def setUp(self):
        self.parser = Parser("artigo.xml")
    
    def test_geracao_pdf_completo(self):
        dados = self.parser.get_dados_completos()
        gerar_pdf("tm1_teste_artigo_completo.pdf", dados)
        resultado = os.path.exists("artigo_completo.pdf")
        self.assertTrue(resultado)
        print("\nTM-01: Geração do PDF completo - 'artigo_completo.pdf' existe:", resultado)
    
    def test_fluxo_xml_corrompido(self):
        self.parser = Parser("xml_malformado.xml")
        print("\nTM-02: Fluxo com XML corrompido testado (Parser instanciado com 'xml_corrompido.xml')")
    
    def test_processamento_artigo_sem_referencias(self):
        parser_sem_ref = Parser("xml_sem_referencias.xml")
        dados = parser_sem_ref.get_dados_completos()
        gerar_pdf("tm3_teste_sem_referencias.pdf", dados)
        resultado = os.path.exists("teste_sem_referencias.pdf")
        self.assertTrue(resultado)
        print("\nTM-03: Processamento de artigo sem referências - 'teste_sem_referencias.pdf' existe:", resultado)
    
    def test_artigo_secao_vazia(self):
        parser_secao_vazia = Parser("xml_secao_vazia.xml")
        dados = parser_secao_vazia.get_dados_completos()
        self.assertTrue("" in dados["secoes"][0][1])
        gerar_pdf("tm4_test_artigo_secao_vazia.pdf", dados)
        print("\nTM-04: Artigo com seção vazia - Seções:", dados["secoes"])
    
    def test_artigo_sem_autores(self):
        parser_sem_autores = Parser("xml_sem_autores.xml")
        dados = parser_sem_autores.get_dados_completos()
        self.assertEqual(dados["autores"], [])
        gerar_pdf("tm5_test_artigo_sem_autores.pdf", dados)
        print("\nTM-05: Artigo sem autores - Autores:", dados["autores"])
    
    def test_integracao_multiplos_arquivos(self):
        arquivos = ["artigo.xml", "xml_titulo_longo.xml", "xml_sem_referencias.xml"]
        for arquivo in arquivos:
            parser = Parser(arquivo)
            dados = parser.get_dados_completos()
            pdf_name = f"tm6_teste_{arquivo}.pdf"
            gerar_pdf(pdf_name, dados)
            resultado = os.path.exists(pdf_name)
            self.assertTrue(resultado)
            print(f"\nTM-06: Arquivo '{pdf_name}' gerado com sucesso - Existência:", resultado)

if __name__ == "__main__":
    unittest.main()
