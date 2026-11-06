from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated
from pymongo import MongoClient

app = FastAPI()

templates = Jinja2Templates(directory="./")

mongo_client = MongoClient('mongodb://localhost:8000/')

db = mongo_client['Xdb']
collection = db['products']



# HTML 페이지 제공
@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse({"request": request}, "advertise.html")

@app.get("/api/data")
async def get_data():
    return {"message": "FastAPI에서 보내는 데이터입니다"}

products = {
    0: {
        "product_name": "맥북", 
        "details": "무겁고 쓰기 불편하다",
        "tone_and_manner": "과장스럽게"
        }
}

class Product(BaseModel):
    product_name: str
    details: str
    tone_and_manner: str

@app.post("/products")
def create_product(product: Product):
    products = product.model_dunp()
    return {"success": "ok"}






