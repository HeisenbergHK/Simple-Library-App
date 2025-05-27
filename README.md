# SimpleLibraryApp 🐳📚

A Django web application for managing a simple library system.
It supports PostgreSQL as the backend and offers a clean REST API for managing books and authors.

This app can be run locally in a development environment, containerized using Docker and Docker Compose, or deployed on a Kubernetes cluster using Minikube.

This project demonstrates how to build a Django web application from scratch and deploy it using industry best practices—covering local development, Docker-based containerization, and full deployment on Kubernetes with Minikube.

## 🌱 Run the Project Without Docker

### 1. 📦 Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip
- PostgreSQL (or SQLite if you prefer modifying settings)
- (Optional) Virtualenv for isolated environments


### 2. 🔄 Clone the Repository

```bash
git clone https://github.com/HeisenbergHK/Simple-Library-App.git
cd SimpleLibraryApp
```

### 3. 🧪 Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. 📜 Install Dependencies
```
pip install -r requirements.txt
```

### 5. ⚙️ Configure Environment
Create a .env file in the project root directory:
```
# Example for PostgreSQL (update values based on your local setup)
DATABASE_URL=postgres://youruser:yourpassword@localhost:5432/SimpleLibraryAppDB

# Or for SQLite (uncomment if needed)
# DATABASE_URL=sqlite:///db.sqlite3
```

Make sure your settings.py reads from the .env using os.environ.get.

### 6. 🛠 Apply Migrations
```
python manage.py migrate
```

### 7. 👤 Create a Superuser
```
python manage.py createsuperuser
```

### 8. 🚀 Run the Server
```
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser.

## 🐳 Run the Project with Docker

### 1. 📂 Clone the Repository
```
git clone https://github.com/HeisenbergHK/Simple-Library-App.git
cd SimpleLibraryApp
```

### 2. 🛠 Set up Environment Variables
Create a .env file in the root directory:
```
# Django DB connection
DATABASE_URL=postgres://postgres:yourpassword@db:5432/SimpleLibraryAppDB

# PostgreSQL container settings
POSTGRES_DB=SimpleLibraryAppDB
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
```

### 3. 🧱 Build and Start Containers
```
docker-compose up --build
```
Visit http://0.0.0.0:8000 in your browser.

### 4. 🔁 Apply Migrations & Create Superuser
In a separate terminal:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## 🚢 Run the Project with Minikube

### 1. 📦 Prerequisites

Make sure you have the following installed:
- Minikube
- kubectl
- Docker (for building images)

### 2. 🔄 Start Minikube
```
minikube start
```

### 3. 🏗️ Build and Push Docker Image
The Docker image is available on DockerHub as `hassankalantari/simple-library-app:latest`. You can either pull it directly or build it locally:

```
# Point shell to minikube's Docker daemon
eval $(minikube docker-env)

# Option 1: Pull from DockerHub (recommended)
docker pull hassankalantari/simple-library-app:latest
# Option 2: Build locally (if you want to make changes)
# docker build -t hassankalantari/simple-library-app:latest .
```

### 4. 🚀 Deploy to Kubernetes
```
# Apply all Kubernetes configurations
kubectl apply -f k8s/

# Wait for deployments to be ready
kubectl rollout status deployment/django
kubectl rollout status deployment/postgres
```

### 5. 🔍 Verify Deployment
```
# Check running pods
kubectl get pods

# Check services
kubectl get services
```

### 6. 🌐 Access the Application
```
# Open the service in your default browser
minikube service django-service
```

## 📁 Project Structure
```
SimpleLibraryApp/
├── .dockerignore               # Docker ignore file
├── .env                        # Environment variable file (You should add this later!)
├── .gitignore                  # Git ignore file
├── Dockerfile                  # Docker image build instructions
├── README.md                   # Main project README
├── README.Docker.md            # Docker-specific instructions (split out for clarity)
├── books_and_authors.json      # Sample data to populate the database
├── compose.yaml                # Docker Compose configuration
├── manage.py                   # Django entry point
├── requirements.txt            # Python dependencies

├── apis/                       # Custom API logic (views, serializers, routers)
├── books/                      # Django app: book/author models and logic
├── K8s/                        # Kubernetes configuration files
│   ├── django-deployment.yaml  # Django app deployment and service
│   ├── postgres-deployment.yaml# PostgreSQL deployment and service
│   ├── postgres-pv-pvc.yaml   # Persistent volume configuration
│   └── postgres-configmap-secret.yaml # Database configuration
├── Postman Collections/        # Postman files for API testing
├── SimpleLibraryApp/           # Django project settings and URLs
├── temp_tests/                 # Temporary or manual testing scripts
└── .venv/                      # (Optional) Virtual environment (You add this later!)
```

## 🧠 Features
- Django + PostgreSQL backend
- RESTful API for book/author management
- Environment configuration via .env
- Kubernetes deployment support
- Dockerized deployment with docker-compose
- Clean project structure
- Easily extensible

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
