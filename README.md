# user-management-cli

A command-line user management system built in Python to learn Object-Oriented Programming concepts.

## What it does

- Register and login as User or Admin via CLI
- Role-based dashboards with different permissions
- Admin can view all users and reset passwords
- Data persists across sessions via JSON storage

## How to run

```bash
git clone https://github.com/yourusername/user-management-cli
cd user-management-cli
python main.py
```

No external dependencies. Pure Python.

## Project structure

```
├── main.py          # Entry point, loads JSON data on startup
├── system.py        # Core app logic, manages all runtime state
├── user.py          # User class with encapsulated password handling
├── admin.py         # Admin class, inherits from User
├── utilities.py     # Helper functions (colored print etc.)
└── data/
    ├── user.json    # Persisted user records
    └── admin.json   # Persisted admin records
```

## OOP concepts practiced

- **Encapsulation** — password stored as private (`__password`), never exposed directly
- **Inheritance** — Admin extends User, inherits auth logic
- **Polymorphism** — Admin and User have separate dashboard/profile implementations
- **Factory pattern** — JSON dicts converted to class instances on load, back to dicts on exit
- **Static methods** — utility operations that don't depend on instance state

## Known gaps 

- No input validation — empty strings and bad emails are accepted
- Passwords stored as plaintext — would use hashing in a real system
- Linear search for login — not scalable beyond small datasets
- No error handling for malformed JSON

## Why I built this

This project was developed as a hands-on exercise during my exploration of Object-Oriented Programming (OOP) in Python.
