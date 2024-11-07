# db.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Establish a database connection"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="contact_manager"
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def init_db():
    """Initialize the database with the contacts table"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(255) NOT NULL,
                                phone VARCHAR(50),
                                email VARCHAR(255)
                              )''')
            conn.commit()
            print("Database initialized.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

def insert_contact(name, phone, email):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        conn.commit()
        conn.close()

def fetch_contacts():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        conn.close()
        return rows

def update_contact(contact_id, name, phone, email):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, contact_id))
        conn.commit()
        conn.close()

def delete_contact(contact_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        conn.commit()
        conn.close()
