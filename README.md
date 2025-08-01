﻿# task-manager-FASTapi

# Task Manager API with FastAPI

A beginner-friendly Task Manager REST API built using FastAPI.  
This project is designed to help one learn how to:

- Structure a FastAPI backend
- Perform CRUD operations
- Connect to a database (SQLite or PostgreSQL)
- Document APIs automatically
- Host the project on GitHub

---

## Features

- Create, Read, Update, Delete (CRUD) tasks
- FastAPI-powered automatic docs (`/docs`)
- Data validation using Pydantic
- Clean folder structure for scalability
- Fully version-controlled with Git & GitHub

---

## Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **Uvicorn** (development server)
- **Git & GitHub** for version control

-
## Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the server**

```bash
uvicorn app.main:app --reload
```

4. **Open API docs**

Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Contributing

Feel free to fork this repo, try new features, and create pull requests!

---

## Resources

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Pydantic Docs](https://docs.pydantic.dev/)
* [Uvicorn Docs](https://www.uvicorn.org/)
* [GitHub Docs](https://docs.github.com/en/get-started)

---

## License

This project is licensed under the MIT License.

