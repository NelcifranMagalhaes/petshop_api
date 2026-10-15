import app.models
from fastapi import FastAPI

from app.routers.product_route import router as product_router

app = FastAPI(title="PetshopFood API")

app.include_router(product_router)