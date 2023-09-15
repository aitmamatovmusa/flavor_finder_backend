# Flavor Finder Backend

Flavor Finder Backend is the backend component of the Flavor Finder web application, providing the API for the frontend application. This backend is built using Django and Django REST Framework and utilizes PostgreSQL as the database.

## Technologies Used

- **Django**: A high-level Python web framework used for building web applications.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs in Django.
- **PostgreSQL**: A robust open-source relational database system.

## Installation

To set up and run Flavor Finder Backend on your local machine using Poetry, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aytmamatov/flavor_finder_backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flavor_finder_backend
   ```

3. Create and activate a virtual environment using Poetry:

   ```bash
   poetry install
   ```

4. Activate the virtual environment:

   ```bash
   poetry shell
   ```

5. Set up the database and configure the necessary environment variables by creating a `.env` file in your project directory. Add the following environment variables:

   ```dotenv
   SECRET_KEY=YOUR_SECRET_KEY
   DB_NAME=YOUR_DB_NAME
   DB_USER=YOUR_DB_USER
   DB_PASS=YOUR_DB_PASSWORD
   DB_HOST=YOUR_DB_HOST
   DB_PORT=YOUR_DB_PORT
   DEBUG=YOUR_DEBUG_SETTING
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

With these steps, you can set up the Flavor Finder Backend locally and start building and testing your API. The frontend component of the Flavor Finder application, including tests, can be found in the Flavor Finder Frontend repository.
