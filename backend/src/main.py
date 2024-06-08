from fastapi import FastAPI

from backend.src.api.routers import main_router


app = FastAPI()
app.include_router(main_router)


@app.get("/")
async def root():
    return {"Hello": "World"}

