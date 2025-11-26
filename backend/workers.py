import threading
from fastapi import UploadFile
from sqlalchemy.orm import Session
from csv_importer import process_csv

def start_import(job_id: str, file: UploadFile, db: Session):
    t = threading.Thread(target=process_csv, args=(job_id, file, db))
    t.start()
    return {"job_id": job_id, "status": "started"}
