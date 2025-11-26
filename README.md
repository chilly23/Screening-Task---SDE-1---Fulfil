# Fulfil SDE-I Assessment (Scoped Submission)

AUTHORED BY - VELAN E | velane929@gmail.com

This project implements a compact, production-style subset of the assignment using:

**FastAPI · SQLAlchemy · SQLite · Threaded Async Simulation · Minimal Frontend**

The goal is to demonstrate:
- clean system design
- correct modeling
- background job orchestration
- CSV ingestion flow
- simple webhook manager
- UI for importing + monitoring
- clarity, maintainability, and extendability

## Features Included (Scoped)

### ✔ Product API
- CRUD (create + list included)
- SKU uniqueness
- Database persistence via SQLAlchemy

### ✔ CSV Import Pipeline
- Async-simulated background job (thread)
- Upsert by SKU
- Progress tracked per job
- Frontend UI for upload + progress

### ✔ Webhook Manager
- Register webhook URLs
- Trigger test webhook (mock delivery)

### ✔ Frontend (Minimal)
- CSV uploader
- Real-time progress polling
- Product viewer

### ✔ Clean Architecture