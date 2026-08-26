from werkzeug.security import generate_password_hash

from app import app
from database import db
from models.usuario import Usuario


DEMO_EMAIL = "demo@inventra.local"
DEMO_PASSWORD = "inventra-demo"


with app.app_context():
    usuario = Usuario.query.filter_by(email=DEMO_EMAIL).first()

    if usuario:
        print("=" * 40)
        print("Usuário demo já existe!")
        print("=" * 40)
        print(f"Email: {DEMO_EMAIL}")
        print(f"Senha: {DEMO_PASSWORD}")
        print("=" * 40)

    else:
        demo = Usuario(
            nome="Usuário Demonstração",
            email=DEMO_EMAIL,
            senha=generate_password_hash(DEMO_PASSWORD),
            perfil="ADMIN"
        )

        db.session.add(demo)
        db.session.commit()

        print("=" * 40)
        print("Usuário demo criado com sucesso!")
        print("=" * 40)
        print(f"Email: {DEMO_EMAIL}")
        print(f"Senha: {DEMO_PASSWORD}")
        print("=" * 40)