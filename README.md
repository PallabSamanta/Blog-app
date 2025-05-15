# 📝 AuthentiBlog

**AuthentiBlog** is a fully functional blog web application built with Django. It allows users to register, log in, create, update, and delete their blog posts. Users can also comment on posts, upload profile and blog images, and reset their passwords (with email setup). Each user has a dedicated profile page.

---

## 🚀 Features

- 🔐 User Authentication (Login, Register, Logout)
- 📄 Create, Update, and Delete Blog Posts
- 🧑‍💻 User Profile with Profile Picture
- 🖼️ Upload Images for Blog Posts (optional)
- 💬 Comment on Posts (only after login)
- 👍 Like on Posts (only after login)
- ⚠️ Post Deletion Warning: *"This action cannot be undone."*
- ❌ Default Profile Picture if none is uploaded
- 🔁 Password Reset Functionality (email setup required)
- 🌙 Clean UI with crispy-bootstrap5

---

## 🧰 Tech Stack

- **Backend:** Django 5.2.1  
- **Frontend:** Bootstrap 5 (via `django-crispy-forms`)  
- **Database:** SQLite (default, can be switched)  
- **Image Handling:** Pillow  
- **Environment Variables:** python-dotenv  

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/PallabSamanta/Blog-app
cd DjangoBlog
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up .env file

Create a .env file in your project folder and add the following:

```bash
EMAIL_USER = your-email@example.com
EMAIL_PASS = your-email-password    # NOT your Gmail password!
```

🔐 You must use an **App Password** — not your actual Gmail password.

Follow this guide:

👉 [https://support.google.com/accounts/answer/185833](https://support.google.com/accounts/answer/185833)

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## 📁 Project Structure

```
├── .env
├── .gitignore
├── accounts
│   ├── .gitignore
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── signals.py
│   ├── templates
│   │   ├── accounts
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   ├── password_reset.html
│   │   │   ├── password_reset_complete.html
│   │   │   ├── password_reset_confirm.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── profile.html
│   │   │   ├── register.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── blog
│   ├── .gitignore
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   ├── blog
│   │   │   ├── about.html
│   │   │   ├── add_comment_to_post.html
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── post_confirm_delete.html
│   │   │   ├── post_detail.html
│   │   │   ├── post_form.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── blog_project
│   ├── .gitignore
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── media
├── requirements.txt
```

---

## 👥 User Roles

- **Anonymous Users:** Can only view blog posts
- **Authenticated Users:** Can create, edit, delete their posts, comment, and manage profile

---

## 🛠️ Notes

- ✅ Blog posts can be published with or without an image

- 👤 Default profile picture shown if user doesn't upload one

- 🔒 You must be logged in to create posts or leave comments

- 📩 Password reset depends on working email configuration (check spam folder too)

---

## ✅ To Do

- <span style="background-color:rgb(255, 255, 255); width: 10px; height: 10px; display: inline-block;"></span> Improve password reset email delivery

-  <span style="background-color:rgb(255, 255, 255); width: 10px; height: 10px; display: inline-block;"></span> Add unit tests

-  <span style="background-color:rgb(255, 255, 255); width: 10px; height: 10px; display: inline-block;"></span> Add pagination and blog search

-  <span style="background-color:rgb(255, 255, 255); width: 10px; height: 10px; display: inline-block;"></span> Add tags or categories to posts

---

## 🖼️ Preview


<!-- <table>
  <tr>
    <td><img src="https://drive.google.com/file/d/1kT2FHyhwQC0qD5WhLHlNyCxB1jQHACLE/view?usp=sharing" alt="Screenshot 1" width="400"></td>
    <td><img src="https://drive.google.com/file/d/1z-9QGJQ___ziDVQElH3WsYf6f5_-1hbi/view?usp=sharing" alt="Screenshot 2" width="400"></td>
  </tr>
</table> -->

<table>
  <tr>
    <td><img src="https://drive.google.com/uc?export=view&id=180h95PDibV1Xk8m-7jWjUXz_nWOQmt5X" alt="Screenshot 1" width="400"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1FXkNyXt0TIkAZYgjzJgjQskT6Xt8aIfE" alt="Screenshot 2" width="400"></td>
  </tr>
</table>

<!-- <table>
  <tr>
    <td><img src="https://drive.google.com/file/d/1V4h7lNF5aD1qQXh1WHlVF7q1QQGTnT2T/view?usp=sharing" alt="Screenshot 1" width="400"></td>
    <td><img src="https://drive.google.com/file/d/14CbfOT0smvOoESxpAusD_q2pComEAjPu/view?usp=sharing" alt="Screenshot 2" width="400"></td>
  </tr>
</table> -->

<table>
  <tr>
    <td><img src="https://drive.google.com/uc?export=view&id=10d5jGF_jQvz3acxLl-m_aeenE-27Tr9N" alt="Screenshot 1" width="400"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1p-GqZRZzK3nDBqsDhStDFbqy9Lempbl0" alt="Screenshot 2" width="400"></td>
  </tr>
</table>


<!-- 
<table>
  <tr>
    <td><img src="https://drive.google.com/file/d/1r_O8ORwAwlQ0msMundR1_yNdGiErqG7s/view?usp=sharing" alt="Screenshot 1" width="400"></td>
    <td><img src="https://drive.google.com/file/d/1ProFUBcm8IyMFo4L8lkRC22z_8rqwVrC/view?usp=sharing" alt="Screenshot 2" width="400"></td>
  </tr>
</table> -->


<table>
  <tr>
    <td><img src="https://drive.google.com/uc?export=view&id=1wbiyw5YblkgX9N3XOBb_zdemvUzMSLLV" alt="Screenshot 1" width="400"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=11hql3jJgGSlIxKl3GcuqTsa92VuXmXO4" alt="Screenshot 2" width="400"></td>
  </tr>
</table>

