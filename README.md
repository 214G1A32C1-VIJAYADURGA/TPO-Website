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


## 🚀 Setup Python 3.11 in GitHub Codespaces (Ubuntu 24.04)

### 1️⃣ Install Required System Dependencies

```bash
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev
```

---

### 2️⃣ Install pyenv

```bash
curl https://pyenv.run | bash
```

---

### 3️⃣ Configure pyenv

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

Verify installation:

```bash
pyenv --version
```

---

### 4️⃣ Install Python 3.11

```bash
pyenv install 3.11.9 (This will take a few minutes. Wait until you install python.)
```

---

### 5️⃣ Set Python 3.11 for Project

```bash
cd /workspaces/TPO-Website
pyenv local 3.11.9 
python --version
```

Expected Output:

```bash
Python 3.11.9
```

---

### 6️⃣ Create and Activate Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate
```

---

### 7️⃣ Install Project Dependencies

```bash
pip install django
pip install -r requirements.txt
pip install --upgrade httplib2
```

---

### 8️⃣ Run Migrations 

```bash
python manage.py migrate

```

### 9️⃣ Create Admin Credentials(For TPO, Admin Logins)
```bash
python manage.py createsuperuser

```

Or you can use existing credentials if you don’t want to create a new superuser.

```
Username: admin
password: 123456
```

### 🔟 Run Django Project
```bash
python manage.py runserver
```

## ✅ Notes

- GitHub Codespaces runs on Linux (Ubuntu), so activation uses:
  
  ```bash
  source myvenv/bin/activate
  ```

- Do NOT use:
  
  ```bash
  myvenv\Scripts\activate
  ```
  (That is for Windows local setup)

---
  

## 🔎 Prerequisites

Before starting the installation, make sure the following are installed:

### Check Python Version

Django works best with **Python 3.10+** (Recommended: **Python 3.11**)

```bash
python --version
```

or

```bash
python3 --version
```

Expected output:
```
Python 3.11.x
```

---

### Check pip Installation
pip is the package manager for Python and is required to install Django and other dependencies.

```bash
pip --version
```

or

```bash
python -m pip --version
```

If pip is not installed:
- Reinstall Python
- Make sure ✔ “Add Python to PATH” is selected
- Ensure ✔ “Install pip” option is enabled

---

## 🏗️ Installation & Setup
During the installation process check python version which supports Django usally 3.11 version needs to be installed and also check whether pip is installed or not during the python setup 
1. ## Clone the Repo
   ```sh
   git clone https://github.com/214G1A32C1-VIJAYADURGA/TPO-Website.git
   cd TPO-Website
   
   ```

2. **Create a virtual environment**

   ```sh
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows use: myvenv\Scripts\activate

   ```

3. **Install dependencies**

   ```sh
   pip install django
   pip install -r requirements.txt
   pip install --upgrade httplib2

   ```

4. **Run migrations**

   ```sh
   python manage.py migrate

   ```
   
5. **Create Superuser(Admin)**

   ```sh
   python manage.py createsuperuser

   ```

6. **Start the server**

   ```sh
   python manage.py runserver

   ```

5. **Access the portal at http://127.0.0.1:8000/**
