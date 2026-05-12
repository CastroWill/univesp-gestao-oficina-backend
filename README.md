# 🚗 Sistema de Gestão para Oficina Mecânica

Sistema web desenvolvido para auxiliar no gerenciamento de atendimentos de uma oficina mecânica de bairro, permitindo o agendamento online de diagnósticos iniciais e o acompanhamento administrativo dos atendimentos.

O projeto foi desenvolvido como parte das atividades da graduação em **Engenharia da Computação (UNIVESP)**.

---

## 📌 Objetivo do Projeto

O objetivo do sistema é facilitar o processo de agendamento de clientes para diagnósticos automotivos, reduzindo a necessidade de contato manual e organizando a agenda do mecânico de forma simples e intuitiva.

O cliente pode visualizar horários disponíveis e realizar um agendamento online, enquanto o mecânico possui um painel administrativo para gerenciamento dos atendimentos.

---

## ✨ Funcionalidades

### 👤 Área do Cliente

- Página inicial com apresentação da oficina
- Informações de contato
- Link de localização da oficina
- Agendamento online de atendimento
- Consulta automática de horários disponíveis
- Formulário com informações do cliente e do veículo

### 🔧 Área Administrativa

- Dashboard com indicadores de atendimento
- Visualização de todos os agendamentos
- Busca por cliente, telefone ou e-mail
- Filtro por status
- Atualização do status do atendimento:
  - Pendente
  - Confirmado
  - Concluído
  - Cancelado

### ⚙️ Regras de Negócio

- Não permite conflito de horários
- Horários ocupados deixam de aparecer
- Agenda dinâmica baseada na disponibilidade real
- Atualização em tempo real do painel administrativo

---

## 🏗️ Arquitetura do Projeto

O sistema foi desenvolvido utilizando arquitetura desacoplada entre **Front-end** e **Back-end**, consumindo uma API REST.

```text
Cliente (Frontend)
        ↓
API REST (FastAPI)
        ↓
Banco de Dados PostgreSQL
```

---

## 🧰 Tecnologias Utilizadas

### Front-end
- HTML5
- CSS3
- Bootstrap 5
- JavaScript Vanilla

### Back-end
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Banco de Dados
- PostgreSQL

### Deploy
- Vercel (Front-end)
- Render (Back-end + Banco)

### Versionamento
- Git
- GitHub

---

## 📁 Estrutura do Projeto

```text
univesp-gestao-oficina/
│
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── services/
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── agendar.html
│   └── admin.html
│
└── README.md
```

---

## 🔌 API REST

### Criar Agendamento

```http
POST /agendamentos
```

### Consultar Horários Disponíveis

```http
GET /horarios-disponiveis?data=YYYY-MM-DD
```

### Listar Agendamentos

```http
GET /agendamentos
```

### Atualizar Status

```http
PATCH /agendamentos/{id}/status
```

### Dashboard Administrativo

```http
GET /dashboard
```

---

## 🚀 Como Executar Localmente

### 1. Clonar repositório

```bash
git clone https://github.com/SEU-USUARIO/univesp-gestao-oficina.git
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

Linux / Mac / Codespaces

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 4. Instalar dependências

```bash
pip install -r backend/requirements.txt
```

### 5. Configurar variáveis de ambiente

Criar arquivo:

```env
backend/.env
```

Com:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/oficina_db
```

### 6. Executar API

```bash
cd backend
uvicorn app.main:app --reload
```

### 7. Executar Front-end

```bash
cd frontend
python -m http.server 5500
```

---

## 🌐 Deploy

### Front-end
Hospedado na **Vercel**

### Back-end
Hospedado na **Render**

### Banco de Dados
**PostgreSQL Render**

---

## 📖 Melhorias Futuras

- Sistema de login para administrador
- Notificações automáticas
- Histórico de atendimentos
- Cadastro completo de clientes
- Cadastro completo de veículos
- Upload de imagens do veículo
- Responsividade avançada

---

## 👨‍💻 Grupo

**Arthur Bispo**
**Thais Edwiges**
**Pietra Lopes**
**Renato Elvira**
**Adriano Macedo**
**Willam Castro**

Projeto acadêmico – Engenharia da Computação | UNIVESP

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.
