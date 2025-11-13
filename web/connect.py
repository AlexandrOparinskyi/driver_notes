from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .payments import payment_router

app = FastAPI(title="Driver notes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://oparinskyi.ru", "http://oparinskyi.ru"],  # Разрешенные домены
    allow_credentials=True,  # Разрешить cookies
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(payment_router)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Driver notes!"}
