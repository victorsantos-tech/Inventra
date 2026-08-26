from app import app
from database import db

from models.categoria import Categoria
from models.fornecedor import Fornecedor
from models.produtos import Produto


with app.app_context():

    # ==========================
    # CATEGORIAS
    # ==========================

    categorias = [
        "Sensores",
        "Automação Industrial",
        "Acionamentos",
        "Motores",
        "Fontes",
        "Identificação"
    ]

    categorias_db = {}

    for nome in categorias:

        categoria = Categoria.query.filter_by(nome=nome).first()

        if not categoria:
            categoria = Categoria(nome=nome)
            db.session.add(categoria)
            db.session.flush()

        categorias_db[nome] = categoria

    # ==========================
    # FORNECEDORES
    # ==========================

    fornecedores = [
        "TechParts",
        "MotionWorks"
    ]

    fornecedores_db = {}

    for nome in fornecedores:

        fornecedor = Fornecedor.query.filter_by(nome=nome).first()

        if not fornecedor:

            fornecedor = Fornecedor(
                nome=nome,
                telefone="(19) 99999-9999",
                email=f"{nome.lower().replace(' ', '')}@inventra.local"
            )

            db.session.add(fornecedor)
            db.session.flush()

        fornecedores_db[nome] = fornecedor

    # ==========================
    # PRODUTOS
    # ==========================

    produtos = [

        ("INV001", "Sensor Indutivo M12", "Sensores", "TechParts", 45, 10, 189.90),
        ("INV002", "Sensor Fotoelétrico", "Sensores", "TechParts", 30, 8, 249.90),
        ("INV003", "Sensor Capacitivo", "Sensores", "TechParts", 18, 5, 229.90),
        ("INV004", "Sensor Ultrassônico", "Sensores", "TechParts", 12, 4, 699.90),
        ("INV005", "Encoder Incremental", "Sensores", "TechParts", 15, 5, 799.90),

        ("INV006", "CLP Industrial Modular", "Automação Industrial", "TechParts", 8, 2, 4590.00),
        ("INV007", "Módulo Entrada Digital", "Automação Industrial", "TechParts", 16, 5, 890.00),
        ("INV008", "Módulo Saída Digital", "Automação Industrial", "TechParts", 14, 5, 930.00),
        ("INV009", "Painel IHM 7 Polegadas", "Automação Industrial", "TechParts", 5, 2, 2890.00),
        ("INV010", "Controlador Industrial", "Automação Industrial", "TechParts", 9, 3, 3990.00),

        ("INV011", "Inversor de Frequência", "Acionamentos", "MotionWorks", 12, 3, 2850.00),
        ("INV012", "Soft Starter", "Acionamentos", "MotionWorks", 10, 3, 1890.00),
        ("INV013", "Drive Servo", "Acionamentos", "MotionWorks", 6, 2, 5990.00),
        ("INV014", "Conversor Industrial", "Acionamentos", "MotionWorks", 8, 3, 3290.00),
        ("INV015", "Controlador de Movimento", "Acionamentos", "MotionWorks", 4, 2, 7590.00),

        ("INV016", "Servo Motor 750W", "Motores", "MotionWorks", 7, 2, 6990.00),
        ("INV017", "Motor Trifásico", "Motores", "MotionWorks", 18, 5, 2590.00),
        ("INV018", "Motor Brushless", "Motores", "MotionWorks", 9, 3, 4990.00),
        ("INV019", "Motor Linear", "Motores", "MotionWorks", 3, 1, 11990.00),
        ("INV020", "Redutor Industrial", "Motores", "MotionWorks", 5, 2, 3890.00),

        ("INV021", "Fonte 24V 5A", "Fontes", "TechParts", 28, 5, 329.90),
        ("INV022", "Fonte 24V 10A", "Fontes", "TechParts", 19, 5, 489.90),
        ("INV023", "UPS Industrial", "Fontes", "TechParts", 6, 2, 1890.00),
        ("INV024", "Fonte Modular", "Fontes", "TechParts", 14, 4, 659.90),
        ("INV025", "Transformador Industrial", "Fontes", "TechParts", 10, 3, 1290.00),

        ("INV026", "Leitor RFID", "Identificação", "TechParts", 9, 2, 1590.00),
        ("INV027", "Tag RFID Industrial", "Identificação", "TechParts", 120, 20, 35.90),
        ("INV028", "Scanner Código de Barras", "Identificação", "TechParts", 11, 3, 890.00),
        ("INV029", "Impressora de Etiquetas", "Identificação", "TechParts", 5, 2, 1990.00),
        ("INV030", "Terminal Coletor de Dados", "Identificação", "TechParts", 8, 2, 3290.00),

    ]

    adicionados = 0

    for codigo, nome, categoria, fornecedor, quantidade, minimo, preco in produtos:

        existe = Produto.query.filter_by(codigo=codigo).first()

        if existe:
            continue

        produto = Produto(
            codigo=codigo,
            nome=nome,
            descricao=f"{nome} utilizado em ambiente industrial.",
            preco=preco,
            quantidade=quantidade,
            estoque_minimo=minimo,
            categoria=categorias_db[categoria],
            fornecedor=fornecedores_db[fornecedor]
        )

        db.session.add(produto)
        adicionados += 1

    db.session.commit()

    print("=" * 50)
    print("Banco populado com sucesso!")
    print(f"{adicionados} produtos adicionados.")
    print("=" * 50)