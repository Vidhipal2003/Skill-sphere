# MyProject

A Django-based learning and student management web application with pages for home, about, services, contact, gallery, team, registration, login, and student dashboard features.

## Features
- Modern responsive UI
- Registration and login flow
- Student dashboard and learning pages
- Services, gallery, and contact pages
- SQLite-backed Django project

## Requirements
- Python 3.10+
- Django 5.x

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Project Structure
- `MyProject/` - Django project settings and URLs
- `user/` - public site pages and authentication views
- `student/` - student dashboard and learning modules
- `templates/` - HTML templates
- `static/` - images, CSS, and static assets

## Notes
This project is intended as a student portal style web application and can be extended with additional features such as admin management, email notifications, and richer dashboards.
