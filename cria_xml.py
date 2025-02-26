import xml.etree.ElementTree as ET

def criar_xml(arquivo, titulo=None, autores=None, resumo=None, secoes=None, referencias=None):
    """Cria arquivos XML para testes"""
    article = ET.Element("article", attrib={"article-type": "research-article", "lang": "pt"})
    front = ET.SubElement(article, "front")
    article_meta = ET.SubElement(front, "article-meta")

    # Título
    if titulo:
        title_group = ET.SubElement(article_meta, "title-group")
        ET.SubElement(title_group, "article-title").text = titulo
    
    # Autores
    contrib_group = ET.SubElement(article_meta, "contrib-group")
    if autores:
        for nome in autores:
            contrib = ET.SubElement(contrib_group, "contrib", attrib={"contrib-type": "author"})
            name = ET.SubElement(contrib, "name")
            ET.SubElement(name, "given-names").text = nome.split()[0]
            ET.SubElement(name, "surname").text = nome.split()[-1]
    
    # Resumo
    if resumo:
        abstract = ET.SubElement(article_meta, "abstract")
        ET.SubElement(abstract, "p").text = resumo
    
    # Corpo (seções)
    body = ET.SubElement(article, "body")
    if secoes:
        for titulo_secao, conteudo in secoes.items():
            sec = ET.SubElement(body, "sec")
            ET.SubElement(sec, "title").text = titulo_secao
            ET.SubElement(sec, "p").text = conteudo
    
    # Referências
    back = ET.SubElement(article, "back")
    ref_list = ET.SubElement(back, "ref-list")
    if referencias:
        for ref in referencias:
            ref_elem = ET.SubElement(ref_list, "ref")
            citation = ET.SubElement(ref_elem, "element-citation", attrib={"publication-type": "journal"})
            ET.SubElement(citation, "article-title").text = ref.get("titulo", "Título desconhecido")
            ET.SubElement(citation, "source").text = ref.get("fonte", "Fonte desconhecida")
            ET.SubElement(citation, "year").text = ref.get("ano", "Ano desconhecido")
    
    # Salvar arquivo XML
    tree = ET.ElementTree(article)
    tree.write(arquivo, encoding="utf-8", xml_declaration=True)

# Criando os arquivos XML necessários
criar_xml("xml_sem_titulo.xml", autores=["João Silva"], resumo="Teste", secoes={"Introdução": "Texto"})
criar_xml("xml_sem_autores.xml", titulo="Teste Sem Autores", resumo="Resumo", secoes={"Metodologia": "Texto"})
criar_xml("xml_referencias_incompletas.xml", titulo="Teste", autores=["Maria Oliveira"], resumo="Resumo", referencias=[{"titulo": None, "fonte": "Revista X", "ano": "2023"}])
criar_xml("xml_titulo_longo.xml", titulo="T" * 150, autores=["Ana Costa"], resumo="Resumo longo")
criar_xml("xml_vazio.xml")
criar_xml("xml_resumo_longo.xml", titulo="Teste", autores=["Carlos Souza"], resumo="R" * 1000)
criar_xml("xml_multiautores.xml", titulo="Teste", autores=["Autor 1", "Autor 2", "Autor 3"], resumo="Resumo")
criar_xml("xml_sem_referencias.xml", titulo="Teste", autores=["Luiz Mendes"], resumo="Resumo", secoes={"Conclusão": "Texto"})
criar_xml("xml_secao_vazia.xml", titulo="Teste", autores=["Isabel Ferreira"], resumo="Resumo", secoes={"Resultados": ""})
criar_xml("xml_corrompido.xml")
