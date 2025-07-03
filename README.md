# 🧠 Projeto de Engenharia de Dados - API de Apostas Online

Este projeto demonstra um pipeline simples e eficiente de Engenharia de Dados, com foco em:

- 🔄 Extração de dados em tempo real da [Odds API](https://the-odds-api.com/)
- 🗄️ Armazenamento dos dados em um banco de dados **PostgreSQL hospedado na Render**
- 📊 Visualização dos dados em tempo real com **Streamlit**
- 🔍 Consultas SQL diretamente no PostgreSQL usando Python + Pandas

---

## 🚀 Tecnologias utilizadas

- **Python 3.12**
- **Pandas**
- **Requests**
- **psycopg2-binary**
- **PostgreSQL (Render Cloud DB)**
- **Streamlit**
- **dotenv (.env)**

---

## 🔁 Etapas do projeto

### 1. 🔎 Extração de dados da API
O script `app.py` realiza a coleta dos dados da Odds API, contendo informações como:

- `key`: chave identificadora do mercado
- `group`: categoria (ex: futebol, tênis, etc)
- `active`: se o mercado está ativo
- `has_outrights`: se possui apostas futuras

### 2. ☁️ Armazenamento em nuvem
Os dados coletados são salvos em um banco **PostgreSQL na Render**, com segurança e acessibilidade garantida na nuvem.  
Conexão realizada com `psycopg2` e variáveis seguras em `.env`.

### 3. 📊 Dashboard com Streamlit
Visualização dos dados com interface leve e interativa:

- Tabela com dados atualizados
- Gráficos (a serem adicionados)
- Possibilidade de expansão para filtros e dashboards interativos

---

## 🧱 Estrutura do projeto

api-apostas/
│
├── .env # Variáveis de ambiente (chaves e credenciais)
├── app.py # Script de extração e inserção no banco PostgreSQL
├── streamlit_app.py # Dashboard com Streamlit conectado ao banco na Render
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── .venv/ # Ambiente virtual Python

yaml
Copy
Edit

---

## ⚙️ Variáveis do `.env`

```env
API_KEY=your_api_key
DB_HOST=your_render_host
DB_PORT=5432
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
⚠️ Certifique-se de NUNCA versionar esse arquivo (.env deve estar no .gitignore)

🖥️ Como rodar localmente
bash
Copy
Edit
# 1. Clonar o projeto
git clone https://github.com/macauli10/api-apostas.git
cd api-apostas

# 2. Criar ambiente virtual
python -m venv .venv
source .venv/Scripts/activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar a coleta de dados
python app.py

# 5. Iniciar o dashboard
.venv/Scripts/python.exe -m streamlit run streamlit_app.py