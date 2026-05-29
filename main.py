from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import sqlite3

app = FastAPI()

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MODELS ----------------

class RegisterData(BaseModel):
    name: str
    email: str
    password: str
    role: str


class LoginData(BaseModel):
    email: str
    password: str


class AttendanceData(BaseModel):
    student_name: str
    date: str
    status: str


class HomeworkData(BaseModel):
    subject: str
    title: str
    description: str
    due_date: str


class NotesData(BaseModel):
    subject: str
    topic: str
    content: str


class AnnouncementData(BaseModel):
    title: str
    message: str


class FeesData(BaseModel):
    student_name: str
    amount: str
    status: str


# ---------------- HOME ----------------

@app.get("/")
def home():

    return {
        "message": "Smart School OS Running 🚀"
    }


# ---------------- REGISTER ----------------

@app.post("/register")
def register(data: RegisterData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)
        """,
        (data.name, data.email, data.password, data.role)
    )

    conn.commit()

    conn.close()

    return {
        "message": "User Registered Successfully 🚀"
    }


# ---------------- LOGIN ----------------

@app.post("/login")
def login(data: LoginData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (data.email, data.password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        return {
            "status": "success",
            "message": f"Welcome {user[1]} 🚀",
            "role": user[4]
        }

    else:

        return {
            "status": "error",
            "message": "Invalid Email or Password ❌"
        }


# ---------------- USERS ----------------

@app.get("/users")
def get_users():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    conn.close()

    return {
        "users": users
    }


# ---------------- ATTENDANCE ----------------

@app.post("/attendance")
def mark_attendance(data: AttendanceData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attendance
        (student_name, date, status)

        VALUES (?, ?, ?)
        """,
        (
            data.student_name,
            data.date,
            data.status
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "Attendance Marked Successfully 🚀"
    }


# ---------------- ALL ATTENDANCE ----------------

@app.get("/all-attendance")
def get_attendance():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    rows = cursor.fetchall()

    conn.close()

    return {
        "attendance": rows
    }


# ---------------- HOMEWORK ----------------

@app.post("/add-homework")
def add_homework(data: HomeworkData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO homework
        (subject, title, description, due_date)

        VALUES (?, ?, ?, ?)
        """,
        (
            data.subject,
            data.title,
            data.description,
            data.due_date
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "Homework Added Successfully 🚀"
    }


# ---------------- ALL HOMEWORK ----------------

@app.get("/all-homework")
def get_homework():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM homework")

    rows = cursor.fetchall()

    conn.close()

    return {
        "homework": rows
    }


# ---------------- NOTES ----------------

@app.post("/add-notes")
def add_notes(data: NotesData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO notes
        (subject, topic, content)

        VALUES (?, ?, ?)
        """,
        (
            data.subject,
            data.topic,
            data.content
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "Notes Added Successfully 🚀"
    }


# ---------------- ALL NOTES ----------------

@app.get("/all-notes")
def get_notes():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")

    rows = cursor.fetchall()

    conn.close()

    return {
        "notes": rows
    }


# ---------------- ANNOUNCEMENT ----------------

@app.post("/add-announcement")
def add_announcement(data: AnnouncementData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO announcements
        (title, message)

        VALUES (?, ?)
        """,
        (
            data.title,
            data.message
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "Announcement Added 🚀"
    }


# ---------------- ALL ANNOUNCEMENTS ----------------

@app.get("/all-announcements")
def get_announcements():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM announcements")

    rows = cursor.fetchall()

    conn.close()

    return {
        "announcements": rows
    }


# ---------------- ADD FEES ----------------

@app.post("/add-fees")
def add_fees(data: FeesData):

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO fees
        (student_name, amount, status)

        VALUES (?, ?, ?)
        """,
        (
            data.student_name,
            data.amount,
            data.status
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "Fees Added Successfully 🚀"
    }


# ---------------- ALL FEES ----------------

@app.get("/all-fees")
def get_fees():

    conn = sqlite3.connect("school.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM fees")

    rows = cursor.fetchall()

    conn.close()

    return {
        "fees": rows
    }