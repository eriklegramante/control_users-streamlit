
# 🚀 Streamlit CRUD – User Management System

Projeto completo de **CRUD com autenticação, controle de permissões e painel administrativo**, desenvolvido em **Python + Streamlit + SQLite**.

Este projeto foi criado com foco em **aprendizado prático** e boas práticas.

---

## 📌 Funcionalidades

### 👤 Autenticação
- Registro de usuários
- Login com email e senha
- Senhas protegidas com hash (SHA-256)
- Controle de sessão com `st.session_state`

### 🧑‍💼 Controle de Acesso
- Usuários comuns (`user`)
- Administradores (`admin`)
- Rotas protegidas
- Admin não pode ser removido

### 🛠️ Painel Administrativo
- Listar usuários
- Criar novos usuários
- Editar nome, email e role
- Deletar usuários (exceto admin)

### 📊 Dashboard
- Métricas gerais
- Gráficos simples
- Ações rápidas
- Interface amigável

---

## 🗂️ Estrutura do Projeto

```
crud/
├── db/
│   └── database.py
├── pages/
│   ├── login.py
│   ├── register.py
│   ├── dashboard.py
│   └── admin_users.py
├── scripts/
│   └── session.py
├── utils/
│   └── security.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- SQLite3
- Pandas

---

## 📦 Instalação Local

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd crud
```

### 2️⃣ Crie o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o projeto
```bash
streamlit run main.py
```

---

## 🔐 Usuário Admin Padrão

O sistema cria automaticamente um admin se não existir:

```
Email: admin@admin.com
Senha: admin123
```

⚠️ **Altere a senha após o primeiro login.**

---

## 🚫 O que NÃO sobe para o repositório

- `venv/`
- Arquivo `.db`
- `.streamlit/secrets.toml`
- Arquivos de cache

Tudo isso já está coberto no `.gitignore`.

---

## 🧠 Aprendizados do Projeto

- Arquitetura básica de autenticação
- Controle de permissões
- CRUD completo
- Gerenciamento de estado no Streamlit
- Separação de responsabilidades
- Deploy de aplicações Python

---

## 📌 Próximos Passos (Evolução)
- Reset de senha
- Logs de auditoria
- Soft delete
- PostgreSQL
- Autenticação persistente
- UI/UX avançado

---

## 👨‍💻 Autor

Projeto desenvolvido para fins educacionais e portfólio.

