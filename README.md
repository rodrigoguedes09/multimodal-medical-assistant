# Medical Automation API

Complete medical automation system developed in Python with Flask, providing a robust REST API for managing patients, doctors, appointments, and an intelligent virtual assistant. The application includes a Redis caching system for performance optimization and a complete suite of automated tests.

## Overview

This application demonstrates a complete architecture for medical clinic management, including:

* **REST API** built with Flask
* **N8N Integration** for workflow automation
* **Virtual Assistant** with natural language processing
* **Redis Cache System** for high performance
* **SQLite Database** for data persistence
* **Telegram Integration** for conversational user interface
* **Voice Command Support** via ElevenLabs TTS/STT
* **Generative AI** using Google Gemini Flash 2.5

The system was developed following software architecture best practices, with clear separation of concerns, robust data validation, and automated test coverage.

## System Demonstration

### Telegram Integration Workflow

The system implements a complete automation flow with the following steps:

1. **Message Reception**: Telegram trigger captures text or audio messages.
2. **Audio Processing**: Automatic transcription using ElevenLabs for better context.
3. **AI Processing**: Gemini Flash 2.5 agent processes user intent.
4. **API Integration**: N8N sub-workflow executes REST API calls.
5. **Contextual Response**: System returns a response in the same format (text or audio) as the original message.

**Patient Management:**

* Complete registration with validation for tax ID (CPF), email, and phone.
* Query, update, and removal of records.
* Secure storage of personal data.

**Appointment System:**

* Availability check by doctor and date.
* Automatic appointment booking.
* Cancellation and rescheduling of appointments.
* Information on pricing and payment methods.

**Intelligent Virtual Assistant:**

* Natural language processing.
* Automatic detection of user intent.
* Booking via conversation.
* Contextual and personalized responses.

**Redis Cache System:**

* Intelligent cache with configurable TTL.
* Automatic invalidation on CRUD operations.
* Graceful fallback when Redis is unavailable.
* Real-time performance monitoring.

### API Usage Example

```bash
# Check system health
curl http://localhost:5000/health

# List patients
curl http://localhost:5000/patients

# Check available schedules
curl http://localhost:5000/available-schedules?date=2025-09-10

# Interact with the virtual assistant
curl -X POST http://localhost:5000/ai-agent \
  -H "Content-Type: application/json" \
  -d '{"message": "What times are available?", "user_id": "user123"}'

```

---

## N8N Integration

### Overview

The system was developed with native integration for N8N (Node Automation), allowing for full automation of medical workflows through visual interfaces.

### Integration Features

* **Webhook Endpoints**: All API endpoints are compatible with N8N webhooks, allowing for event-based triggers.
* **ElevenLabs Integration**: Text-to-Speech (TTS) and Speech-to-Text (STT) transformations using the ElevenLabs API for full voice command support.
* **AI Agent with Gemini**: Utilizes Google's Gemini 2.5 Flash model, offering excellent performance and cost-benefit for natural language processing.
* **Email Confirmation**: Automated confirmation system via N8N sub-workflow, integrated as a tool for the AI agent.
* **Data Processing**: Structured JSON responses facilitate processing by N8N nodes.
* **Virtual Assistant**: The `/ai-agent` endpoint provides natural language processing for conversation automation.

---

## Quick Start

### Prerequisites

* Python 3.11 or higher
* Redis Server (Optional - system works with fallback)
* Git for version control

### Installation and Execution

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/medical-automation-api.git
cd medical-automation-api

```


2. **Create a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure environment variables (Optional):**
```bash
cp .env.example .env
# Edit the .env file as needed

```


5. **Run the application:**
```bash
cd src
python app.py

```


6. **Access the API:**
`http://localhost:5000`

### Running Tests

```bash
# Run all tests
python run_tests.py

# Or use pytest directly
pytest tests/ -v

# Generate HTML report
pytest tests/ --html=test_report.html --self-contained-html

```

---

## Project Structure

