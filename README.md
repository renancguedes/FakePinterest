Projeto web inspirado no Pinterest, desenvolvido com **Flask** para praticar autenticação, upload de imagens e páginas dinâmicas.

> Observação: este projeto é para fins de estudo/portfólio e não possui relação oficial com o Pinterest.

---

## Demo

- **Login/Cadastro**
- **Feed** com os 10 posts mais recentes
- **Perfil** do usuário com upload de fotos

### Screenshots

> Substitua os arquivos abaixo pelas suas imagens.

- **Tela de login**
    - ![Tela de Login](docs/img/login.png)

- **Tela de feed**
    - ![Feed](docs/img/feed.png)

- **Tela de perfil (upload)**
    - ![Perfil](docs/img/perfil.png)

---

## Funcionalidades

- Autenticação de usuário (login/logout)
- Criação de conta com senha criptografada (bcrypt)
- Feed com posts mais recentes
- Página de perfil do usuário
- Upload de imagem e salvamento em `static/fotos_posts`
- Banco de dados SQLite

---

## Tecnologias

- Python + Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Bcrypt
- SQLite
- HTML + CSS

---

## Como rodar localmente (Windows)

### 1) Criar e ativar ambiente virtual

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
```

### 2) Instalar dependências

```powershell
pip install -r requirements.txt
```

### 3) Criar o banco de dados

```powershell
python criar_banco.py
```

Isso cria o arquivo `banco.db` (SQLite) e as tabelas.

### 4) Rodar o servidor

```powershell
python main.py
```

Acesse no navegador:
- `http://127.0.0.1:5000/`

---

## Estrutura do projeto (resumo)

- `main.py`: inicializa e roda o servidor
- `criar_banco.py`: cria as tabelas no SQLite
- `fakepinterest/routes.py`: rotas (login, criar conta, feed, perfil)
- `fakepinterest/models.py`: modelos `Usuario` e `Post`
- `fakepinterest/forms.py`: formulários (WTForms)
- `fakepinterest/static/`: CSS e imagens
- `fakepinterest/templates/`: páginas HTML (Jinja2)

---

## Observações de segurança

- A `SECRET_KEY` está fixa em `fakepinterest/__init__.py` apenas para estudo. Em produção, o ideal é usar variável de ambiente.

---