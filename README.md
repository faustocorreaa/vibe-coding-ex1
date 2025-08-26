# Vibe Coding FastAPI Project

A well-structured FastAPI project following best practices for scalable web API development.

## 🚀 Features

- ✅ FastAPI with automatic API documentation
- ✅ Modular architecture with clean separation of concerns
- ✅ Environment-based configuration
- ✅ Type hints throughout the codebase
- ✅ Development and production dependencies
- ✅ Best practices folder structure

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
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
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

## 🧪 Testing

Run tests using pytest:
```bash
pytest
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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Fausto Correa** - AWS Certified Solutions Architect
- GitHub: [@faustocorreaa](https://github.com/faustocorreaa)
