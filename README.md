# Lost & Found Platform (V1)

## Table of Contents

1. Project Overview
2. Features
3. Tech Stack
4. Project Structure
5. Installation & Setup
6. Usage
7. API Endpoints
8. Known Issues / Limitations
9. Future Improvements
10. Contributing
11. License

---

## 1. Project Overview

Lost & Found Platform is a full-stack web application that allows users to report lost and found items.

**V1 Highlights:**

* Public dashboard showing all lost and found items  
* Backend developed entirely by me using Python, Django, and Django REST Framework  
* Frontend fully generated and enhanced using AI (Bootstrap + HTML + CSS)  
* Admin access available via Django’s default admin panel  
* Designed for educational purposes and hands-on experience with backend development

---

## 2. Features

### V1 (Base version)

* Report lost items  
* Report found items  
* Public dashboard showing all lost/found items  
* Polished frontend UI (floating triangle animations, responsive cards, gradient buttons)  
* Admin functionality available via Django admin panel

> **Note:** Search and view items feature is visible in frontend but not fully implemented in V1.

---

## 3. Tech Stack

* **Backend:** Django, Django REST Framework  
* **Frontend:** HTML, CSS, Bootstrap 5 (fully AI-generated)  
* **Database:** SQLite (development)  
* **Version Control:** Git, GitHub

---

## 4. Project Structure

```
accounts/       # User models and authentication
api/            # API endpoints and serializers
frontend/       # AI-generated frontend templates & static files
reports/        # Lost/Found item models
LostFoundProject/  # Django project settings & URLs
manage.py       # Django management script
requirements.txt # Python dependencies
```

---

## 5. Installation & Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd Lost-and-Found-Platform-V1
```

2. Create a virtual environment:

```bash
python -m venv env
```

3. Activate the environment:

* **Windows:** `env\Scripts\activate`  
* **Linux/Mac:** `source env/bin/activate`

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start the server:

```bash
python manage.py runserver
```

---

## 6. Usage

1. Access the public dashboard to view lost and found items  
2. Report lost or found items  
3. Admin users can manage items, users, and data via Django admin panel

---

## 7. API Endpoints (High-Level)

| Endpoint                      | Method   | Description            |
| ----------------------------- | -------- | ----------------------|
| /api/lost-items/              | GET/POST | List/Create lost items |
| /api/found-items/             | GET/POST | List/Create found items |

> All other endpoints like claims or JWT authentication are only in V2

---

## 8. Known Issues / Limitations

* No authentication implemented in V1
* Search and match functionality not implemented
* Some minor frontend inconsistencies

---

## 9. Future Improvements

* Add search and view items functionality
* Implement claims system
* Add JWT authentication
* Enhance frontend interactivity
* Switch to PostgreSQL/MySQL for production

---

## 10. Contributing

1. Fork the repository  
2. Create a new branch for changes  
3. Commit your changes  
4. Push to your branch and create a pull request

---

## 11. License

This project is open-source for educational purposes.
