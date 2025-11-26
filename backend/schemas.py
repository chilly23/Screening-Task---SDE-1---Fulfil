from pydantic import BaseModel

class ProductCreate(BaseModel):
    sku: str
    name: str
    price: float
    stock: int

class ProductOut(ProductCreate):
    id: int
    class Config:
        orm_mode = True
