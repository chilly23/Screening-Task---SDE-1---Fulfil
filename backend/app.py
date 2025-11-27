from fastapi import FastAPI, UploadFile, Depends
from sqlalchemy.orm import Session
from backend.workers import start_import
from utils.progress_store import get_progress
from backend.webhook import register_webhook, send_test_webhook
import uuid

from backend.database import Base, engine, SessionLocal
from backend.models import Product
from backend.schemas import ProductCreate, ProductOut
from backend.csv_importer import import_csv


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fulfil Assessment - Scoped Submission")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.post("/products")
def create_product(p: ProductCreate, db: Session = Depends(get_db)):
    prod = Product(**p.dict())
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod

@app.post("/upload-csv")
def upload_csv(file: UploadFile, db: Session = Depends(get_db)):
    job_id = str(uuid.uuid4())
    start_import(job_id, file, db)
    return {"job_id": job_id}

@app.get("/progress/{job_id}")
def progress(job_id: str):
    return {"progress": get_progress(job_id)}

@app.post("/webhook/register")
def wh_register(url: str):
    return register_webhook(url)

@app.post("/webhook/test")
def wh_test(url: str):
    return send_test_webhook(url)
