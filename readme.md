# CoffeeNascita ☕

**CoffeeNascita** is a web application designed for a coffee store business. It provides a digital storefront to showcase products, manages orders, and delivers an engaging user experience using modern web technologies.

## 🚀 Key Features

* **E-commerce Functionality:** Product display and management.
* **Modern UI:** Styled with **Tailwind CSS** integration via `crispy-tailwind`.
* **API Support:** RESTful API endpoints powered by **Django REST Framework**.
* **Image Processing:** Efficient image handling with **Pillow**.
* **Environment Management:** Secure configuration using `django-environ`.

## 🛠️ Tech Stack

This project relies on a robust set of libraries. The key technologies include:

* **Backend Framework:** Django 5.2.8
* **API:** Django REST Framework 3.16.1
* **Database:** * *Development:* SQLite (default)
  * *Production:* PostgreSQL (via `psycopg2-binary`)
* **Frontend/Forms:** Django Crispy Forms & Crispy Tailwind
* **Utilities:** IPython, Colorama, SQLParse

## 📋 Requirements

Ensure you have the following installed on your system before starting:

* **Python 3.10+**
* **PostgreSQL** (Recommended for production environments)
* **Git**

### Python Dependencies
The project relies on specific versions of the following packages (see `requirements.txt` for the full list):

* `Django==5.2.8`
* `djangorestframework==3.16.1`
* `psycopg2-binary==2.9.11`
* `django-crispy-forms==2.5`
* `crispy-tailwind==1.0.3`
* `pillow==12.0.0`
* `django-environ==0.12.0`

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sergiogonzalezch/CoffeeNascita.git](https://github.com/sergiogonzalezch/CoffeeNascita.git)
    cd CoffeeNascita
    ```

2.  **Create and activate a virtual environment:**
    
    * **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables (.env):**
    Since this project uses `django-environ`, create a `.env` file in the root directory (alongside `manage.py`) to configure your database and secret keys.
    
    *Example `.env` content:*
    ```env
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=postgres://user:password@localhost:5432/coffeenascita_db
    ```

5.  **Database Migration:**
    Apply the migrations to set up your database schema (PostgreSQL or SQLite):
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    Open your browser at `http://127.0.0.1:8000/`.

## 🗄️ Database Note

While the project is configured to use **PostgreSQL** in production (using `psycopg2-binary`), you may default to SQLite for local development unless you configure the `DATABASE_URL` in your `.env` file to point to a local Postgres instance.

## 🤝 Contributing

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewFeature`)
3.  Commit your Changes (`git commit -m 'Add NewFeature'`)
4.  Push to the Branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request

## 📄 License

This project is open-source.

---
*Created by [Sergio Gonzalez](https://github.com/sergiogonzalezch)*