# 💼 Job Portal

A Django-based Job Portal that connects **Employers** and **Job Seekers**. Employers can post and manage job listings, while job seekers can browse and apply for jobs.

---

## 🚀 Features

### Employer
- Register & Login
- Create Job Posts
- Edit/Delete Jobs
- View Posted Jobs

### Job Seeker
- Register & Login
- Browse Jobs
- View Job Details
- Apply for Jobs
- View Applied Jobs

### Security
- Role-Based Authentication
- Login Required Pages
- CSRF Protection
- Duplicate Application Prevention

---

## 🛠️ Tech Stack

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap
- Django ORM

---

## 📂 Project Structure

```
job_portal/
│
├── accounts/        # Authentication & User Management
├── jobs/            # Job & Application Management
├── templates/       # HTML Templates
├── static/          # CSS, JS, Images
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# 🏗️ System Architecture

```
                  +-------------+
                  |    Browser  |
                  +------+------+
                         |
                         ▼
                  +-------------+
                  |   URLs      |
                  +------+------+
                         |
                         ▼
                  +-------------+
                  |    Views    |
                  +------+------+
                         |
         +---------------+---------------+
         |                               |
         ▼                               ▼
+------------------+             +------------------+
|      Models      |             |    Templates     |
+--------+---------+             +--------+---------+
         |                                |
         ▼                                ▼
   +-------------+                 HTML Response
   | SQLite DB   |
   +-------------+
```

---

## 🗄️ Database Design

```
+----------------+
|   CustomUser   |
+----------------+
| id             |
| username       |
| email          |
| role           |
+--------+-------+
         |
         | 1
         |
         | *
+--------v-------+
|      Job       |
+----------------+
| title          |
| company        |
| salary         |
| location       |
| posted_by      |
+--------+-------+
         |
         | 1
         |
         | *
+--------v-------+
|  Application   |
+----------------+
| applicant      |
| job            |
| applied_date   |
+----------------+
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/rohanvw/job_portal.git

# Navigate to project
cd job_portal

# Create virtual environment
python -m venv env

# Activate virtual environment
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## 📌 Django Concepts Used

- MVT Architecture
- Django ORM
- Custom User Model
- Authentication & Authorization
- CRUD Operations
- Class-Based Views (CBV)
- Model Forms
- URL Routing
- Template Engine
- Foreign Key Relationships
- Pagination
- Django Admin

---

## 🔮 Future Improvements

- Resume Upload
- Job Search & Filters
- Email Notifications
- REST API (Django REST Framework)
- PostgreSQL Support
- Docker Deployment

---

## 👨‍💻 Developed By

Rohan Wahule
