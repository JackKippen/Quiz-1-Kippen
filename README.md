# Django Portfolio Project

This is a college portfolio website built with Django. It is designed as a student assignment, with a clean blue-and-white layout, internal template styles, and beginner-friendly code.

## Features

- Home page with a hero section, skills, featured projects, portfolio statistics, latest testimonial preview, and contact cards.
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
- `Testimony` model for visitor testimonials.
- `Inquiry` model with a contact form that saves inquiries to the database.
- Function-based views for home, about, projects, project detail, contact, personal information, testimony creation, and testimony detail.
- One class-based list view for testimonials as required by the assignment.
- Simple responsive layout using only HTML templates and internal CSS.
- No external CSS files, no JavaScript, and no frontend frameworks.

## Pages

- `/` - Home page
- `/about/` - About page
- `/projects/` - Projects list
- `/projects/<id>/` - Project detail
- `/testimonies/` - Testimony list
- `/testimonies/create/` - Leave a testimony
- `/contact/` - Inquiry/contact form
- `/personal-information/` - Profile details

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

5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. (Optional) Create a Django superuser:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Admin

- Admin site: `http://127.0.0.1:8000/admin/`
- Manage `Project`, `PersonalInformation`, `Testimony`, and `Inquiry` entries.

## Notes

- The website uses Django templates with internal `<style>` tags only.
- The contact form saves inquiries to the database via the `Inquiry` model.
- Testimonies can be created by visitors and viewed in the testimony list.
- The design is intentionally simple and student-friendly, not a premium professional template.
