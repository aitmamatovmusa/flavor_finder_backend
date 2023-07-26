# Flavor Finder Backend

Flavor Finder Backend is the backend component of the Flavor Finder web application, which allows users to find and review places to eat, as well as rate them based on their experiences. The backend is built using Django, serving as the API for the frontend application.

## Project Description

Flavor Finder Backend is responsible for handling data storage, and retrieval for the Flavor Finder web application. It provides RESTful API endpoints that the frontend application can interact with to perform various tasks, such as fetching places, leaving reviews, and calculating average ratings.

## Features

- CRUD operations for places and reviews
- Calculating and displaying average ratings for places

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL

## Installation

1. Clone this repository to your local machine using:

```bash
git clone https://github.com/aytmamatov/flavor_finder_backend.git
```

2. Navigate to the project directory:

```bash
cd flavor_finder_backend
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

4. Install the project dependencies:

```bash
pip install -r requirements.txt
```

5. Create a PostgreSQL database and configure the database settings in `flavor_finder/settings.py`.

6. Apply database migrations:

```bash
python manage.py migrate
```

7. Run the development server:

```bash
python manage.py runserver
```

## Contributing

If you would like to contribute to this project, feel free to open a pull request or submit an issue in the repository.

## License

This project is licensed under the MIT.