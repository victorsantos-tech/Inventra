from app import app
from database import db
from models.produtos import Produto


with app.app_context():

    produtos = Produto.query.all()

    atualizados = 0

    for produto in produtos:

        produto.imagem = f"{produto.codigo}.jpg"
        atualizados += 1

        print(
            f"{produto.codigo} - {produto.nome} -> {produto.imagem}"
        )

    db.session.commit()


print("=" * 50)
print("Imagens atualizadas com sucesso!")
print(f"{atualizados} produtos atualizados.")
print("=" * 50)