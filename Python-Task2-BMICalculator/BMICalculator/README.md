# Password Generator -- Python Programming Internship

**Project:** Task 3 -- Password Generator

## 1. Project Overview

A Python-based Password Generator developed with Tkinter. The
application allows the user to specify a password length, generates a
random password containing letters, numbers, and special characters, and
provides a button to copy the generated password to the clipboard.

## 2. Features

-   Tkinter graphical user interface.
-   Password length input field.
-   Minimum password length of 8 characters.
-   Random password generation.
-   Combination of uppercase and lowercase letters.
-   Inclusion of numbers.
-   Inclusion of special characters.
-   Display of the generated password.
-   Copy Password button for copying the generated password to the
    clipboard.
-   Validation for invalid or non-numeric password length.

## 3. Technologies Used

-   Python
-   Tkinter
-   `random` module
-   `string` module
-   VS Code
-   Git and GitHub

## 4. Character Set

The password is generated using:

``` python
string.ascii_letters + string.digits + "!@#$%^&*"
```

## 5. Project Structure

``` text
PasswordGenerator/
├── Password_Generator.py
└── README.md
```

## 6. How to Run

1.  Install Python.
2.  Open `Password_Generator.py` in VS Code.
3.  Run the program.
4.  Enter a password length of at least 8.
5.  Click **Generate Password**.
6.  Click **Copy Password** to copy the generated password to the
    clipboard.

## 7. Input Validation

The application checks that:

-   The password length is a valid number.
-   The password length is at least 8 characters.
-   A password is generated before the user attempts to copy it.

## 8. Internship Submission

This Password Generator is Task 3 of the Python Programming Internship
project work.

## 9. Author

**Hailu Taye**

Python Programming Internship -- OASIS INFOBYTE
