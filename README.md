# SimpleLibraryApp 🐳📚

A Django web application powered by PostgreSQL, containerized using Docker and Docker Compose.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SimpleLibraryApp.git
cd SimpleLibraryApp
```

### 2. Set up environment variables
Create a .env file in the root directory:

# .env
```
# Django DB connection
DATABASE_URL=postgres://{postgres}:{password}@db:{port}/SimpleLibraryAppDB

# PostgreSQL container settings
POSTGRES_DB=SimpleLibraryAppDB
POSTGRES_USER={postgres}
POSTGRES_PASSWORD={password}
```

### 3. Build and run the app
Use Docker Compose to build and start both the Django and PostgreSQL containers:

```
docker-compose up --build
```

Visit http://0.0.0.0:8000 in your browser.

### 4. Apply migrations & create a superuser
In a separate terminal:

```
# Run inside the container
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## 📁 Project Structure
```
SimpleLibraryApp/
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
├── manage.py
├── SimpleLibraryApp/      # Django project settings
└── apis/
└── books/
└── books_and_authors.json
└── Postman Collections/
```