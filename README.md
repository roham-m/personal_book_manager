# Personal Book Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

## Description

Personal Book Manager is a simple book management program built with Python. It allows users to add multiple books, display their book lists, save their books in a JSON file, and access them again later. It also includes an Admin Mode with password protection.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Run the Program](#run-the-program)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Features

- Add multiple books.
- Display all saved books.
- Save books in a JSON file.
- Load previously saved books.
- Keep old books when adding new books.
- Admin Mode with password protection.

## How It Works

1. The program starts by asking the user for their name.
2. It loads previously saved books from `books.json`.
3. The program welcomes the user to the Personal Book Manager.
4. The user can choose whether to enter Admin Mode.
5. If the user chooses Admin Mode, the program asks for an admin password.
6. If the password is correct, Admin Mode is activated. Otherwise, an error message is displayed.
7. The user chooses how many new books they want to add.
8. The program asks for the name of each book and adds it to the book list.
9. All books, including previously saved books and new books, are displayed.
10. The complete book list is saved in `books.json` for future use.

## Requirements

- Python
- python-dotenv

**Note:** `os` and `json` are built-in Python modules and do not need to be installed separately.

## Project Structure

```text id="4v7p2h"
Personal_Book_Manager/
│
├── main.py             # Main file that runs the program
├── books.py            # Contains functions for managing books
├── books.json          # Stores all saved books
├── requirements.txt    # Contains required Python packages
├── .env.example        # Template for required environment variables
├── .gitignore          # Prevents sensitive and unnecessary files from being uploaded
├── images/             # Stores project screenshots and images
└── README.md           # Project documentation
```

## Installation

First, clone the repository:

```bash id="k8p2jd"
git clone YOUR_REPOSITORY_LINK
```

Open the project folder:

```bash id="j4m8qp"
cd Personal_Book_Manager
```

Install the required packages using `requirements.txt`:

```bash id="p2n6wt"
pip install -r requirements.txt
```

## Environment Setup

1. Create a file named `.env` inside the project folder.
2. The `.env.example` file is only a template.
3. Open `.env.example` to see which Environment Variable is required.

The required variable is:

`admin_pass`

Add the following content to your `.env` file:

```env id="r7m3vx"
admin_pass=your_password_here
```

Replace `your_password_here` with your own password.

**Important:**

- Never upload your `.env` file to GitHub.
- Upload `.env.example` to GitHub.
- Make sure `.env` is included in your `.gitignore` file.

## Run the Program

The main file of this project is `main.py`.

Run the program using:

```bash id="z5q9nb"
python main.py
```

## Usage

1. Enter your name.
2. Choose whether to enter Admin Mode.
3. Enter the admin password if requested.
4. Choose how many books you want to add.
5. Enter the names of your books.
6. View your saved books.

All books are stored in `books.json` and loaded again when you run the program.

## Troubleshooting

### 1. FileNotFoundError

**What does it mean?**

Python cannot find the file it is trying to open.

**Why can it happen?**

The `books.json` file may not exist, or the program may be running from the wrong folder.

**What should I check first?**

Make sure you are running `main.py` from the project folder and check the file path.

### 2. JSONDecodeError

**What does it mean?**

Python cannot read the data inside `books.json`.

**Why can it happen?**

The JSON file may be empty or contain incorrect data.

**What should I check first?**

Open `books.json` and check whether its contents are valid JSON. For an empty book list, use `[]`.

### 3. ModuleNotFoundError: No module named 'dotenv'

**What does it mean?**

Python cannot find the `python-dotenv` package.

**Why can it happen?**

The package may not be installed in your Python environment.

**What should I check first?**

Run the following command in your terminal:

```bash id="m8v2kc"
pip install -r requirements.txt
```

### 4. Admin Password Not Working

**What does it mean?**

The program does not recognize the admin password.

**Why can it happen?**

The `.env` file may be missing, the password may be incorrect, or `load_dotenv()` may not have been called.

**What should I check first?**

- Make sure `.env` exists in the project folder.
- Check that the variable name is exactly `admin_pass`.
- Make sure `load_dotenv()` runs before `os.getenv("admin_pass")`.
- Check that the password in `.env` is correct.

## Author

Roham Mirzaei