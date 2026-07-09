from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.database import models

from app.routers.chat import router as chat_router
from app.routers.interactions import router as interaction_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI First CRM",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(interaction_router)


@app.get("/")
def root():
    return {
        "message": "AI First CRM Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }