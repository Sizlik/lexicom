from fastapi import FastAPI
from src.user.router import router as user_router

app = FastAPI()


app.include_router(user_router)


@app.get("/")
async def health():
    return {"status": "Healthy"}
