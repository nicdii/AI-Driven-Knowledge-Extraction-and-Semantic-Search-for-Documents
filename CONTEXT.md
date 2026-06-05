# Codebase Context

## Snapshot

This repository is a Django project named `search_system`. It is intended to become a document search and retrieval platform with OCR, metadata extraction, embedding generation, API access, and chatbot interaction.

As of this context file, the codebase is mostly scaffolded. The project settings and app directories exist, but models, views, tests, templates, static assets, and app routes are placeholders.

## Runtime

- Main entrypoint: `manage.py`
- Django settings module: `search_system.settings`
- Root URL config: `search_system.urls`
- WSGI app: `search_system.wsgi.application`
- ASGI app: `search_system.asgi.application`

## Installed Apps

Local apps configured in `INSTALLED_APPS`:

- `accounts`: user/account functionality placeholder
- `documents`: document management placeholder
- `ocr`: OCR processing placeholder
- `metadata_extraction`: metadata extraction placeholder
- `embeddings`: embedding generation/indexing placeholder
- `retrieval`: search/retrieval placeholder
- `api`: REST API placeholder
- `chatbot`: chatbot interface placeholder

Third-party app:

- `rest_framework`

## URL Surface

`search_system/urls.py` currently registers only:

```python
path("admin/", admin.site.urls)
```

No app-level URL modules are currently included.

## Database Configuration

Database behavior is controlled by `.env`:

- `USE_SQLITE_FALLBACK=True` uses local SQLite at `BASE_DIR / "db.sqlite3"`.
- `USE_SQLITE_FALLBACK=False` uses PostgreSQL.

PostgreSQL environment variables:

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

Default PostgreSQL database name is `search_system`.

## Settings Highlights

- `DEBUG` defaults to `True`.
- `ALLOWED_HOSTS` defaults to `127.0.0.1,localhost`.
- `TIME_ZONE` is `Asia/Kolkata`.
- `LOGIN_URL` is `accounts:login`, but no matching account URLs/views exist yet.
- `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` both point to `/`.
- REST Framework defaults:
  - Permission: `IsAuthenticated`
  - Authentication: `SessionAuthentication`
- Static files:
  - `STATIC_URL = "/static/"`
  - `STATICFILES_DIRS = [BASE_DIR / "static"]`
  - `STATIC_ROOT = BASE_DIR / "staticfiles"`
- Media files:
  - `MEDIA_URL = "/media/"`
  - `MEDIA_ROOT = BASE_DIR / "media"`
- Logging:
  - Root logger writes INFO logs to console and `logs/app.log`.

## OCR Configuration

OCR-related settings:

- `TESSERACT_PATH`
- `POPPLER_PATH`
- `OCR_LANGUAGE`, defaulting to `eng+pan`

Expected external dependencies:

- Tesseract OCR
- Poppler

## Dependencies

Important Python packages from `requirements.txt`:

- Django and DRF: `Django`, `djangorestframework`
- Database: `psycopg[binary]`
- Environment: `python-dotenv`
- Embeddings/vector search: `sentence-transformers`, `faiss-cpu`, `torch`
- NLP/search: `spacy`, `rank-bm25`, `scikit-learn`
- OCR/document parsing: `pytesseract`, `pdf2image`, `PyMuPDF`, `Pillow`
- Data: `numpy`, `pandas`

## Current Implementation State

- All app `models.py` files currently contain only Django's default placeholder comment.
- App `views.py` files currently contain only Django's default placeholder import/comment.
- Admin modules are scaffolded but do not register custom models.
- Migration packages exist, but no initial model migrations are present.
- `templates/` and `static/` exist but are empty.
- `services/` and `core/` exist as Python packages for shared logic, but contain no implementation yet.

## Git/Workspace Notes

The repository currently appears untracked from Git's perspective. Generated/local folders such as `venv/`, `__pycache__/`, `staticfiles/`, `.env`, and logs are present in the workspace and should normally be ignored before the first commit.

Suggested ignore patterns:

```gitignore
.env
venv/
__pycache__/
*.py[cod]
db.sqlite3
logs/*.log
media/
staticfiles/
faiss_index/
```

## Likely Development Flow

1. Create persistent models in `documents`, then add migrations.
2. Implement upload and file storage handling.
3. Add OCR services in `ocr` or `services`.
4. Extract metadata into `metadata_extraction`.
5. Generate embeddings in `embeddings` and persist/index them.
6. Implement BM25/vector/hybrid retrieval in `retrieval`.
7. Expose workflows through `api`.
8. Add chatbot orchestration in `chatbot`.
9. Wire app URLs into `search_system.urls`.
10. Add templates or frontend endpoints as needed.

## Cautions For Future Agents

- Do not read or print `.env` secret values unless explicitly requested.
- Avoid committing generated directories and local runtime artifacts.
- `LOGIN_URL = "accounts:login"` currently references a route that does not exist.
- DRF endpoints will require authentication by default unless per-view permissions are changed.
- OCR and PDF conversion may fail until Tesseract and Poppler are installed and discoverable.
