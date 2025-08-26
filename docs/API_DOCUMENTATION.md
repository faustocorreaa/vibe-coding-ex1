# API Documentation
## Vibe Coding FastAPI Project

---

## **Table of Contents**
1. [Quick Start](#quick-start)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
4. [Error Handling](#error-handling)
5. [Rate Limiting](#rate-limiting)
6. [Examples](#examples)
7. [SDKs and Libraries](#sdks-and-libraries)

---

## **Quick Start**

### **Base URL**
```
Production: https://your-domain.com
Development: http://localhost:8000
```

### **Content Type**
All API requests and responses use JSON format:
```
Content-Type: application/json
```

### **API Versioning**
Current API version: `v1`
All endpoints are prefixed with `/api/v1`

---

## **Authentication**

### **Current Status**
🚧 **No authentication required** for the current endpoints.

### **Future Implementation**
The API is designed to support:
- Bearer token authentication
- API key authentication
- OAuth 2.0 integration

---

## **Endpoints**

### **1. Root Endpoint**

Get welcome message and API status.

**Endpoint:** `GET /`

**Parameters:** None

**Response:**
```json
{
  "message": "Welcome to FastAPI project with best practices!"
}
```

**Status Codes:**
- `200 OK` - Success

**Example Request:**
```bash
curl -X GET "http://localhost:8000/" \
  -H "accept: application/json"
```

---

### **2. Hello World**

Basic hello world endpoint.

**Endpoint:** `GET /api/v1/hello/`

**Parameters:** None

**Response:**
```json
{
  "message": "Hello World"
}
```

**Status Codes:**
- `200 OK` - Success

**Example Request:**
```bash
curl -X GET "http://localhost:8000/api/v1/hello/" \
  -H "accept: application/json"
```

---

### **3. Personalized Greeting**

Get a personalized greeting message.

**Endpoint:** `GET /api/v1/hello/name/{name}`

**Path Parameters:**
| Parameter | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| `name` | string | Yes | Name to greet | 1-100 characters, alphanumeric |

**Response:**
```json
{
  "message": "Hello {name}!"
}
```

**Status Codes:**
- `200 OK` - Success
- `422 Unprocessable Entity` - Invalid name parameter

**Example Request:**
```bash
curl -X GET "http://localhost:8000/api/v1/hello/name/Fausto" \
  -H "accept: application/json"
```

**Example Response:**
```json
{
  "message": "Hello Fausto!"
}
```

---

## **Error Handling**

### **Error Response Format**
All errors follow a consistent format:

```json
{
  "detail": "Error description"
}
```

For validation errors:
```json
{
  "detail": [
    {
      "loc": ["path", "parameter_name"],
      "msg": "Error message",
      "type": "error_type"
    }
  ]
}
```

### **HTTP Status Codes**

| Status Code | Description | When it occurs |
|-------------|-------------|----------------|
| `200 OK` | Success | Request processed successfully |
| `400 Bad Request` | Invalid request | Malformed request |
| `404 Not Found` | Resource not found | Endpoint doesn't exist |
| `422 Unprocessable Entity` | Validation error | Invalid parameters |
| `429 Too Many Requests` | Rate limit exceeded | Too many requests (future) |
| `500 Internal Server Error` | Server error | Unexpected server error |

---

## **Rate Limiting**

### **Current Status**
🚧 **No rate limiting** is currently implemented.

### **Future Implementation**
Planned rate limits:
- **Anonymous users:** 100 requests per minute
- **Authenticated users:** 1000 requests per minute

Headers will include:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1635724800
```

---

## **Examples**

### **JavaScript/Node.js**

```javascript
// Using fetch
async function getHelloWorld() {
    try {
        const response = await fetch('http://localhost:8000/api/v1/hello/');
        const data = await response.json();
        console.log(data.message); // "Hello World"
    } catch (error) {
        console.error('Error:', error);
    }
}

// Using axios
const axios = require('axios');

async function getPersonalizedGreeting(name) {
    try {
        const response = await axios.get(`http://localhost:8000/api/v1/hello/name/${name}`);
        console.log(response.data.message); // "Hello {name}!"
    } catch (error) {
        console.error('Error:', error.response.data);
    }
}
```

### **Python**

```python
import requests

# Basic hello world
def get_hello_world():
    response = requests.get('http://localhost:8000/api/v1/hello/')
    if response.status_code == 200:
        data = response.json()
        print(data['message'])  # "Hello World"
    else:
        print(f"Error: {response.status_code}")

# Personalized greeting
def get_personalized_greeting(name):
    response = requests.get(f'http://localhost:8000/api/v1/hello/name/{name}')
    if response.status_code == 200:
        data = response.json()
        print(data['message'])  # "Hello {name}!"
    else:
        print(f"Error: {response.status_code}")
```

### **cURL Examples**

```bash
# Root endpoint
curl -X GET "http://localhost:8000/" \
  -H "accept: application/json"

# Hello World
curl -X GET "http://localhost:8000/api/v1/hello/" \
  -H "accept: application/json"

# Personalized greeting
curl -X GET "http://localhost:8000/api/v1/hello/name/Developer" \
  -H "accept: application/json"

# With error handling
curl -X GET "http://localhost:8000/api/v1/hello/name/" \
  -H "accept: application/json" \
  -w "HTTP Status: %{http_code}\n"
```

### **Postman Collection**

Import this collection into Postman:

```json
{
  "info": {
    "name": "Vibe Coding FastAPI",
    "description": "API collection for Vibe Coding FastAPI project"
  },
  "item": [
    {
      "name": "Root",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/",
          "host": ["{{base_url}}"],
          "path": [""]
        }
      }
    },
    {
      "name": "Hello World",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/api/v1/hello/",
          "host": ["{{base_url}}"],
          "path": ["api", "v1", "hello", ""]
        }
      }
    },
    {
      "name": "Hello Name",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/api/v1/hello/name/{{name}}",
          "host": ["{{base_url}}"],
          "path": ["api", "v1", "hello", "name", "{{name}}"]
        }
      }
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000"
    },
    {
      "key": "name",
      "value": "Developer"
    }
  ]
}
```

---

## **SDKs and Libraries**

### **Python SDK Example**

```python
import requests
from typing import Optional

