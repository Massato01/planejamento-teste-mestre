# CÓDIGO PARASER: V1
# import xml.etree.ElementTree as ET
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from textwrap import wrap

# class Parser:
#     def __init__(self, arquivo_xml):
#         """Inicializa o parser e carrega o XML"""
#         self.tree = ET.parse(arquivo_xml)
#         self.root = self.tree.getroot()

#     def get_titulo(self):
#         """Retorna o título do artigo"""
#         return self.root.find(".//article-title").text

#     def get_autores(self):
#         """Retorna a lista de autores do artigo"""
#         autores = []
#         for autor in self.root.findall(".//contrib[@contrib-type='author']"):
#             nome = autor.find(".//given-names").text
#             sobrenome = autor.find(".//surname").text
#             autores.append(f"{nome} {sobrenome}")
#         return autores

#     def get_resumo(self):
#         """Retorna o resumo do artigo"""
#         return self.root.find(".//abstract/p").text

#     def get_secoes(self):
#         """Retorna uma lista de tuplas contendo título e parágrafos das seções"""
#         secoes = []
#         for secao in self.root.findall(".//sec"):
#             titulo_secao = secao.find("title").text
#             paragrafos = [p.text for p in secao.findall("p")]
#             secoes.append((titulo_secao, paragrafos))
#         return secoes

#     def get_referencias(self):
#         """Retorna uma lista de referências formatadas"""
#         referencias = []
#         for ref in self.root.findall(".//ref"):
#             titulo_ref = ref.find(".//article-title")
#             source_ref = ref.find(".//source")
#             ano_ref = ref.find(".//year")

#             titulo_texto = titulo_ref.text if titulo_ref is not None else "Título desconhecido"
#             source_texto = source_ref.text if source_ref is not None else "Fonte desconhecida"
#             ano_texto = ano_ref.text if ano_ref is not None else "Ano desconhecido"

#             referencias.append(f"{titulo_texto}, {source_texto}, {ano_texto}")
#         return referencias

#     def get_dados_completos(self):
#         """Retorna um dicionário agregando todos os elementos extraídos"""
#         return {
#             "titulo": self.get_titulo(),
#             "autores": self.get_autores(),
#             "resumo": self.get_resumo(),
#             "secoes": self.get_secoes(),
#             "referencias": self.get_referencias(),
#         }

# def gerar_pdf(arquivo_pdf, dados):
#     """Gera um PDF estilizado a partir dos dados do artigo, garantindo a quebra de linha adequada"""
#     c = canvas.Canvas(arquivo_pdf, pagesize=letter)
#     width, height = letter
#     line_height = 15  # Altura de cada linha

#     # Título do artigo com quebra de linha
#     c.setFont("Helvetica-Bold", 16)
#     y_position = height - 80
#     for line in wrap(dados["titulo"], width=50):
#         c.drawString(100, y_position, line)
#         y_position -= line_height

#     # Autores
#     c.setFont("Helvetica", 12)
#     c.drawString(100, y_position - 20, "Autores: " + ", ".join(dados["autores"]))
#     y_position -= 40

#     # Resumo
#     c.setFont("Helvetica-Oblique", 12)
#     c.drawString(100, y_position, "Resumo:")
#     c.setFont("Helvetica", 10)
#     y_position -= line_height
#     for line in wrap(dados["resumo"], width=80):
#         c.drawString(100, y_position, line)
#         y_position -= line_height

#     # Adicionar seções do artigo
#     y_position -= 20
#     for secao_titulo, paragrafos in dados["secoes"]:
#         c.setFont("Helvetica-Bold", 12)
#         c.drawString(100, y_position, secao_titulo)
#         y_position -= line_height

#         c.setFont("Helvetica", 10)
#         for paragrafo in paragrafos:
#             for line in wrap(paragrafo, width=80):
#                 c.drawString(100, y_position, line)
#                 y_position -= line_height
#             y_position -= 10

#     # Adicionar referências
#     y_position -= 20
#     c.setFont("Helvetica-Bold", 12)
#     c.drawString(100, y_position, "Referências")
#     c.setFont("Helvetica", 10)
#     y_position -= line_height
#     for referencia in dados["referencias"]:
#         for line in wrap(referencia, width=80):
#             c.drawString(100, y_position, line)
#             y_position -= line_height
#         y_position -= 10

#     c.save()

# # Executar a conversão
# arquivo_xml = "artigo.xml"
# arquivo_pdf = "artigo_formatado.pdf"

# parser = Parser(arquivo_xml)
# dados = parser.get_dados_completos()
# gerar_pdf(arquivo_pdf, dados)

# print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

# CÓDIGO PARASER: V2
import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

