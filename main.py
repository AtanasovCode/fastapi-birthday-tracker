from fastapi import FastAPI
from contextlib import asynccontextmanager
from web.person_router import router as person_api_router
from database.seed import seed
from database.database import engine
from model.models import Base



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(person_api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

