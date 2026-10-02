# Django Portfolio Project

This Django portfolio project includes a public portfolio experience, a superuser-only admin dashboard, and a clean project/tech-stack management flow for the owner.

## Features

- Public portfolio pages for home, about, project list, and project detail.
- Dedicated superuser-only sign-in page.
- User registration page for creating standard user accounts.
- Secure dashboard at `/dashboard/` for admin-only management.
- Project listing and tech-stack listing in table format.
- Project creation form for authenticated admin users.
- Tech stack creation form for authenticated admin users.
- Reusable `TechStack` model so one technology can be shared across multiple projects.
- Environment-variable configuration for local secrets and debug settings.
- Clean clone setup with `.gitignore` and `.env.example` support.

## Project Models

- `Project`
  - `project_name`
  - `description`
  - `tech_stacks` (many-to-many with `TechStack`)
  - `link`
- `TechStack`
  - `name`
  - `created_at`
- `PersonalInformation`
- `Testimony`
- `Inquiry`

## Key Routes

- `/` - Home page
- `/about/` - About page
- `/projects/` - Public project list
- `/projects/<id>/` - Public project detail
- `/login/` - Superuser-only sign in page
- `/register/` - Standard user registration page
- `/dashboard/` - Admin dashboard with project and tech-stack tables
- `/dashboard/projects/` - Project list table
- `/dashboard/projects/create/` - Create a project
- `/dashboard/tech-stacks/` - Tech stack table
- `/dashboard/tech-stacks/create/` - Create a tech stack
- `/contact/` - Inquiry form
- `/testimonies/` - Testimony list

## Fresh Clone Setup

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the project dependencies:

```bash
pip install django
```

4. Copy the example environment file and update values:

```bash
copy .env.example .env
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open the app:

```text
http://127.0.0.1:8000/
```

## Environment Variables

The project expects these values in a local `.env` file (not committed to Git):

```env
DJANGO_SECRET_KEY=replace-with-your-secret-key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
```

The file `.env.example` is included as a template without exposing any real credentials. For deployment, set a strong production secret key and the correct deployed host names.

## Deployment Checklist

Before deployment, make sure you have:

- a real `DJANGO_SECRET_KEY`
- `DEBUG=False`
- the correct production `ALLOWED_HOSTS`
- a proper database configuration for the deployment environment
- static files collected for production if needed
- a superuser account created in the deployed environment

> Ask me for your production secret key and deployment host values if you want me to wire them in for your hosting platform.

## Admin Login

- Access the superuser sign-in page at `/login/`.
- Only a Django superuser account may log in here.
- Successful login redirects to `/dashboard/`.
- Non-superusers are blocked even if they have an existing account.

## Notes

- The repository intentionally does not include `db.sqlite3` or `.venv`.
- Run `python manage.py migrate` after a fresh clone before starting the project.
- The project uses Django templates and a simple internal CSS setup for a beginner-friendly portfolio.
