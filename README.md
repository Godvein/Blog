# Django Blog Website

This is a simple blog website built using Django. It allows users to create, edit, delete, and view blog posts. The project also includes features like user authentication, categories, and commenting on posts.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Blog Posts**: Create, update, delete, and view blog posts.
- **User Profile**: Create user profile and update it.
- **Admin Panel**: Manage posts, categories, and users from the Django admin interface.

## Requirements

- Python 3.x
- Django 3.x or later
- Django REST framework (if applicable)
- SQLite (default) or other database options
- Bootstrap (optional for styling)

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/Godvein/Blog-.git
    cd blog-website
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for the admin panel**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the application**
    - Go to `http://127.0.0.1:8000/` to view the blog.
    - Go to `http://127.0.0.1:8000/admin/` to access the admin panel.