class Parser:
    def __init__(self, arquivo_xml):
        """Inicializa o parser e carrega o XML"""
        self.tree = ET.parse(arquivo_xml)
        self.root = self.tree.getroot()

    def get_titulo(self):
        """Retorna o título do artigo"""
        titulo_elem = self.root.find(".//article-title")
        if titulo_elem is not None and titulo_elem.text is not None:
            return titulo_elem.text.strip()
        return None

    def get_autores(self):
        """Retorna a lista de autores do artigo"""
        autores = []
        for autor in self.root.findall(".//contrib[@contrib-type='author']"):
            given = autor.find(".//given-names")
            surname = autor.find(".//surname")
            nome = given.text.strip() if given is not None and given.text is not None else ""
            sobrenome = surname.text.strip() if surname is not None and surname.text is not None else ""
            full_name = f"{nome} {sobrenome}".strip()
            if full_name:
                autores.append(full_name)
        return autores

    def get_resumo(self):
        """Retorna o resumo do artigo"""
        abstract_elem = self.root.find(".//abstract/p")
        if abstract_elem is not None and abstract_elem.text is not None:
            return abstract_elem.text.strip()
        return ""

    def get_secoes(self):
        """Retorna uma lista de tuplas contendo título e parágrafos das seções"""
        secoes = []
        for secao in self.root.findall(".//sec"):
            title_elem = secao.find("title")
            titulo_secao = title_elem.text.strip() if title_elem is not None and title_elem.text is not None else ""
            paragrafos = []
            for p in secao.findall("p"):
                paragrafos.append(p.text.strip() if p.text is not None else "")
            secoes.append((titulo_secao, paragrafos))
        return secoes

    def get_referencias(self):
        """Retorna uma lista de referências formatadas"""
        referencias = []
        for ref in self.root.findall(".//ref"):
            titulo_ref = ref.find(".//article-title")
            source_ref = ref.find(".//source")
            ano_ref = ref.find(".//year")

            titulo_texto = titulo_ref.text.strip() if titulo_ref is not None and titulo_ref.text is not None else "Título desconhecido"
            source_texto = source_ref.text.strip() if source_ref is not None and source_ref.text is not None else "Fonte desconhecida"
            ano_texto = ano_ref.text.strip() if ano_ref is not None and ano_ref.text is not None else "Ano desconhecido"

            referencias.append(f"{titulo_texto}, {source_texto}, {ano_texto}")
        return referencias

    def get_dados_completos(self):
        """Retorna um dicionário agregando todos os elementos extraídos"""
        return {
            "titulo": self.get_titulo(),
            "autores": self.get_autores(),
            "resumo": self.get_resumo(),
            "secoes": self.get_secoes(),
            "referencias": self.get_referencias(),
        }

def gerar_pdf(arquivo_pdf, dados):
    """Gera um PDF estilizado a partir dos dados do artigo, garantindo a quebra de linha adequada"""
    c = canvas.Canvas(arquivo_pdf, pagesize=letter)
    width, height = letter
    line_height = 15  # Altura de cada linha

    # Título do artigo com quebra de linha
    c.setFont("Helvetica-Bold", 16)
    y_position = height - 80
    if dados["titulo"]:
        for line in wrap(dados["titulo"], width=50):
            c.drawString(100, y_position, line)
            y_position -= line_height

    # Autores
    c.setFont("Helvetica", 12)
    if dados["autores"]:
        c.drawString(100, y_position - 20, "Autores: " + ", ".join(dados["autores"]))
    else:
        c.drawString(100, y_position - 20, "Autores: Não informado")
    y_position -= 40

    # Resumo
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(100, y_position, "Resumo:")
    c.setFont("Helvetica", 10)
    y_position -= line_height
    if dados["resumo"]:
        for line in wrap(dados["resumo"], width=80):
            c.drawString(100, y_position, line)
            y_position -= line_height
    else:
        c.drawString(100, y_position, "Resumo não disponível")
        y_position -= line_height

    # Seções do artigo
    y_position -= 20
    if dados["secoes"]:
        for secao_titulo, paragrafos in dados["secoes"]:
            c.setFont("Helvetica-Bold", 12)
            c.drawString(100, y_position, secao_titulo)
            y_position -= line_height

            c.setFont("Helvetica", 10)
            for paragrafo in paragrafos:
                for line in wrap(paragrafo, width=80):
                    c.drawString(100, y_position, line)
                    y_position -= line_height
                y_position -= 10
    else:
        c.drawString(100, y_position, "Sem seções disponíveis")
        y_position -= line_height

    # Referências
    y_position -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_position, "Referências")
    c.setFont("Helvetica", 10)
    y_position -= line_height
    if dados["referencias"]:
        for referencia in dados["referencias"]:
            for line in wrap(referencia, width=80):
                c.drawString(100, y_position, line)
                y_position -= line_height
            y_position -= 10
    else:
        c.drawString(100, y_position, "Sem referências disponíveis")
        y_position -= line_height

    c.save()

# Executar a conversão
arquivo_xml = "artigo.xml"
arquivo_pdf = "artigo_formatado.pdf"

parser = Parser(arquivo_xml)
dados = parser.get_dados_completos()
gerar_pdf(arquivo_pdf, dados)

print(f"PDF '{arquivo_pdf}' gerado com sucesso!")
