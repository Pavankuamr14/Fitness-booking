 # Fitness Booking System 🏋️‍♂️

A modern RESTful API for managing fitness class bookings, built with FastAPI and PostgreSQL.

## Features ✨

- **Class Management**: View and manage fitness classes
- **Booking System**: Easy class booking with email notifications
- **Time Zone Support**: Flexible timezone handling for global users
- **API Documentation**: Interactive Swagger UI documentation
- **Docker Support**: Easy deployment with Docker
- **PostgreSQL Database**: Reliable data storage with SQLModel

## Tech Stack 🛠

- **Backend**: FastAPI, Python 3.11
- **Database**: PostgreSQL
- **ORM**: SQLModel
- **Containerization**: Docker
- **Frontend**: HTML, CSS (with modern design)

## Prerequisites 📋

- Python 3.11+
- Docker (optional)
- PostgreSQL (if running locally)

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

## API Endpoints 🌐

- `GET /`: Landing page with API information
- `GET /docs`: Interactive API documentation
- `GET /classes`: List all available fitness classes
- `POST /book`: Book a fitness class
- `GET /bookings`: View bookings by email

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

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact 📧

Pavan Kumar - [GitHub Profile](https://github.com/Pavankuamr14)

Project Link: [https://github.com/Pavankuamr14/Fitness-booking.git](https://github.com/Pavankuamr14/Fitness-booking.git)

## Acknowledgments 🙏

- FastAPI for the amazing web framework
- SQLModel for the powerful ORM
- Docker for containerization
- All contributors who have helped with the project