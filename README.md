# Personal Book Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

## Description

Personal Book Manager is a simple book management program built with Python. It allows users to add multiple books, display their book lists, and save their books in a JSON file so they can access them again later.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Run the Program](#run-the-program)
- [Usage](#usage)
- [Author](#author)

## Features

- Add multiple books.
- Display all saved books.
- Save books in a JSON file.
- Load previously saved books.
- Keep old books when adding new books.

## Requirements

- Python
- python-dotenv

**Note:** `os` and `json` are built-in Python modules and do not need to be installed separately.

## Project Structure

```text
Personal_Book_Manager/
│
├── main.py
├── books.py
├── books.json
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

First, clone the repository:

```bash
git clone YOUR_REPOSITORY_LINK
```

Open the project folder:

```bash
cd Personal_Book_Manager
```

Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Environment Setup

1. Create a file named `.env` inside the project folder.
2. The `.env.example` file is only a template.
3. Open `.env.example` to see which Environment Variable is required.

The required variable is:

`BOOK_MANAGER_ADMIN_PASSWORD`

Add the following content to your `.env` file:

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own password.

**Important:**

- Never upload your `.env` file to GitHub.
- Upload `.env.example` to GitHub.
- Make sure `.env` is included in your `.gitignore` file.

## Run the Program

The main file of this project is `main.py`.

Run the program using:

```bash
python main.py
```

## Usage

1. Enter your name.
2. Choose how many books you want to add.
3. Enter the names of your books.
4. View your saved books.

All books are stored in `books.json` and loaded again when you run the program.

