# ATTENDANCE-MANAGEMENT-SYSTEM
📘 Attendance Management System

This project is a simple Attendance Management System built using Python and PostgreSQL. It allows you to manage student records, mark daily attendance, view attendance history, and generate a summary of all students’ attendance.

🔧 Features

Add Student

Add new students to the system with a unique ID and name.

Mark Attendance

Record whether a student is present or absent for a specific date.

Uses datetime to automatically store the date of attendance.

View Attendance

View the attendance history of a specific student.

Displays each record with the date and status: ✅ Present / ❌ Absent.

Summary

Shows total number of present and absent days for each student.

Menu-driven Interface

User-friendly menu in the console for interacting with the system.

💻 Tech Stack

Python: Handles all logic for student management and attendance tracking.

PostgreSQL: Stores student data and attendance records in relational tables.

psycopg2: Python library to connect and interact with PostgreSQL databases.

🗄️ Database Schema
Table: student
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique ID for each student
name	TEXT NOT NULL	Name of the student
Table: attendance
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique ID for each attendance record
student_id	INT REFERENCES student(id)	Foreign key to student table
date	DATE NOT NULL	Date of attendance
status	BOOLEAN DEFAULT TRUE	TRUE if present, FALSE if absent
