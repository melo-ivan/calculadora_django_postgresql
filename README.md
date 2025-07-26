# 🧮 Calculadora Django + PostgreSQL

Aplicação web de calculadora com Django e PostgreSQL que realiza operações básicas, registra o histórico por usuário autenticado e aplica boas práticas de organização em projetos web. Ideal para fins educacionais e demonstração de CRUD em Django.

---

## 🚀 Funcionalidades

- Cadastro e login de usuários
- Operações matemáticas: soma, subtração, multiplicação e divisão
- Registro de operações por usuário no banco de dados
- Visualização do histórico de cálculos
- Interface web simples e funcional

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Django 4+
- PostgreSQL
- HTML/CSS (com Bootstrap opcional)
- Gunicorn e Whitenoise (para deploy no Render)

---

## 🧪 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/calculadora_django_postgresql.git
cd calculadora_django_postgresql

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure variáveis de ambiente (pode usar .env)
export DEBUG=1
export SECRET_KEY=sua-chave-secreta
export DATABASE_URL=sqlite:///db.sqlite3

# Migre o banco e rode o servidor
python manage.py migrate
python manage.py runserver

