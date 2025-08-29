# Office Task Manager API

A high-performance and secure **Office Task Manager API** built with Django and Django REST Framework. This API is designed for a professional environment, enabling managers to create and assign tasks while allowing users to manage their own workloads efficiently. The system emphasizes accountability and focus, with features like admin oversight and protections against altering completed work.

---

## ✨ Features

-   **User Registration:** New users can create an account.
-   **JWT Authentication:** Secure, stateless authentication using `djangorestframework-simplejwt`. Users log in to receive access and refresh tokens.
-   **Token Refresh & Secure Logout:** Supports token refreshing and implements a token blacklist to securely invalidate tokens upon logout.
-   **Role-Based Permissions:**
    -   **Users:** Can create, view, and update tasks assigned to them.
    -   **Admins (Superusers):** Have full oversight. They can view all tasks, create new tasks, and assign them to any user.
-   **Advanced Task Management:**
    -   **CRUD Operations:** Authenticated users can manage their assigned tasks.
    -   **Task Assignment:** Admins can create tasks and assign them to specific users to delegate work.
    -   **Immutable Records:** Once a task is marked as `completed`, it **cannot be updated or deleted**, ensuring a permanent record of finished work.
-   **Dynamic Filtering:** The task list endpoint supports filtering, allowing users to view tasks based on their completion status (e.g., `?is_completed=true`).

---

## 🛠️ Technology Stack

-   **Backend:** Python, Django
-   **API Framework:** Django REST Framework (DRF)
-   **Authentication:** `djangorestframework-simplejwt`
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

5.  **Create a superuser (Admin) to access the admin panel and admin-only endpoints:**
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

Authentication is handled via JWT. To access protected endpoints, include an `Authorization` header with the value `Bearer <your_access_token>`.

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
-   **Description:** Authenticates a user and returns access and refresh tokens.
-   **Body:**
    ```json
    {
        "username": "newuser",
        "password": "strongpassword123"
    }
    ```

#### 3. Refresh Access Token

-   **Endpoint:** `POST /api/token/refresh/`
-   **Description:** Provides a new access token using a valid refresh token.
-   **Body:**
    ```json
    {
        "refresh": "your_long_refresh_token_here"
    }
    ```

#### 4. Log Out (Blacklist Token)

-   **Endpoint:** `POST /api/v1/users/logout/`
-   **Description:** Invalidates the user's refresh token.
-   **Authentication:** Requires a valid `access_token`.
-   **Body:**
    ```json
    {
        "refresh": "your_long_refresh_token_here"
    }
    ```

### Task Management (CRUD)

**Authentication:** All task endpoints require a valid `access_token`.

#### 1. List & Filter Tasks

-   **Endpoint:** `GET /api/v1/tasks/`
-   **Description:** Retrieves a list of tasks assigned to the authenticated user. **Admins** will see all tasks from all users.
-   **Filtering:** Filter by completion status by appending `?is_completed=true` or `?is_completed=false`.

#### 2. Create a New Task

-   **Endpoint:** `POST /api/v1/tasks/`
-   **Description:** Creates a new task.
    -   **Regular users:** The task is automatically assigned to themselves.
    -   **Admins:** Can optionally provide a `user` ID in the body to assign the task to a specific user.
-   **Body (User):**
    ```json
    {
        "title": "My New Task",
        "description": "A detailed description of what needs to be done."
    }
    ```
-   **Body (Admin assigning to user with ID 5):**
    ```json
    {
        "title": "Task for Employee",
        "description": "Please complete the quarterly report.",
        "user": 5
    }
    ```

#### 3. Retrieve a Specific Task

-   **Endpoint:** `GET /api/v1/tasks/{id}/`
-   **Description:** Retrieves the details of a single task.

#### 4. Update a Task

-   **Endpoint:** `PUT /api/v1/tasks/{id}/` or `PATCH /api/v1/tasks/{id}/`
-   **Description:** Updates an existing task.
-   **Restriction:** This action is **denied** if the task's `is_completed` status is `true`.
-   **Body (Example):**
    ```json
    {
        "title": "Updated Task Title",
        "is_completed": true
    }
    ```

#### 5. Delete a Task

-   **Endpoint:** `DELETE /api/v1/tasks/{id}/`
-   **Description:** Deletes a specific task.
-   **Restriction:** This action is **denied** if the task's `is_completed` status is `true`.