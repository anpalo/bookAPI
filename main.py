from flask import Flask, request, jsonify, send_file
import psycopg2
import os
from werkzeug.utils import secure_filename



# cursor.execute(): Executes a SQL query.
# cursor.fetchall(): Retrieves all rows from the result of the query.
# cursor.fetchone(): Retrieves a single row from the result.

app = Flask(__name__)



app.config['UPLOAD_FOLDER'] = '/home/USER/Documents/bookLibrary'

def get_db_connection():
    conn = psycopg2.connect(
        dbname='books',
        user='USER',
        password='PASSWORD',
        host='localhost'
    )
    return conn

def create_book_table():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS library ('
                'id BIGSERIAL NOT NULL PRIMARY KEY,'
                'name VARCHAR(100) UNIQUE NOT NULL,'
                'author VARCHAR(100),'
                'genre VARCHAR(50),'
                'path VARCHAR(200));')
    conn.commit()
    cur.close()
    conn.close()



@app.route("/books", methods=["GET"])
def get_book_list():
    conn = get_db_connection() # connect to database
    cur = conn.cursor() # to let SQL interact with database

    try:
        cur.execute('SELECT id, name, author, genre, path FROM library')
        books = cur.fetchall()
        book_list = [
            {"id": book[0],
             "name": book[1],
             "author": book[2],
             "genre": book[3],
             "path": book[4]}
            for book in books
        ]
        return jsonify({"books": book_list})
    except Exception as e:
        error_message = "Failed to get book data. Please try again later."
        return jsonify({"error": "Internal server error", "message": error_message, "details": str(e)}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/books/<int:id>", methods=['GET'])
def get_book_PDF(id):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute('SELECT path FROM library WHERE id = %s', (id, ))
        book = cur.fetchone()

        if not book or not book[0]:
            return jsonify({"error": "Not Found", "message": "Book not found or file not available"}), 404

        file_path = book[0]
        if not os.path.exists(file_path):
            return jsonify({"error": "File Not Found", "message": "File Path Invalid"}), 404

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        error_message = "Failed to get book's download data. Please try again later."
        return jsonify({"error": "Internal server error", "message": error_message, "details": str(e)}), 500
    finally:
        cur.close()
        conn.close()



if __name__ == "__main__":
    create_book_table()  # Ensure the table is created before starting the app
    app.run(debug=True)