```
medical-automation-api/
├── README.md                   # Main documentation
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Test configuration
├── run_tests.py                # Test runner script
├── .gitignore                  # Version control ignore file
├── config/                     # Configuration files
│   ├── __init__.py
│   └── settings.py             # Application settings
├── src/                        # Main source code
│   ├── app.py                  # Main Flask application
│   ├── database/               # Data layer
│   │   ├── connection.py       # SQLAlchemy connection
│   │   ├── seed_data.py        # Initial data
│   │   └── seed_data_new.py    # Expanded data
│   ├── models/                 # Data models
│   │   ├── patient.py          # Patient model
│   │   └── appointment.py      # Appointment/Doctor models
│   ├── routes/                 # API routes
│   │   ├── patients.py         # Patient endpoints
│   │   └── appointments.py     # Appointment endpoints
│   ├── services/               # Business logic
│   │   ├── patient_service.py  # Patient services
│   │   ├── appointment_service.py # Appointment services
│   │   └── cache_service.py    # Redis cache system
│   └── utils/                  # Utilities
│       └── validators.py       # Input validators
├── tests/                      # Test suite
│   ├── test_unit_core.py       # 17 unit tests
│   ├── test_api_integration.py # 28 integration tests
│   └── TEST_DOCUMENTATION.md   # Test documentation
└── docs/                       # Additional documentation
    ├── cache-documentation.md   # Cache documentation
    ├── advanced-features-guide.md # Advanced features guide
    └── n8n-workflow-guide.md    # N8N integration guide

```

---

## Technologies Used

### Backend Framework

* **Flask 2.3.3**: Minimalist and flexible web framework for Python.
* **SQLAlchemy 2.0+**: ORM (Object-Relational Mapping) for Python.
* **SQLite**: Embedded database for development and testing.

### Caching System

* **Redis**: High-performance in-memory cache system.
* **Fallback Mode**: System functions normally without Redis available.
* **Configurable TTL**: Cache with automatic expiration (Default: 5 minutes).

### Testing and Code Quality

* **pytest 7.1.2+**: Modern testing framework for Python.
* **pytest-html**: Detailed HTML report generation.
* **pytest-cov**: Code coverage analysis.
* **45 Automated Tests**: 100% success rate.

---

## Application Architecture

### Design Pattern

The application follows a Layered Architecture with clear separation of concerns:

1. **API Routes Layer**: HTTP Endpoints.
2. **Services Layer**: Business Logic.
3. **Cache Layer**: Redis caching system.
4. **Models Layer**: Data Models.
5. **Database Layer**: SQLite Persistence.

### Redis Cache System

* **Intelligent Cache**: 5-minute TTL for dynamic data.
* **Automatic Invalidation**: Cache cleared automatically during CRUD operations.
* **Graceful Fallback**: Operates without Redis if the server is down.
* **Health Monitoring**: Continuous monitoring of cache health.

---

## API Reference

### Health and Cache Endpoints

* `GET /health`: Check application health status.
* `GET /cache/stats`: Returns cache system statistics.
* `GET /cache/health`: Check Redis health status.

### Patient Endpoints

* `GET /patients`: List all registered patients.
* `GET /patients/{id}`: Get a specific patient by ID.
* `POST /patients`: Create a new patient.
* `PUT /patients/{id}`: Update an existing patient.
* `DELETE /patients/{id}`: Remove a patient from the system.

### Doctor and Appointment Endpoints

* `GET /doctors`: List all registered doctors.
* `GET /available-schedules`: List available time slots.
* Query params: `?date=YYYY-MM-DD&doctor_id=int`


* `POST /appointments`: Book a new appointment.
* `DELETE /appointments/{id}`: Cancel a scheduled appointment.
* `GET /payment-info`: Information regarding prices and payment methods.

### Virtual Assistant Endpoint

* `POST /ai-agent`: Interact with the virtual assistant.
* Body: `{"message": "string", "user_id": "string"}`



---

## Tests

### Complete Test Suite

The application features 45 automated tests with a 100% success rate:

* **Unit Tests (17 tests)**: Format validation (Tax ID, email, phone, dates), business logic, utility functions, and intent detection.
* **Integration Tests (28 tests)**: API endpoints, Redis cache integration, database persistence, and AI agent real-world use cases.

### Running the Tests

* **Interactive Script**: `python run_tests.py`
* **Direct Pytest**: `pytest tests/ -v`
* **Code Coverage**: `pytest tests/ --cov=src --cov-report=html`

## License

This project is licensed under the **MIT License** - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---
