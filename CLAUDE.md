# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django-based cough sound analysis application (NIH Cough Sound) that collects audio recordings for COVID-19 and tuberculosis research. The application supports multilingual interfaces (English, Malay, Simplified Chinese) and integrates with Azure storage for production deployments.

## Development Commands

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

### Development Server
```bash
# Start development server
python manage.py runserver

# Start with specific settings
python manage.py runserver --settings=mohcough.settings
```

### Code Quality Tools
```bash
# Run Ruff linting (configured in pyproject.toml)
ruff check .

# Run Ruff formatting
ruff format .

# Pre-commit hooks are configured - run manually with:
pre-commit run --all-files
```

### Database Operations
```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset migrations (if needed)
python manage.py migrate <app_name> zero
```

### Internationalization
```bash
# Generate translation files
python manage.py makemessages -l ms  # Malay
python manage.py makemessages -l zh_Hans  # Chinese

# Compile translation files
python manage.py compilemessages
```

### Docker Development
```bash
# Local development
docker-compose -f docker-compose-local.yaml up

# Production build
docker-compose up
```

## Architecture Overview

### Django Apps Structure
- **accounts**: User management and authentication (Staff, Subject models)
- **questionnaire**: COVID/TB health questionnaires
- **recording**: Audio recording functionality (cough and breath sounds)
- **result**: Analysis results and history
- **api**: REST API endpoints for external integrations
- **common**: Shared utilities and templates

### Key Models
- `Account`: Staff user model with email-based authentication
- `Subject`: Participant model with phone number validation
- `AudioRecord`: Main audio recording model with Azure storage integration
- `AudioRecordSample`: Legacy audio recording model (deprecated)

### URL Structure
- `/`: Main application (accounts app)
- `/questionnaire/`: Health questionnaires
- `/recording/`: Audio recording interface
- `/result/`: Results and analysis
- `/api/`: REST API endpoints
- `/common/`: Shared utilities

### Static Files Organization
- **static/**: Source static files
- **staticfiles/**: Collected static files for production
- **media/**: User uploaded files (audio recordings)

## Configuration

### Environment Variables (via python-decouple)
Required environment variables should be defined in a `.env` file:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_ENGINE`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_DRIVER`: Database configuration
- `LANGUAGE_CODE`: Default language (default: 'ms')
- `TIME_ZONE`: Timezone (default: 'Asia/Kuala_Lumpur')
- `AZURE_CONNECTION_STRING`, `AZURE_CONTAINER`: Azure storage (production only)

### Database Support
- Configured for Microsoft SQL Server with Azure SQL Database support
- Uses django-mssql-backend and pyodbc drivers
- Connection pooling and unicode support enabled

### Multilingual Support
- Supported languages: English (en), Malay (ms), Simplified Chinese (zh-hans)
- Translation files located in `locale/` directory
- Uses Django's i18n framework with custom language definitions

## Testing and Deployment

### Testing
```bash
# Run tests for specific app
python manage.py test <app_name>

# Run all tests
python manage.py test
```

### Production Deployment
- Uses Gunicorn as WSGI server (configured in gunicorn.conf.py)
- WhiteNoise for static file serving
- Azure Blob Storage for media files in production
- Docker containerization with multi-stage builds
- Entry point scripts: entrypoint_dev.sh and entrypoint_prod.sh

### Audio Recording Features
- Supports both cough and breath recordings
- Multiple recording categories: COVID-19, tuberculosis, prediction
- File upload to Azure storage with organized folder structure
- Legacy support for masked/unmasked recording variants

## Security Considerations
- CORS configured for API access
- CSRF protection enabled
- Custom user model with email authentication
- Phone number validation for Malaysian format
- File upload restrictions and validation
