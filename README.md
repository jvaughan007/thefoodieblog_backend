---

### **Backend Documentation (Django API)**

---

# Backend: Recipe Blog API

## Table of Contents
1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Virtual Environment Setup](#virtual-environment-setup)
4. [Migrations and Database Setup](#migrations-and-database-setup)
5. [Running the Server](#running-the-server)
6. [Available Endpoints](#available-endpoints)
7. [Project Structure](#project-structure)
8. [Environment Variables](#environment-variables)
9. [Contributing](#contributing)

---

## Overview
This is the backend API for the Recipe Blog, built using Django and Django REST Framework. It handles CRUD operations for recipes, including images and formatted blog content.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd recipe-blog-backend
   ```

2. **Virtual Environment Setup:**

   It’s highly recommended to use a virtual environment for Python projects.

   **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   ```

   **Activate the Virtual Environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create and Configure the `.env` File:**

   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

---

## Migrations and Database Setup

1. **Apply Migrations:**
   Run the following commands to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Load Seed Data (Optional):**
   If you have fixture data, load it using:
   ```bash
   python manage.py loaddata recipes.json
   ```

---

## Running the Server

1. **Run the Django Development Server:**
   ```bash
   python manage.py runserver
   ```
   The server will be available at `http://127.0.0.1:8000/`.

---

## Available Endpoints

Here is a list of the key API endpoints:

- **GET /api/recipes/**: Get all recipes.
- **GET /api/recipes/:id/**: Get a single recipe by ID.
- **POST /api/recipes/**: Create a new recipe.
- **PUT /api/recipes/:id/**: Update an existing recipe.
- **DELETE /api/recipes/:id/**: Delete a recipe.

For more details, refer to the `api/urls.py` file.

---

## Project Structure

Here is a brief overview of the main directories:

- **`api/`**: Contains the Django app for managing recipes.
- **`config/`**: Contains project settings and configuration files.
- **`media/recipe_images/`**: Stores uploaded recipe images.
- **`fixtures/`**: Contains seed data for the project (optional).

---

## Environment Variables

The backend uses a `.env` file to manage sensitive data and configuration settings. Ensure it includes:

```
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request once the changes are made.

---

These plain-text guides should be straightforward and readable when published to GitHub. If you have further questions or need more customization, feel free to ask!

