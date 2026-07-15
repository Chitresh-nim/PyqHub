# 🎓 AKTU PYQ Hub

> **A Production-Grade Full-Stack Platform for AKTU Students** — Built with Django REST Framework, Supabase Cloud Storage, and Comprehensive Testing

[![Deployed on Render](https://img.shields.io/badge/Deployed_on-Render-46C2D2?style=for-the-badge&logo=render&logoColor=white)](https://aktu-pyq-hub.onrender.com)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-A30000?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)](https://jwt.io/)
[![Tests](https://img.shields.io/badge/Tests-13_Passing-brightgreen?style=for-the-badge)](https://github.com/yourusername/aktu-pyq-hub/actions)
[![Coverage](https://img.shields.io/badge/Coverage-95%25-success?style=for-the-badge)](https://github.com/yourusername/aktu-pyq-hub)

---

## 📌 Overview

**AKTU PYQ Hub** is a full-stack web application that helps Dr. A.P.J. Abdul Kalam Technical University students access Previous Year Question Papers (PYQs) efficiently. Built with a **RESTful API-first architecture**, integrated with **Supabase cloud storage**, and backed by **comprehensive testing**, the platform delivers a seamless, secure, and scalable experience.

> **⚠️ Note:** This project is in **active development**. The paper database is being progressively populated through Django admin. Check back regularly for new content!

**🔗 Live Demo:** https://pyqhub-2mdn.onrender.com

---

## ✨ Key Features

### 🔐 Authentication & Profiles
- Secure registration/login with validation
- JWT + Session-based authentication
- Profile management with picture upload
- Password hashing (PBKDF2)

### 📄 Question Paper Management
- Browse papers with pagination (5 per page)
- Subject-wise & year-wise organization
- Download PDFs from Supabase cloud storage
- Django admin for easy data entry

### 🔍 Search & Filtering
- Instant search by subject name/code
- Filter by Branch, Semester, Academic Year
- Real-time results with Fetch API
- Rate-limited API (30 requests/min)

### ⭐ Bookmark System
- Bookmark/remove papers instantly
- View all bookmarks in dashboard
- AJAX-based toggle with feedback

### 🛡️ Security
- Rate limiting to prevent abuse
- CSRF & XSS protection
- File validation (size & type)
- Admin-only dashboard access

### 🧪 Testing
- 13 unit tests with 95% coverage
- Error handling with logging
- Form & file validation

### 📱 Responsive UI
- Mobile-first design with Bootstrap 5
- Clean card-based layout
- Toast notifications for feedback

---

## 🏗️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Core Language |
| **Django 4.2** | Web Framework |
| **Django REST Framework** | API Development |
| **PostgreSQL 15** | Production Database |
| **Supabase** | Cloud File Storage |
| **Gunicorn** | WSGI Server |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5/CSS3** | Structure & Styling |
| **Bootstrap 5.3** | UI Framework |
| **JavaScript ES6** | Interactivity |
| **Fetch API** | AJAX Requests |

### Tools & Infrastructure
| Tool | Purpose |
|------|---------|
| **Git** | Version Control |
| **Django Test Framework** | Unit Testing |
| **Coverage.py** | Test Coverage |
| **Render** | Hosting |
| **Supabase** | Storage |

---

Roadmap

✅ Completed

· User Authentication
· Search & Filtering
· Bookmark System
· REST API
· Supabase Storage
· Unit Tests (13)
· Deployment on Render

🚀 Planned

· Populate 500+ papers
· PDF preview
· User analytics dashboard
· Paper recommendations
· Mobile app (React Native)
· Docker containerization
· CI/CD pipeline


## 🤝 Contributing

Contributions welcome!

### Ways to Help:
- 📚 Add question papers via /admin
- 🐛 Report bugs via Issues
- 💡 Suggest features
- 👨‍💻 Submit code via Pull Requests

### Quick Steps:
1. Fork the repo
2. Make changes
3. Submit PR

### No Coding Required:
- Add papers
- Report bugs
- Share with friends

Thank you for helping! 🎓

Author : Chitresh Nimkar
