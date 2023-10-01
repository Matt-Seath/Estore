# Estore

Estore is a Django-based e-store backend web application with a modular architecture. It leverages SQL and Django ORM, includes an admin page, provides a REST API for seamless frontend integration, utilizes Django's authentication system, supports file uploading for products, enables custom SMTP server for email notifications, employs Redis for automating background tasks, implements automated testing, caching, and logging.

## Features

- **Modular Architecture**: Estore is designed with a modular architecture for easy extension and customization.

- **SQL and Django ORM**: Utilizes SQL databases with Django's powerful Object-Relational Mapping.

- **Admin Page**: Comes with an admin interface for managing products, orders, and users.

- **REST API**: Provides a RESTful API for seamless integration with frontend applications.

- **Django Authentication**: Utilizes Django's built-in authentication system for user management.

- **File Uploads**: Supports file uploading for product images and other media.

- **Custom SMTP Server**: Enables sending emails using a custom SMTP server for notifications.

- **Redis for Background Tasks**: Utilizes Redis to automate background tasks and improve performance.

- **Automated Testing**: Includes automated tests to ensure code reliability and functionality.

- **Caching**: Implements caching to optimize performance and reduce database queries.

- **Logging**: Provides logging for tracking and debugging purposes.

## Getting Started

To run Estore on your local machine, follow these steps:

1. Clone this repository to your local environment.
2. Set up your virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure your database settings in `settings.py`.
5. Apply migrations with `python manage.py migrate`.
6. Create a superuser account with `python manage.py createsuperuser`.
7. Start the development server with `python manage.py runserver`.
8. Access the admin interface at `http://localhost:8000/admin/` and log in with your superuser credentials.

## Usage

Estore provides a comprehensive set of APIs and interfaces for managing products, orders, and users. You can integrate these functionalities into your frontend application using the provided REST API. For detailed API documentation, refer to the [API Documentation](docs/api.md).

## Contributing

We welcome contributions to enhance and extend the functionality of Estore. To contribute, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your branch to your forked repository.
5. Open a pull request with a detailed description of your changes.

## License

Estore is released under the [MIT License](LICENSE).
