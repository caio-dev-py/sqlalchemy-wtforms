# Projeto SQLAlchemy + Flask-WTF

Este é um projeto Flask que utiliza **Flask-WTF** para formulários seguros e validados, **Flask-SQLAlchemy** para ORM (mapeamento objeto-relacional) e outras extensões úteis como **Flask-Mail** e **Python-Dotenv**.

## 📦 Estrutura do Projeto
```
projeto-sqlalchemy-wtf/
├── src/
│ └── projeto_sqlalchemy_wtf/
│ ├── init.py
│ ├── models.py
│ ├── forms.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── home.py
│ │ └── form_user.py
│ ├── templates/
│ └── static/
├── .env
├── pyproject.toml
├── README.md
└── database.db
```

## 🚀 Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
- [Python-Dotenv](https://github.com/theskumar/python-dotenv)
- [Email Validator](https://pypi.org/project/email-validator/)

# 🛠️ Instalação e Execução
## ✅ Pré-requisitos

- Python 3.13 ou superior
- Poetry instalado

## Clonar o repositório
git clone https://github.com/seu-usuario/projeto-sqlalchemy-wtf.git
cd projeto-sqlalchemy-wtf

## Criar o ambiente e instalar as dependências
poetry install

## Criar o arquivo .env
Crie um arquivo .env na raiz do projeto com as dependências necessárias:
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha

## Rodar o projeto

poetry run flask --app src/projeto_sqlalchemy_wtf/main.py run
**Certifique-se de que main.py está configurado corretamente como ponto de entrada e dentro da estrutura src/.**
✅ Funcionalidades
Cadastro de usuários com validação de e-mail

Banco de dados com SQLAlchemy

Formulários protegidos com CSRF

Envio de e-mail após cadastro (opcional)

Integração com Bootstrap 5

📌 Observações
O projeto utiliza Blueprints para separar as rotas e manter a aplicação organizada.

Bootstrap pode ser incluído via CDN nos arquivos HTML da pasta templates.

📄 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Caio Araujo 🚀 