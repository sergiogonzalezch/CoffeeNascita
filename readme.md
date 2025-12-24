# CoffeeNascita ☕

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![Status](https://img.shields.io/badge/status-prototype-yellow.svg)

**CoffeeNascita** is a growing web application prototype designed for a modern coffee store business. Currently serving as a foundational sketch, this project demonstrates core e-commerce capabilities using the latest Django standards and is being actively developed to expand its features.

## 🚀 Future Roadmap & Goals

This project is an evolving work-in-progress. The development plan aims to transform this prototype into a comprehensive platform with the following upcoming features:

* **🏠 Landing Page:** Replacing the current immediate store view with a dedicated, high-conversion main landing page.
* **📊 Dashboard Admin Dashboard:** Developing a robust internal module for advanced order management, sales queries, and analytics.
* **🔍 Enhanced User Experience:** Improving the customer portal to allow more detailed order tracking and history queries.

## 🚀 Key Features

* **🛒 E-commerce Functionality:** robust product display, cart management, and order processing.
* **🎨 Modern UI:** Beautifully styled with **Tailwind CSS** via `crispy-tailwind` integration.
* **🔌 API First:** RESTful API endpoints powered by **Django REST Framework** for future scalability (mobile apps, etc.).
* **🖼️ Media Handling:** Optimized image processing using **Pillow**.
* **🔒 Security:** Environment variable management with `django-environ` for secure configuration.

## 🛠️ Tech Stack

* **Backend:** Django 5.2.8
* **API:** Django REST Framework 3.16.1
* **Database:**
    * *Development:* SQLite
    * *Production:* PostgreSQL (`psycopg2-binary`)
* **Frontend:** Django Crispy Forms & Crispy Tailwind
* **Infrastructure:** AWS Elastic Beanstalk (Configuration in progress)

## 📋 Prerequisites

Ensure you have the following installed on your system:

* **Python 3.10+**
* **Git**
* **PostgreSQL** (Optional for local dev, required for production simulation)

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
    *(Make sure to rename your file if it's still named 'requeriments')*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables (.env):**
    Create a `.env` file in the root directory to store your secrets.

    *Example `.env` content:*
    ```env
    DEBUG=True
    SECRET_KEY=your-secret-key-here
    DATABASE_URL=postgres://user:password@localhost:5432/coffeenascita_db
    # If using SQLite locally, you can omit DATABASE_URL
    ```

5.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` to see the app in action.

## ☁️ Deployment

The project is being configured for deployment on **AWS Elastic Beanstalk**.
* **Status:** 🚧 Work in Progress (WIP).
* Configuration files can be found in the `.ebextensions/` directory.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Created by [Sergio Gonzalez](https://github.com/sergiogonzalezch)*