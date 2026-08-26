[1mdiff --git a/config.py b/config.py[m
[1mindex 4a185a4..d199b0d 100644[m
[1m--- a/config.py[m
[1m+++ b/config.py[m
[36m@@ -9,10 +9,10 @@[m [mos.makedirs(INSTANCE_DIR, exist_ok=True)[m
 [m
 class Config:[m
 [m
[31m-    SECRET_KEY = "boschflow-2026"[m
[32m+[m[32m    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")[m
 [m
     SQLALCHEMY_DATABASE_URI = ([m
[31m-        f"sqlite:///{os.path.join(INSTANCE_DIR, 'boschflow.db')}"[m
[32m+[m[32m        f"sqlite:///{os.path.join(INSTANCE_DIR, 'inventra.db')}"[m
     )[m
 [m
     SQLALCHEMY_TRACK_MODIFICATIONS = False[m
\ No newline at end of file[m
