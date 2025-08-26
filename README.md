# Vibe Coding FastAPI Project

A well-structured FastAPI project following best practices for scalable web API development.

## 🚀 Features

- ✅ FastAPI with automatic API documentation
- ✅ Modular architecture with clean separation of concerns
- ✅ Environment-based configuration
- ✅ Type hints throughout the codebase
- ✅ Development and production dependencies
- ✅ Best practices folder structure
- ✅ Comprehensive documentation and testing

## 📚 Documentation

- **[📋 Functional Requirements](docs/FUNCTIONAL_REQUIREMENTS.md)** - Complete functional specification
- **[🔗 API Documentation](docs/API_DOCUMENTATION.md)** - API usage guide with examples
- **[🧪 Interactive API Docs](http://localhost:8000/docs)** - Swagger UI (when running)
- **[📖 Alternative Docs](http://localhost:8000/redoc)** - ReDoc interface (when running)

## 📁 Project Structure

```
vibe-coding-ex1/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py       # API router aggregation
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── hello.py # Hello World endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # App configuration
│   ├── models/              # Database models
│   │   └── __init__.py
│   ├── schemas/             # Pydantic models
│   │   └── __init__.py
│   ├── crud/                # Database operations
│   │   └── __init__.py
│   ├── db/                  # Database configuration
│   │   └── __init__.py
│   └── utils/               # Utility functions
│       └── __init__.py
├── docs/                    # Documentation files
│   ├── FUNCTIONAL_REQUIREMENTS.md
│   └── API_DOCUMENTATION.md
├── tests/                   # Test files
│   ├── __init__.py
│   └── test_hello.py
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Multi-service setup
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.8+
- pip or pipenv

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/faustocorreaa/vibe-coding-ex1.git
   cd vibe-coding-ex1
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # For development:
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

## 🚀 Running the Application

### Development Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Using Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build and run manually
docker build -t vibe-coding-fastapi .
docker run -p 8000:8000 vibe-coding-fastapi
```

The API will be available at:
- **Application:** http://localhost:8000
- **Interactive API docs (Swagger UI):** http://localhost:8000/docs
- **Alternative API docs (ReDoc):** http://localhost:8000/redoc

## 📚 API Endpoints

### Root Endpoint
- `GET /` - Welcome message

### Hello World Endpoints
- `GET /api/v1/hello/` - Returns "Hello World"
- `GET /api/v1/hello/name/{name}` - Returns personalized greeting

### Quick Test
```bash
# Test the API
curl http://localhost:8000/
curl http://localhost:8000/api/v1/hello/
curl http://localhost:8000/api/v1/hello/name/Developer
```

## 🧪 Testing

Run tests using pytest:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_hello.py -v
```

## 🔧 Development Tools

### Code Formatting
```bash
black app/
isort app/
```

### Linting
```bash
flake8 app/
mypy app/
```

### Pre-commit Hooks (Optional)
```bash
pre-commit install
pre-commit run --all-files
```

## 🏗️ Architecture

The project follows a **layered architecture** pattern:

- **API Layer** (`app/api/`): HTTP endpoints and request/response handling
- **Business Logic** (`app/core/`): Application configuration and business rules
- **Data Access** (`app/crud/`): Database operations and data manipulation
- **Data Models** (`app/models/` & `app/schemas/`): Data structures and validation
- **Utilities** (`app/utils/`): Helper functions and common utilities

## 🌟 Best Practices Implemented

- ✅ **Modular Architecture**: Clean separation of concerns
- ✅ **Type Safety**: Comprehensive type hints using Pydantic
- ✅ **Configuration Management**: Environment-based configuration
- ✅ **API Versioning**: Structured API versioning with `/api/v1/`
- ✅ **Comprehensive Testing**: Unit and integration tests
- ✅ **Documentation**: Auto-generated API docs + comprehensive guides
- ✅ **Containerization**: Docker support for consistent deployments
- ✅ **Code Quality**: Linting, formatting, and type checking
- ✅ **Security Ready**: Structure prepared for authentication/authorization

## 🚢 Deployment

### Docker Deployment
```bash
# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

### Traditional Deployment
```bash
# Install production dependencies
pip install -r requirements.txt

# Run with production settings
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Environment Variables
Essential production environment variables:
```bash
PROJECT_NAME="Your Project Name"
DEBUG=false
SECRET_KEY="your-super-secret-production-key"
DATABASE_URL="your-database-connection-string"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow the existing code style
- Add tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Fausto Correa** - AWS Certified Solutions Architect
- **GitHub:** [@faustocorreaa](https://github.com/faustocorreaa)
- **Profile:** *I design and translate Business Requirements into implementation architecture, secure and robust & high available*

---

## 📈 Roadmap

### Phase 1 ✅ (Current)
- [x] Basic FastAPI setup
- [x] Hello World endpoints
- [x] Comprehensive documentation
- [x] Testing framework
- [x] Docker support

### Phase 2 🚧 (Next)
- [ ] Database integration (PostgreSQL/SQLite)
- [ ] Authentication & Authorization (JWT)
- [ ] CRUD operations
- [ ] Input validation & error handling
- [ ] Rate limiting

### Phase 3 🔮 (Future)
- [ ] Monitoring & logging
- [ ] Caching layer (Redis)
- [ ] Background tasks (Celery)
- [ ] API metrics and analytics
- [ ] CI/CD pipeline

---

⭐ **Star this repository if you find it helpful!**
