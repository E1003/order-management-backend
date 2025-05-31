# 🧾 Order Management Backend

This is the backend for the **Order Management System**, built with **Django REST Framework**.  
It provides RESTful APIs for managing users, customers, sellers, products, categories, and orders. It also includes token-based authentication using JWT.

---

## 🚀 Features

- 🔐 JWT-based authentication (`/login/`, `/refresh/`, `/logout/`)
- 👤 User management (`/user/`)
- 👥 Customer and seller management
- 📦 Product and category management
- 🛒 Order creation, update, deletion
- 📊 API-only backend designed to work with Angular frontend

---

## 🛠 Tech Stack

- **Framework:** Django 5.x
- **API:** Django REST Framework
- **Auth:** Simple JWT
- **Database:** SQLite (can be switched to PostgreSQL)
- **Architecture:** Modular apps (`agent`, `product`, `order`)

---

## 📂 API Endpoints Summary

### 🔐 Auth Endpoints
| Method | URL        | Description               |
|--------|------------|---------------------------|
| POST   | `/login/`  | Obtain JWT token          |
| POST   | `/refresh/`| Refresh JWT token         |
| POST   | `/logout/` | Invalidate JWT token      |

### 👤 User & Agent Endpoints
| Method | URL             | Description                     |
|--------|------------------|---------------------------------|
| GET    | `/user/`         | Get current user info           |
| GET    | `/customers/`    | List all customers              |
| POST   | `/customers/`    | Create a new customer           |
| PUT    | `/customers/<id>/` | Update customer               |
| DELETE | `/customers/<id>/` | Delete customer               |
| GET    | `/sellers/`      | List all sellers                |
| POST   | `/sellers/`      | Create a new seller             |
| PUT    | `/sellers/<id>/` | Update seller                   |
| DELETE | `/sellers/<id>/` | Delete seller                   |

### 📦 Product Endpoints
| Method | URL                   | Description              |
|--------|------------------------|--------------------------|
| GET    | `/products/`           | List all products        |
| POST   | `/products/`           | Create new product       |
| PUT    | `/products/<id>/`      | Update product           |
| DELETE | `/products/<id>/`      | Delete product           |
| GET    | `/categories/`         | List all categories      |
| POST   | `/categories/`         | Create new category      |
| PUT    | `/categories/<id>/`    | Update category          |
| DELETE | `/categories/<id>/`    | Delete category          |

### 🛒 Order Endpoints
| Method | URL              | Description              |
|--------|-------------------|--------------------------|
| GET    | `/orders/`        | List all orders          |
| POST   | `/orders/`        | Create a new order       |
| PUT    | `/orders/<id>/`   | Update order             |
| DELETE | `/orders/<id>/`   | Delete order             |

---

## 🔧 Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/E1003/order-management-backend.git
cd order_backend

# 2. Create a virtual environment
python -m venv env
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
