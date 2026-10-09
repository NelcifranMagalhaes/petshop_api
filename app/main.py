from fastapi import FastAPI
from app.routers import product_route

app = FastAPI()

app.include_router(product_route.router)