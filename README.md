
# Search System

A Django-based document search system scaffold for ingesting documents, OCR processing, metadata extraction, embeddings, retrieval, APIs, and chatbot-style interaction.

The project is currently in an early scaffold state. The Django project, installed apps, settings, dependency list, and directory layout are present; domain models, views, templates, static assets, and API routes are still placeholders.

## Tech Stack

- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL via `psycopg`
- Optional SQLite fallback for local development
- OCR and document processing: `pytesseract`, `pdf2image`, `PyMuPDF`, `Pillow`
- Search and NLP: `sentence-transformers`, `faiss-cpu`, `spacy`, `rank-bm25`, `scikit-learn`
- Data utilities: `numpy`, `pandas`

## Project Structure

```text
.
├── accounts/              # User/account app scaffold
├── api/                   # API app scaffold
├── chatbot/               # Chatbot interface app scaffold
├── core/                  # Shared project package
├── documents/             # Document management app scaffold
├── embeddings/            # Embedding generation/indexing app scaffold
├── metadata_extraction/   # Metadata extraction app scaffold
├── ocr/                   # OCR app scaffold
├── retrieval/             # Retrieval/search app scaffold
├── search_system/         # Django project settings, URLs, ASGI/WSGI
├── services/              # Shared service layer package
├── static/                # Project static assets
├── templates/             # Project templates
├── logs/                  # Application logs
├── manage.py
└── requirements.txt
```

## Current Routes

Only the Django admin route is currently configured:

```text
/admin/
```

App-level URL files and public/API routes still need to be added.


## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If using PostgreSQL, create the database first:

```sql
CREATE DATABASE search_system;
```

Then run migrations:

```powershell
python manage.py migrate
```

Create an admin user:

```powershell
python manage.py createsuperuser
```

Start the development server:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

## OCR Dependencies

OCR features will require system-level installations in addition to Python packages:

- Tesseract OCR
- Poppler, for PDF image conversion through `pdf2image`

Configure their executable paths through `TESSERACT_PATH` and `POPPLER_PATH` if they are not available on the system `PATH`.

## Development Notes

- `INSTALLED_APPS` includes `accounts`, `documents`, `ocr`, `metadata_extraction`, `embeddings`, `retrieval`, `api`, and `chatbot`.
- REST Framework defaults to authenticated access using session authentication.
- Logs are written to `logs/app.log` and the console.
- Static files are served from `static/` during development and collected into `staticfiles/`.
- Media uploads are configured to use `media/`, though the folder is not currently present in the repository.

## Suggested Next Steps

1. Add `.gitignore` entries for `venv/`, `__pycache__/`, `.env`, `logs/*.log`, `db.sqlite3`, `media/`, `staticfiles/`, and generated FAISS indexes.
2. Define core document models and migrations.
3. Add upload, OCR, metadata extraction, embedding, retrieval, and chatbot workflows.
4. Add app-level `urls.py` files and include them from `search_system/urls.py`.
5. Add tests around each processing stage as behavior is implemented.
=======
# AI-Driven-Knowledge-Extraction-and-Semantic-Search-for-Documents
This project is a Django-based semantic search platform for RCMS &amp; PVS Housedocuments. The system will allow users to upload documentss, extract text through OCR, store page-level content, generate chunks and metadata, create semantic embeddings, index them with FAISS, and search relevant passages through a web UI and API.

