# SplitWise

SplitWise is a Django-based web application for managing expenses and group finances.

## Features

- Track expenses within groups
- Add users to groups and manage group memberships
- View expense history and summaries
- Generate reports for expense analysis

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment: `python -m venv env`.
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`.
6. Run migrations: `python manage.py migrate`.
7. Create a superuser: `python manage.py createsuperuser`.
8. Start the development server: `python manage.py runserver`.

## Usage

- Access the admin panel by navigating to `http://localhost:8000/admin` and log in with the superuser credentials.
- Create groups, add users, and manage expenses through the admin interface.
- Access the main application interface at `http://localhost:8000` to interact with the application.

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
