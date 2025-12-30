# Student Information Portal

A simple **Full Stack Web Application** built using **Python** and **Flask**, designed to manage student information through a web interface.  
This project demonstrates backend logic, data handling, routing, template rendering, and object-oriented design — similar to real-world full stack development principles.

---

## 🚀 Project Overview

The **Student Information Portal** allows users to:

- Add new student records
- View all existing records
- Search for a student by roll number  
  All student data is stored in a **JSON file**, ensuring easy data management and persistence.

---

## 🧩 Features

### 🧠 Backend Logic (Python)

- **Data Handling & File Management**

  - Stores student information (`name`, `roll_no`, `department`, `email`) in a JSON file.
  - Supports:
    - ➕ Add new record
    - 📋 Display all records
    - 🔍 Search record by roll number

- **Object-Oriented Design**

  - Implements a `Student` class with methods like `display_info()` and `update_email()`.
  - Demonstrates creation and manipulation of multiple student objects.

- **Exception Handling**
  - Uses `try-except` blocks to handle missing files or incorrect data formats gracefully.

---

### 🌐 Flask Web Application

- **Home Page (`/`)**

  - Displays a welcome message with navigation links:
    - ➕ _Add Student_
    - 👀 _View Students_

- **Add Student Page (`/add`)**

  - Contains a form for entering student details.
  - On submission, the data is validated and stored in `students.json`.

- **View Students Page (`/students`)**

  - Displays all student records in a neatly formatted HTML table using **Jinja2 templates**.

- **Bonus (Optional)**
  - Search student by roll number.
  - Display message **"Student not found"** for invalid roll numbers.

---

## 🗂 Folder Structure

```
student_portal/
│
├── app.py
├── students.json
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── students.html
│   └── search.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MeesamBukhari/FSD-A3-Student-Portal.git
cd FSD-A3-Student-Portal
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install required dependencies

```bash
pip install flask
```

### 5️⃣ Run the Flask application

```bash
python app.py
```

### 6️⃣ Open the application

Visit **http://127.0.0.1:5000/** in your browser.

---

## 🧰 Technologies Used

| Category             | Tools / Technologies                     |
| -------------------- | ---------------------------------------- |
| Backend              | Python, Flask                            |
| Frontend             | HTML, CSS, Jinja2                        |
| Data Storage         | JSON File                                |
| Programming Concepts | OOP, Exception Handling, File Management |

---

## 💡 Future Improvements

- Add edit/delete options for student records.
- Integrate database support (e.g., SQLite or PostgreSQL).
- Improve UI using Bootstrap or Tailwind CSS.
- Add user authentication.

---

## 👨‍💻 Author

**Meesam Bukhari**  
Front-End Developer | Freelancer | GitHub Services Expert  
📍 Pak-Austria Fachhochschule  
🌐 [GitHub Profile](https://github.com/MeesamBukhari)

---

## 📜 License

This project is created for educational purposes under the **MIT License**.  
Feel free to modify and use it for your learning or personal projects.

---

⭐ _If you found this project helpful, don’t forget to star the repo!_

