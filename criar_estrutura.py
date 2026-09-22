from pathlib import Path

arquivos = [
    ".env",
    ".gitignore",
    "app/_init_.py",
    "app/main.py",
    "app/config.py",
    "app/database.py",
    "app/models/_init_.py",
    "app/models/projeto.py",
    "app/repositories/_init_.py",
    "app/repositories/projeto_repository.py",
    "app/schemas/_init_.py",
    "app/schemas/projeto_schema.py",
    "app/services/_init_.py",
    "app/services/projeto_service.py",
    "app/routers/_init_.py",
    "app/routers/projeto_router.py",
    "app/exceptions/_init_.py",
    "app/exceptions/erros.py",
    "app/exceptions/handlers.py",
]

for caminho in arquivos:
    arquivo = Path(caminho)
    arquivo.parent.mkdir(parents=True, exist_ok=True)  # cria as pastas
    arquivo.touch(exist_ok=True)                        # cria o arquivo vazio
    print("criado:", caminho)