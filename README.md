# Ahmed Sayed License Activation System + Snake Game

## 📌 Project Overview

This project is a **Desktop License Activation System** built using **Python**.
The program simulates how commercial software uses **activation keys (license keys)** to unlock features.

When a user enters a valid activation key, the system verifies it with a **server API** connected to a **database**.
If the key is valid, the program unlocks and launches a **Snake Game**.

This project demonstrates concepts used in real software products such as:

* License key validation
* Client–Server communication
* API verification
* Desktop GUI applications
* Game integration

---

# 🧠 How the System Works

The system is composed of three main parts:

1️⃣ Desktop Application
2️⃣ Server API
3️⃣ Database

Flow:

User enters License Key
↓
Desktop App sends request to Server
↓
Server checks key in Database
↓
If valid → program unlocks
↓
Snake Game launches

---

# 🖥 Desktop Application

Built using:

* Python
* Tkinter (GUI)
* Requests (HTTP communication)

Features:

* License Key input
* Server validation
* Error handling
* Social links buttons
* Launches the Snake Game after activation

---

# 🌐 Server Side

The server is built using:

* PHP
* MySQL Database
* XAMPP environment

The server receives the activation key and checks if it exists in the database and if it has already been used.

If valid:

* The key is marked as **used**
* Activation response is sent back

---

# 🗄 Database Structure

Database name:

licenses

Table:

license_keys

Columns:

* id
* license_key
* used

Example keys:

AHMED-1111
AHMED-2222
AHMED-3333

Each key can only be used **once**.

---

# 🎮 Snake Game

After successful activation, the program launches a simple **Snake Game** built using Python.

Controls:

W → Up
S → Down
A → Left
D → Right

Game Features:

* Food generation
* Snake growth
* Continuous movement
* Simple collision mechanics

---

# ⚙ Installation Guide

## 1 Install Python

Download Python and install it.

## 2 Install Required Libraries

Open terminal and run:

pip install requests

---

## 3 Setup the Server

Install:

XAMPP

Start:

Apache
MySQL

---

## 4 Add the Server Files

Move the folder:

server

Into:

C:\xampp\htdocs

Rename it to:

license_server

---

## 5 Import Database

Open in browser:

http://localhost/phpmyadmin

Import the file:

database.sql

---

## 6 Run the Application

Navigate to:

desktop_client

Run:

python app.py

---

# 🔑 Test Activation Keys

Use one of the following keys:

AHMED-1111
AHMED-2222
AHMED-3333

Each key will work **only once**.

---

# 📦 Converting to EXE

To convert the program into a Windows executable:

Install:

pip install pyinstaller

Run:

pyinstaller --onefile app.py

The executable will appear in:

dist/app.exe

---

# 🚀 Future Improvements

Possible improvements for the system:

* Encrypted license keys
* Online server hosting
* Expiration-based licenses
* Advanced GUI design
* Anti-tampering protection
* Automatic updates

---

# 👨‍💻 Author

Ahmed Sayed

Software Developer
This project demonstrates a basic **software licensing system** used in commercial desktop applications.

GitHub Project by Ahmed Sayed
