# Book API
This API is accessible at quill.bevans.com

A simple API to manage and download books stored on a server. This API allows you to fetch details of the books in the library and download them as PDFs.

## Features

- **GET /books**: Retrieve a list of books with details like name, author, genre, and file path.
- **GET /books/{id}**: Download a book (PDF) by specifying its ID.

## Setup and Installation

To get started with this API, follow these instructions:

1. Clone the repository:

    ```bash
    git clone https://github.com/anpalo/bookAPI.git
    cd bookAPI
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv bookAPI-env
    source bookAPI-env/bin/activate  # On Windows, use bookAPI-env\Scripts\activate
    ```

3. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure your PostgreSQL database by creating the necessary table (the script will do this automatically when the app runs).

5. Run the application:

    ```bash
    python main.py
    ```

## Changes Made

### POST Method Removed

For security reasons, the POST method for adding new books and uploading files has been **removed**. It was initially included for ease of book uploads, but due to potential security vulnerabilities, this functionality has been disabled. The API now only supports retrieving book data and downloading books by ID.

## Environment Variables

- `UPLOAD_FOLDER`: Path where uploaded books should be stored.
  
- Database Configuration
The application uses a PostgreSQL database to store and manage book data. The database connection is configured via environment variables:
DB_NAME: The name of the PostgreSQL database (e.g., books).
DB_USER: The database username (e.g., myuser).
DB_PASSWORD: The password for the database user (e.g., mypassword).
DB_HOST: The host of the PostgreSQL database (default is localhost).