class VibeCodeAPI:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip('/')
    
    def get_welcome(self) -> dict:
        """Get welcome message."""
        response = requests.get(f"{self.base_url}/")
        response.raise_for_status()
        return response.json()
    
    def hello_world(self) -> dict:
        """Get hello world message."""
        response = requests.get(f"{self.base_url}/api/v1/hello/")
        response.raise_for_status()
        return response.json()
    
    def hello_name(self, name: str) -> dict:
        """Get personalized greeting."""
        if not name or len(name) > 100:
            raise ValueError("Name must be 1-100 characters")
        
        response = requests.get(f"{self.base_url}/api/v1/hello/name/{name}")
        response.raise_for_status()
        return response.json()

# Usage
api = VibeCodeAPI()
print(api.hello_world())  # {"message": "Hello World"}
print(api.hello_name("Fausto"))  # {"message": "Hello Fausto!"}
```

### **JavaScript/TypeScript SDK Example**

```typescript
interface APIResponse {
    message: string;
}

class VibeCodeAPI {
    private baseUrl: string;

    constructor(baseUrl: string = 'http://localhost:8000') {
        this.baseUrl = baseUrl.replace(/\/$/, '');
    }

    async getWelcome(): Promise<APIResponse> {
        const response = await fetch(`${this.baseUrl}/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    }

    async helloWorld(): Promise<APIResponse> {
        const response = await fetch(`${this.baseUrl}/api/v1/hello/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    }

    async helloName(name: string): Promise<APIResponse> {
        if (!name || name.length > 100) {
            throw new Error('Name must be 1-100 characters');
        }
        
        const response = await fetch(`${this.baseUrl}/api/v1/hello/name/${encodeURIComponent(name)}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    }
}

// Usage
const api = new VibeCodeAPI();
api.helloWorld().then(data => console.log(data.message));
api.helloName('Developer').then(data => console.log(data.message));
```

---

## **Interactive Documentation**

### **Swagger UI**
Access the interactive API documentation at:
```
http://localhost:8000/docs
```

Features:
- ✅ Try out endpoints directly
- ✅ View request/response schemas
- ✅ Generate code examples
- ✅ Authentication testing (when implemented)

### **ReDoc**
Access the alternative documentation at:
```
http://localhost:8000/redoc
```

Features:
- ✅ Clean, readable format
- ✅ Comprehensive endpoint details
- ✅ Schema documentation
- ✅ Download OpenAPI spec

### **OpenAPI Specification**
Download the raw OpenAPI specification:
```
http://localhost:8000/api/v1/openapi.json
```

---

## **Testing the API**

### **Health Check**
To verify the API is running:
```bash
curl -f http://localhost:8000/ || echo "API is down"
```

### **Automated Testing**
Run the test suite:
```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

---

## **Support**

### **Issues and Bugs**
Report issues on GitHub: [Issues](https://github.com/faustocorreaa/vibe-coding-ex1/issues)

### **Feature Requests**
Submit feature requests via GitHub Issues with the "enhancement" label.

### **Community**
- **Author:** Fausto Correa - AWS Certified Solutions Architect
- **GitHub:** [@faustocorreaa](https://github.com/faustocorreaa)

---

## **Changelog**

### **v1.0.0** - August 26, 2025
- ✅ Initial release
- ✅ Basic hello world endpoints
- ✅ Comprehensive documentation
- ✅ Docker support
- ✅ Testing framework

---

**Last Updated:** August 26, 2025
