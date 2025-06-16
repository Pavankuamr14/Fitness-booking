# Fitness Booking System

A modern RESTful API for managing fitness class bookings, built with FastAPI and PostgreSQL.

## Video Walkthrough and Live Demo

- Video Walkthrough: https://www.loom.com/share/a2de2b71bd22446b825b0e7f90897042?sid=525e6001-263e-41cb-8285-0e68bf88cd76
- Live Demo: http://54.159.94.167/ (open it in incognito mode) 

## Features

- **Class Management**: View and manage fitness classes
- **Booking System**: Easy class booking with email notifications
- **Time Zone Support**: Flexible timezone handling for global users
- **API Documentation**: Interactive Swagger UI documentation
- **Docker Support**: Easy deployment with Docker
- **PostgreSQL Database**: Reliable data storage with SQLModel

## Tech Stack

- **Backend**: FastAPI, Python 3.11
- **Database**: PostgreSQL
- **ORM**: SQLModel
- **Containerization**: Docker
- **Frontend**: HTML, CSS (with modern design)

## Prerequisites

- Python 3.11+
- Docker (optional)
- PostgreSQL (if running locally)
- Postman (for API testing)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/Pavankuamr14/Fitness-booking.git
cd Fitness-booking
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
DB_HOST=your_database_host
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

## Running the Application 🏃‍♂️

### Local Development

1. Start the application:
```bash
uvicorn main:app --reload
```

2. Access the API documentation at `http://localhost:8000/docs`

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t fitness-booking .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --env-file .env fitness-booking
```

## API Documentation 📚

### Base URL
```
http://localhost:8000
```

### Available Endpoints

#### 1. Get All Classes
```bash
# cURL
curl -X GET "http://localhost:8000/classes?timezone=UTC"

# Postman
GET http://localhost:8000/classes?timezone=UTC
```

#### 2. Book a Class
```bash
# cURL
curl -X POST "http://localhost:8000/book" \
     -H "Content-Type: application/json" \
     -d '{
           "class_id": 1,
           "client_name": "John Doe",
           "client_email": "john@example.com"
         }'

# Postman
POST http://localhost:8000/book
Content-Type: application/json

{
    "class_id": 1,
    "client_name": "John Doe",
    "client_email": "john@example.com"
}
```

#### 3. Get Bookings by Email
```bash
# cURL
curl -X GET "http://localhost:8000/bookings?email=john@example.com"

# Postman
GET http://localhost:8000/bookings?email=john@example.com
```

### Postman Collection

You can import the following Postman collection to test all endpoints:

```json
{
  "info": {
    "name": "Fitness Booking API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Get All Classes",
      "request": {
        "method": "GET",
        "url": {
          "raw": "http://localhost:8000/classes?timezone=UTC",
          "query": [
            {
              "key": "timezone",
              "value": "UTC"
            }
          ]
        }
      }
    },
    {
      "name": "Book a Class",
      "request": {
        "method": "POST",
        "url": "http://localhost:8000/book",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"class_id\": 1,\n    \"client_name\": \"John Doe\",\n    \"client_email\": \"john@example.com\"\n}"
        }
      }
    },
    {
      "name": "Get Bookings by Email",
      "request": {
        "method": "GET",
        "url": {
          "raw": "http://localhost:8000/bookings?email=john@example.com",
          "query": [
            {
              "key": "email",
              "value": "john@example.com"
            }
          ]
        }
      }
    }
  ]
}
```

## Project Structure 📁

```
fitness_booking/
├── templates/          # HTML templates
├── static/            # Static files
├── main.py           # FastAPI application
├── models.py         # Database models
├── crud.py           # Database operations
├── database.py       # Database configuration
├── utils.py          # Utility functions
├── requirements.txt  # Project dependencies
└── Dockerfile        # Docker configuration
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Pavan Kumar - [GitHub Profile](https://github.com/Pavankuamr14)

Project Link: [https://github.com/Pavankuamr14/Fitness-booking.git](https://github.com/Pavankuamr14/Fitness-booking.git)

## Acknowledgments

- FastAPI for the amazing web framework
- SQLModel for the powerful ORM
- Docker for containerization
- All contributors who have helped with the project