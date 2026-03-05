
# Metadata Lineage Service

A backend service built with **FastAPI** to manage  **dataset metadata and lineage relationships** .

This service allows users to register datasets, track lineage between datasets, and search dataset metadata.
The application is containerized using **Docker** and uses **MySQL** as the database.

---

# Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy
* Alembic
* MySQL
* Docker / Docker Compose
* Poetry

---

# Features

* Register datasets with metadata
* Track lineage between datasets
* Search datasets by table name
* Database schema management using Alembic migrations
* Environment-based configuration using `.env`
* Containerized deployment using Docker

---

# Environment Variables

Create a `.env` file in the project root:

```
DB_USER=root
DB_PASSWORD=root
DB_HOST=db
DB_PORT=3306
DB_NAME=metadata
```

---

# Running the Project with Docker

Build and start the services:

```
docker compose up --build
```

This starts the FastAPI service and MySQL database.

---

# Run Database Migrations

After the containers are running, execute migrations:

```
docker exec -it metadata_api alembic upgrade head
```

This will create the required database tables.

---

# API Documentation

Once the application is running, open:

```
http://localhost:8000/docs
```

Swagger UI provides interactive API documentation for testing the endpoints.

---

# Running Locally (Without Docker)

Install dependencies:

```
poetry install
```

Run the application:

```
poetry run uvicorn app.main:app --reload
```

Run migrations:

```
poetry run alembic upgrade head
```
