# Login-CertSecure

# Flask User Registration and Login System

This is a Flask-based web application that provides user registration, login, and logout functionality. It uses SQLAlchemy for database management and Flask-Login for user session management. This README will guide you through setting up and running the application.

## Features

- User registration with email, username, and password.
- User login and session management.
- User logout functionality.
- Simple home page for authenticated users.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python (3.x recommended)
- Flask
- Flask-SQLAlchemy
- Flask-Login

You can install these dependencies using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login
```

## Setup

1. Clone the repository or download the code.

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. In the project directory, run the following command to initialize the SQLite database:

   ```bash
   python
   ```

   ```python
   from app import db
   with app.app_context():
       db.create_all()
   ```

   Exit the Python shell by typing `exit()`.

## Configuration

Open the `app.py` file and modify the following configurations:

- `app.config["SECRET_KEY"]`: Change the secret key to a secure random string.
- `app.config["SQLALCHEMY_DATABASE_URI"]`: You can change the database URI if needed (e.g., use a different database like PostgreSQL).

## Running the Application

To run the application, use the following command:

```bash
python app.py
```

The application will start, and you can access it in your web browser at `http://localhost:5000`.

## Usage

### User Registration

1. Access the registration page by going to `http://localhost:5000/register`.
2. Fill in your desired username, email, and password.
3. Click the "Register" button.
4. You will be redirected to the login page.

### User Login

1. Access the login page by going to `http://localhost:5000/login`.
2. Enter your registered email and password.
3. Click the "Login" button.
4. Upon successful login, you will be redirected to the home page.

### User Logout

1. Click the "Logout" link on the home page.
2. You will be logged out and redirected to the home page.

### Home Page

- Authenticated users will see a simple home page.
- Unauthenticated users will be redirected to the login page.

## Customization

You can customize this application further by adding more features, improving the UI, or integrating additional functionality as needed. The provided code serves as a foundation for building more complex web applications with user authentication. 

Feel free to modify and extend this code to suit your specific requirements.

Enjoy using your Flask User Registration and Login System!

## License

The iValidate web page is provided under the [MIT License](LICENSE). You are free to use and modify the code for your purposes. Please review the full license text for more details.
