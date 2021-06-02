# Functions

## Admin
- Can add or remove Librarian.
- View and Edit Student records.

## Librarian
- Login and edit their account information.
- Can Add, View, Book.
- Can Issue Book (added by Admin) to registered student.
- Can view Issued book with issued date and expiry date.
- Can view Fine (10 rupees for each day after expiry date).
- Can View Students that are registered into system.
- Can View resqut form students for new books.

## Student
- Create account and Login.
- Can view their issued book with expiry date and fine(if there any otherwise 0)
- Can put their request for new books in the Request Portal.

# HOW TO RUN THIS PROJECT

- Install Python(3.8.0) (Dont Forget to select Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```bash
python -m pip install -r requirements. txt
```
- Download This Project Zip Folder and Extract it
.Move to project folder in Terminal. Then run following Commands :
```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```bash
http://127.0.0.1:8000/
```
