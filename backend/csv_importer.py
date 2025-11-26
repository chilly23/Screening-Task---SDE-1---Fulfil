import time
import csv
from fastapi import UploadFile
from sqlalchemy.orm import Session
from models import Product
from utils.progress_store import set_progress

def process_csv(job_id: str, file: UploadFile, db: Session):
    contents = file.file.read().decode().splitlines()
    reader = csv.DictReader(contents)

    total = sum(1 for _ in contents) - 1  # minus header
    processed = 0

    for row in reader:
        sku = row.get("sku")
        name = row.get("name")
        price = float(row.get("price", 0))
        stock = int(row.get("stock", 0))

        existing = db.query(Product).filter(Product.sku == sku).first()
        if existing:
            existing.name = name
            existing.price = price
            existing.stock = stock
        else:
            db.add(Product(sku=sku, name=name, price=price, stock=stock))

        db.commit()

        processed += 1
        percent = int((processed / total) * 100)
        set_progress(job_id, percent)

        time.sleep(0.03)  # simulate work

    set_progress(job_id, 100)
