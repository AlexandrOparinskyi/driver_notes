from fastapi import FastAPI

from .payments import payment_router

app = FastAPI(title="Driver notes")
app.include_router(payment_router)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Driver notes!"}
