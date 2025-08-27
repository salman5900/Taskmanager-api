# Django REST Task Manager API

A robust and secure Task Manager API built with Django and Django REST Framework. This API provides a foundation for a modern task management application, featuring secure user authentication using JSON Web Tokens (JWT).

---

## ✨ Features

-   **User Registration:** New users can create an account.
-   **JWT Authentication:** Secure, stateless authentication using `djangorestframework-simplejwt`. Users can log in to receive access and refresh tokens.
-   **Token Refresh:** Users can obtain a new access token using a valid refresh token without needing to re-enter their credentials.
-   **Secure Logout:** Implements a token blacklist to securely invalidate refresh tokens upon logout.
-   **CRUD Operations for Tasks:** Authenticated users can Create, Read, Update, and Delete their own tasks.
-   **Permissions:** Users can only view and modify tasks that they have created.

---

## 🛠️ Technology Stack

-   **Backend:** Python, Django
-   **API Framework:** Django REST Framework (DRF)
-   **Authentication:** djangorestframework-simplejwt
-   **Database:** SQLite3 (default, configurable)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.8+
-   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://your-repository-url.com/project.git](https://your-repository-url.com/project.git)
    cd project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

---

## 🔑 API Endpoints & Authentication

Authentication is handled via JWT. To access protected endpoints, you must include an `Authorization` header with the value `Bearer <your_access_token>`.

### User Authentication

#### 1. Register a New User

-   **Endpoint:** `POST /api/v1/users/register/`
-   **Description:** Creates a new user account.
-   **Body:**
    ```json
    {
        "username": "newuser",
        "password": "strongpassword123"
    }
    ```

#### 2. Log In (Get Tokens)

-   **Endpoint:** `POST /api/token/`
-   **Description:** Authenticates a user and returns a pair of access and refresh tokens.
-   **Body:**
    ```json
    {
        "username": "newuser",
        "password": "strongpassword123"
    }
    ```
-   **Successful Response:**
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

#### 3. Refresh Access Token

-   **Endpoint:** `POST /api/token/refresh/`
-   **Description:** Provides a new access token if the refresh token is valid.
-   **Body:**
    ```json
    {
        "refresh": "your_long_refresh_token_here"
    }
    ```

#### 4. Log Out (Blacklist Token)

-   **Endpoint:** `POST /api/v1/users/logout/`
-   **Description:** Adds the user's refresh token to a blacklist, invalidating it for future use.
-   **Authentication:** Requires a valid `access_token`.
-   **Body:**
    ```json
    {
        "refresh": "your_long_refresh_token_here"
    }
    ```

### Task Management (CRUD)

**Authentication:** All task endpoints require a valid `access_token` in the `Authorization: Bearer <token>` header.

#### 1. List All Your Tasks

-   **Endpoint:** `GET /api/v1/tasks/`
-   **Description:** Retrieves a list of all tasks created by the authenticated user.

#### 2. Create a New Task

-   **Endpoint:** `POST /api/v1/tasks/`
-   **Description:** Creates a new task.
-   **Body:**
    ```json
    {
        "title": "My First Task",
        "description": "Complete the project README file.",
        "is_completed": false
    }
    ```

#### 3. Retrieve a Specific Task

-   **Endpoint:** `GET /api/v1/tasks/{id}/`
-   **Description:** Retrieves the details of a single task.

#### 4. Update a Task

-   **Endpoint:** `PUT /api/v1/tasks/{id}/` or `PATCH /api/v1/tasks/{id}/`
-   **Description:** Updates a task. `PUT` requires all fields, while `PATCH` allows for partial updates.
-   **Body:**
    ```json
    {
        "is_completed": true
    }
    ```

#### 5. Delete a Task

-   **Endpoint:** `DELETE /api/v1/tasks/{id}/`
-   **Description:** Deletes a specific task.