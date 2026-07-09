# AI First CRM – HCP Interaction Logger

An AI-powered CRM application that helps pharmaceutical sales representatives log Healthcare Professional (HCP) interactions using natural language. Instead of manually filling lengthy CRM forms, users can describe an interaction in plain English, and the AI extracts structured information that can be saved to the database.

## Features

- AI-powered interaction logging using natural language
- Structured interaction form automatically populated from AI responses
- Create, Read, Update, and Delete (CRUD) operations for interactions
- RESTful APIs built with FastAPI
- SQLite database using SQLAlchemy ORM
- React + TypeScript frontend
- Redux Toolkit for state management
- LangGraph workflow with AI tool integration
- Interactive API documentation using Swagger UI

---

## Tech Stack

### Frontend

- React
- TypeScript
- Redux Toolkit
- Axios
- CSS

### Backend

- FastAPI
- Python
- SQLAlchemy
- Pydantic
- SQLite
- LangGraph
- LangChain
- Groq API

---

## Project Structure

```
AI First CRM HCP Interaction Logger
│
├── backend
│   ├── app
│   │   ├── database
│   │   ├── langgraph
│   │   ├── models
│   │   ├── prompts
│   │   ├── routers
│   │   ├── services
│   │   ├── tools
│   │   ├── schemas.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── redux
│   │   ├── services
│   │   └── types
│   └── package.json
│
└── README.md
```

---

## How It Works

1. The user describes an HCP interaction in natural language.
2. The request is sent to the FastAPI backend.
3. LangGraph processes the conversation.
4. The AI extracts important interaction details.
5. The extracted data is displayed in the interaction form.
6. The interaction can be saved to the SQLite database.
7. Saved interactions can be viewed, updated, or deleted through the API.

---

## REST API Endpoints

### Chat

| Method | Endpoint | Description                                     |
| ------ | -------- | ----------------------------------------------- |
| POST   | `/chat/` | Process a natural language interaction using AI |

### Interactions

| Method | Endpoint             | Description                |
| ------ | -------------------- | -------------------------- |
| GET    | `/interactions/`     | Get all interactions       |
| GET    | `/interactions/{id}` | Get a specific interaction |
| POST   | `/interactions/`     | Create a new interaction   |
| PUT    | `/interactions/{id}` | Update an interaction      |
| DELETE | `/interactions/{id}` | Delete an interaction      |

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ai-first-crm.git
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## Future Improvements

- Authentication and user management
- AI conversation history
- Search and filtering for interactions
- Dashboard with analytics and reports
- Cloud database support
- Docker deployment

---

## Author

**Ishanvi Deshmukh**

B.Tech CSE (AI & ML)
