# 🎓 TPO Placement Portal

## 📌 Overview

The **TPO Placement Portal** is a Django-based web application designed to streamline the placement process for students, faculty, and Training & Placement Officers (TPO). It provides role-based access, student filtering, job application tracking, and company management features.

## 🚀 Features

### 🔹 **TPO Dashboard**

- **Faculty Management**: Add, view, and manage faculty profiles.
- **Student Management**: Filter students, export data, and update eligibility.
- **Eligible Rounds Data**: Upload and update student interview round results.
- **Drive Details**: Manage company listings, send emails & notifications.
- **Company Process**: Add & edit companies and their hiring process.
- **Student Training**: Upload & manage training data via Excel.
- **Offer Letters**: View & manage uploaded student offer letters.
- **Notifications**: Send and track placement updates.
- **Logout**: Secure session termination.

### 🔹 **Faculty Dashboard**

- **Profile Management**: Edit own profile (cannot delete own account).
- **View Faculty**: See faculty details.
- **Student & Placement View**: Track department-wise student progress.

### 🔹 **Student Dashboard**

- **Profile Completion**: Mandatory before placement application.
- **Placement Eligibility Check**: Verify application eligibility.
- **Resume & Course Recommendations**: Improve placement chances.
- **Job Applications**: Apply for jobs via notifications.
- **Upload Offer Letter**: Submit placement proof.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL / MySQL
- **External Services**: SMTP (Email), Google Custom Search API

## 🏗️ Installation & Setup

1. **Create a virtual environment**

   ```sh
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows use: venv\Scripts\activate

   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt

   ```

3. **Run migrations**

   ```sh
   python manage.py migrate

   ```

4. **Start the server**

   ```sh
   python manage.py runserver

   ```

5. **Access the portal at http://127.0.0.1:8000/**
