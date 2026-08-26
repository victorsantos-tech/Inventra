[1mdiff --git a/criar_admin.py b/criar_admin.py[m
[1mindex 3508d6c..4e48da9 100644[m
[1m--- a/criar_admin.py[m
[1m+++ b/criar_admin.py[m
[36m@@ -2,56 +2,43 @@[m [mfrom werkzeug.security import generate_password_hash[m
 [m
 from app import app[m
 from database import db[m
[31m-[m
 from models.usuario import Usuario[m
 [m
 [m
[31m-with app.app_context():[m
[32m+[m[32mDEMO_EMAIL = "demo@inventra.local"[m
[32m+[m[32mDEMO_PASSWORD = "inventra-demo"[m
 [m
[31m-    email_demo = "demo@boschflow.com"[m
 [m
[32m+[m[32mwith app.app_context():[m
 [m
     usuario = Usuario.query.filter_by([m
[31m-        email=email_demo[m
[32m+[m[32m        email=DEMO_EMAIL[m
     ).first()[m
 [m
[31m-[m
     if usuario:[m
 [m
         print("=" * 40)[m
         print("Usuário demo já existe!")[m
         print("=" * 40)[m
[31m-        print("Email: demo@boschflow.com")[m
[31m-        print("Senha: boschflow123")[m
[32m+[m[32m        print(f"Email: {DEMO_EMAIL}")[m
[32m+[m[32m        print(f"Senha: {DEMO_PASSWORD}")[m
         print("=" * 40)[m
 [m
[31m-[m
     else:[m
 [m
[31m-[m
         demo = Usuario([m
[31m-[m
             nome="Usuário Demonstração",[m
[31m-[m
[31m-            email=email_demo,[m
[31m-[m
[31m-            senha=generate_password_hash([m
[31m-                "boschflow123"[m
[31m-            ),[m
[31m-[m
[32m+[m[32m            email=DEMO_EMAIL,[m
[32m+[m[32m            senha=generate_password_hash(DEMO_PASSWORD),[m
             perfil="ADMIN"[m
[31m-[m
         )[m
 [m
[31m-[m
         db.session.add(demo)[m
[31m-[m
         db.session.commit()[m
 [m
[31m-[m
         print("=" * 40)[m
         print("Usuário demo criado com sucesso!")[m
         print("=" * 40)[m
[31m-        print("Email: demo@boschflow.com")[m
[31m-        print("Senha: boschflow123")[m
[32m+[m[32m        print(f"Email: {DEMO_EMAIL}")[m
[32m+[m[32m        print(f"Senha: {DEMO_PASSWORD}")[m
         print("=" * 40)[m
\ No newline at end of file[m
