# BookWorm

BookWorm is a web application for managing and sharing books. Users can create an account, add books to their personal library, and browse and search for books added by other users.

## Features

- User Registration: Users can create a new account by providing their email and password.

- User Login: Registered users can log in to their accounts using their credentials.

- Profile Page: Each user has a profile page where they can view and manage their personal library of books.

- Add Books: Users can add books to their library by providing the book title, author, and other details.

- Search Books: Users can search for books by title, author, or any other relevant information.

## Technologies Used

- [![Django](https://img.shields.io/badge/Django-3.2-blue)](https://www.djangoproject.com/)  The web application is built using the Django web framework, which provides a robust foundation for creating web applications.

- [![SQLite](https://img.shields.io/badge/SQLite-3-green)](https://www.sqlite.org/index.html)  The project uses SQLite as the default database for storing user and book data.

- [![HTML/CSS](https://img.shields.io/badge/HTML%2FCSS-5%2F3-orange)](https://developer.mozilla.org/en-US/docs/Web/HTML)  The user interface is built using HTML and CSS for styling and layout.

## Setup

### 1. Clone the repository:
   ```console
   foo@bar:~$ git clone https://github.com/Apersant1/BookWorm.git
   ```
### 2. Create a virtual environment:
   ```console
   foo@bar:~$ python -m venv myenv
   ```


### 3. Activate the virtual environment:

   - For Windows:
     
   ```console
   \myenv\Scripts\activate
   ``` 

  
   - For macOS/Linux:
     
   ```console
   source myenv/bin/activate
   ``` 
     
     
     
### 4. Install the dependencies:
  ```console
  pip install -r requirements.txt
  ``` 
    
   
   
   
### 5. Apply database migrations:
  ```console
  python manage.py migrate
  ``` 
   
   
### 6. Start the development server:
  ```console
  python manage.py runserver
  ``` 

   
### 7. Open your web browser and visit `http://localhost:8000` to access the BookWorm application.

## Contributing

Contributions are welcome! If you'd like to contribute to BookWorm, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository.

5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more information.

