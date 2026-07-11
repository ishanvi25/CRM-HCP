# AI First CRM – Healthcare Professional (HCP) Interaction Logger

An AI-powered Customer Relationship Management (CRM) application that simplifies Healthcare Professional (HCP) interaction logging for pharmaceutical sales representatives.

Instead of manually completing lengthy CRM forms, users can describe their meeting with a doctor or healthcare professional in natural language. Using **LangGraph**, **LangChain**, and **Groq LLM**, the application extracts structured information from the conversation, automatically populates the interaction form, and stores the data in a SQLite database.

This project demonstrates the integration of **Generative AI**, **tool-calling agents**, **FastAPI**, **React**, and **Redux Toolkit** to build an intelligent full-stack CRM application.

---

# Project Overview

Pharmaceutical sales representatives frequently record interactions with doctors after meetings, including:

- Healthcare Professional (HCP) details
- Topics discussed
- Educational materials shared
- Product samples distributed
- Meeting outcomes
- Follow-up actions
- Overall sentiment

Traditionally, this information is entered manually into CRM systems, which is repetitive and time-consuming.

This project automates that process by allowing users to describe the meeting naturally while the AI extracts structured information and fills the CRM form automatically.

---

# Key Features

### AI-Powered Interaction Logging

Users can describe an HCP interaction using plain English. The AI understands the conversation and extracts relevant information into structured CRM fields.

### Automatic Form Population

After processing the conversation, the extracted details automatically populate the interaction form without requiring manual entry.

### LangGraph Agent Workflow

The application uses a LangGraph agent capable of deciding which tool should be executed based on the user's request.

Supported tools include:

- Log Interaction
- Edit Interaction
- Summarize Interaction
- Suggest Follow-up
- Clear Interaction

### CRUD Operations

The application supports complete CRUD functionality:

- Create new interactions
- Retrieve all interactions
- View individual interactions
- Update existing interactions
- Delete interactions

### REST API

A FastAPI backend exposes RESTful endpoints for chat processing and interaction management.

### SQLite Database

Interaction data is persisted using SQLAlchemy ORM with SQLite.

### Interactive API Documentation

Swagger UI is available for testing all backend endpoints.

---

# Tech Stack

## Frontend

- React
- TypeScript
- Redux Toolkit
- Axios
- CSS

## Backend

- FastAPI
- Python
- SQLAlchemy
- Pydantic
- SQLite

## AI & Agent Framework

- LangGraph
- LangChain
- Groq LLM API

---

# Project Architecture

```
                 User
                   │
                   ▼
        React + TypeScript Frontend
                   │
             Axios API Calls
                   │
                   ▼
            FastAPI Backend
                   │
                   ▼
             LangGraph Agent
                   │
         Chooses Appropriate Tool
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
  Log Interaction  Edit   Summarize
        │
        ▼
 SQLite Database (SQLAlchemy)
        │
        ▼
 Updated Interaction Returned
        │
        ▼
 Redux Store Updated
        │
        ▼
 Form Automatically Populated
```

---

# LangGraph Tools

The application uses five AI tools.

## 1. Log Interaction

Extracts structured information from natural language and saves the interaction to the database.

Example:

> "I met Dr. Sharma today to discuss diabetes medication."

The AI extracts:

- HCP Name
- Interaction Type
- Date
- Time
- Topics Discussed
- Materials Shared
- Samples Distributed
- Outcomes
- Follow-up Actions
- Sentiment

---

## 2. Edit Interaction

Allows users to modify existing interaction fields.

Example:

> "Change the sentiment to Neutral."

---

## 3. Summarize Interaction

Generates a concise summary of an interaction.

Example:

> "Summarize today's meeting."

---

## 4. Suggest Follow-up

Provides recommendations for future engagement.

Example:

> "Suggest the next follow-up."

---

## 5. Clear Interaction

Resets the current interaction so a new one can be recorded.

---

# Project Structure

```
AI First CRM HCP Interaction Logger
│
├── backend
│   ├── app
│   │   ├── database
│   │   │   ├── database.py
│   │   │   ├── crud.py
│   │   │   └── models.py
│   │   │
│   │   ├── langgraph
│   │   │   └── graph.py
│   │   │
│   │   ├── prompts
│   │   ├── routers
│   │   ├── services
│   │   ├── tools
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── redux
│   │   ├── services
│   │   ├── types
│   │   └── App.tsx
│   │
│   └── package.json
│
├── README.md
└── .gitignore
```

---

# Application Workflow

1. The user enters an interaction in natural language.
2. The frontend sends the message to the FastAPI backend.
3. LangGraph receives the conversation.
4. The LLM analyzes the user's intent.
5. The appropriate tool is selected automatically.
6. Structured interaction details are extracted.
7. The interaction is stored in SQLite.
8. The backend returns the extracted interaction.
9. Redux updates the application state.
10. The interaction form is automatically populated.

---

# REST API Endpoints

## Chat

| Method | Endpoint | Description                                   |
| ------ | -------- | --------------------------------------------- |
| POST   | `/chat/` | Process natural language interaction using AI |

---

## Interactions

| Method | Endpoint             | Description                |
| ------ | -------------------- | -------------------------- |
| GET    | `/interactions/`     | Retrieve all interactions  |
| GET    | `/interactions/{id}` | Retrieve interaction by ID |
| POST   | `/interactions/`     | Create interaction         |
| PUT    | `/interactions/{id}` | Update interaction         |
| DELETE | `/interactions/{id}` | Delete interaction         |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/ishanvi25/CRM-HCP.git

cd CRM-HCP
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# Future Enhancements

- User authentication and authorization
- Conversation history
- AI-generated meeting insights
- Advanced search and filtering
- Analytics dashboard
- PDF export of interaction reports
- PostgreSQL or MySQL support
- Docker deployment
- Cloud hosting (AWS/Azure/GCP)

---

# Author

**Ishanvi Deshmukh**

B.Tech – Computer Science & Engineering (Artificial Intelligence & Machine Learning)

Lakshmi Narain College of Technology

2022 – 2026

---

## Acknowledgements

This project was developed as part of an AI-powered CRM assignment to demonstrate the practical integration of Large Language Models, LangGraph agents, FastAPI, React, Redux Toolkit, and SQLAlchemy in a real-world healthcare CRM workflow.
