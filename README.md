# Django Portfolio Project

This is a student portfolio website built with Django for Quiz 1 and Quiz 2. The project now uses database models for personal information and project entries, with function-based views and HTML templates.

## Features

- `Project` model with:
  - `project_name`
  - `description`
  - `tech_stack`
  - `link`
- `PersonalInformation` model with:
  - `first_name`
  - `middle_name`
  - `last_name`
  - `summary`
  - `contact_number`
  - `email`
  - `address`
- Project list view (`/projects/`) showing only project titles
- Project detail view (`/projects/<id>/`) showing full project details
- Personal information view (`/personal-information/`) returning profile details
- Home, about, and contact pages now render backend data where appropriate
- Django admin support for managing projects and personal information

## How to run the project

1. Open a terminal in the project folder.
2. Make sure Python is installed.
3. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install Django if not already installed:

```bash
pip install django
```

5. Create or update the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. (Optional) Create a Django superuser to access the admin:

```bash
python manage.py createsuperuser
```

7. Run the Django development server:

```bash
python manage.py runserver
```

8. Open a browser and go to:

```text
http://127.0.0.1:8000/
```

## Admin

- Admin site: `http://127.0.0.1:8000/admin/`
- Manage `Project` and `PersonalInformation` from Django admin

## Notes

- The personal information and project content are stored in the database.
- The project list page shows only titles, with detail pages for the full project data.
- The contact form is still static and does not send messages.
