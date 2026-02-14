# Tkinter CI/CD Demo 🚀

This repository demonstrates how to automatically build a Windows `.exe` file 
for a Python Tkinter application using GitHub Actions.  

The purpose of this project is to learn CI/CD concepts for Python-based desktop applications.

---

## 📌 Project Overview

This project contains:

- A simple Tkinter calculator app (`main.py`)
- PyInstaller for packaging the app into a Windows executable
- GitHub Actions workflow to automate the build process

---

## 🛠 Technologies Used

- Python 3.12
- Tkinter (GUI)
- PyInstaller (Packaging)
- GitHub Actions (CI/CD)

---

## ⚙️ How It Works

When code is pushed to the `main` branch:

1. GitHub Actions starts a Windows virtual machine.
2. Python is installed.
3. Dependencies from `requirements.txt` are installed.
4. PyInstaller builds the `.exe` file.
5. The executable is uploaded as a build artifact.

No manual `.exe` creation is required.

---

## 📂 Project Structure

Github-Action-Python-exe/
├── src/
    └──main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .github/
    └── workflows/
        └── build.yml

## 🚀 How to Trigger the Build

Push changes to the `main` branch:

```bash
git add .
git commit -m "Trigger CI build"
git push origin main
```

The workflow will automatically run and create the .exe.

## 📥 How to Download the EXE

Go to the Actions tab in your GitHub repository.

Click the latest workflow run.

Scroll to the Artifacts section.

Download windows-exe.

Extract the zip file.

Run main.exe.

📦 requirements.txt

pyinstaller

## 🎯 What This Project Demonstrates

CI/CD pipeline setup for Python desktop apps

Automated Windows builds with PyInstaller

Artifact upload in GitHub Actions

Reproducible build environments

Clean repository practices using .gitignore

## 🧠 Learning Outcome
This project helps understand:

How GitHub Actions works

How CI runners operate

How desktop applications can be built automatically

How real-world software teams automate packaging and delivery

## 📜 License
This project is for educational purposes.
