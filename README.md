# 🏠 Real Trust – Consultancy, Design & Marketing Website  
A full-stack Django-based landing website created for the **Flipr Task**, featuring dynamic project listing, happy client testimonials, auto-cropping images, and contact/newsletter backend storage.

---

## 🚀 Features

### ⭐ Landing Page Sections
- Hero + Consultation Form  
- Our Projects (Fetch from backend)  
- Happy Clients (Fetch from backend)  
- Newsletter subscription  
- Footer with navigation  

### ⭐ Backend Features
- Admin panel to:
  - Add/Edit/Delete **Projects**
  - Add/Edit/Delete **Clients**
  - View Contact form submissions
  - Manage Newsletter Subscribers  

### ⭐ Image Processing
- Admin se image upload karte hi:
  - Image automatically **crop + resize** to **450×350**
  - Cleaner UI on frontend

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django |
| Frontend | HTML, Internal CSS |
| Database | SQLite / PostgreSQL / MySQL |
| Deployment | Render / Railway |
| Media Handling | Django Media Storage + Pillow |

---
flipr_consultancy_site/
│
├── main/
│ ├── templates/
│ │ └── landing.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ └── forms.py
│
├── flipr_consultancy_site/
│ ├── settings.py
│ ├── urls.py
│
├── media/
├── manage.py
└── README.md

---

---

## ⚙ Installation Guide

### 1️⃣ Clone Repository
bash
git clone https://github.com/Amitjiyadav/flipr_consultancy_site.git
cd flipr_site
### 2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate 
###3️⃣ Install Dependencies
pip install django pillow
###4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
###5️⃣ Create Admin User
python manage.py createsuperuser
###6️⃣ Run the Server
python manage.py runserver
Open browser:http://127.0.0.1:8000/


---
📁 Models Documentation
Project Model
| Field       | Type                      |
| ----------- | ------------------------- |
| image       | ImageField (auto-cropped) |
| name        | CharField                 |
| description | TextField                 |


Client Model
| Field       | Type                      |
| ----------- | ------------------------- |
| image       | ImageField (auto-cropped) |
| name        | CharField                 |
| designation | CharField                 |
| description | TextField                 |

Contact Model
| Field     | Type        |
|-----------|-------------|
| full_name | CharField   |
| email     | EmailField  |
| mobile    | CharField   |
| city      | CharField   |

Subscriber Model
| Field | Type       |
|-------|------------|
| email | EmailField |

-------
🛠 View Logic

Landing page fetches:

projects = Project.objects.all()
clients = Client.objects.all()

and sends context to template:

return render(request, "landing.html", {
    "projects": projects,
    "clients": clients
})

--------------------
🖼 Image Auto-Cropping Logic

Images are processed on save() using Pillow:

Crop to maintain aspect ratio

Resize to 450×350

Save in /media/projects or /media/clients


-------------------------
🚀 Deployment Guide
🔹 Backend (Django)

Use platforms:
Render (recommended)
Steps on Render:
Create new web service
Add repo
Environment variables:
PYTHON_VERSION=3.10
Start command:
gunicorn flipr_consultancy_site.wsgi
Add Static/Media config (Render automatically handles)
----------------------------
🎨 Frontend Deployment (Vercel)
⚠ Django templates cannot run on Vercel.
Vercel supports only static frontend.
Steps:
Create /frontend/ folder with index.html
Remove Django template tags:
{{ p.image.url }}
{% for ... %}
{% csrf_token %}
Push to GitHub
Create Vercel project
Build command: (leave empty)
Output directory: .
Your static landing page will go live.
------------------------
🧪 API Endpoints (optional extension)

You can expose data using DRF:

/api/projects/
/api/clients/
/api/contacts/
/api/subscribers/
----------------------------
💡 Future Enhancements
Add authentication
Add fully functional project detail pages
Integrate email notifications
Make newsletter double opt-in
Add user dashboard
_____________________________________________________________________________________
👨‍💻 Developer
Amit Yadav
Flipr Consultancy Project 2025
