# Django Library Management System

## Overview
This Django project is designed for managing a library system, capable of handling book inventories, user management, and more. The project is configured for deployment using Vercel, making it easily accessible via the web.

## Deployed Project Link
[Library Management System](https://library-management-deploy.vercel.app/)

## Features
- User management
- Book inventory management
- Automated data generation using Faker for testing

## Prerequisites
Before you begin, ensure you have Python 3.9 installed on your system. This project also requires additional Python libraries which can be installed using the provided `requirements.txt`.

## Local Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/KhalidAlMuhammed/Django-Library-Management-System.git
   cd Django-Library-Management-System
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
