import app.models
from fastapi import FastAPI

from app.routers.product_route import router as product_router
from app.routers.customer_route import router as customer_router
from app.routers.sale_route import router as sale_router

app = FastAPI(title="PetshopFood API")

app.include_router(product_router)
app.include_router(customer_router)
app.include_router(sale_router)