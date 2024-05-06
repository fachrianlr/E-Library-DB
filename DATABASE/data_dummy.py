import csv
import random
from datetime import timedelta

import psycopg2
from faker import Faker

fake = Faker()


# Generate dummy data for users
def generate_users(num_records):
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['user_id', 'user_name', 'password', 'full_name', 'email', 'contact_info', 'dob']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(num_records):
            writer.writerow({
                'user_id': i + 1,
                'user_name': fake.user_name(),
                'password': fake.password(),
                'full_name': fake.name(),
                'email': fake.email(),
                'contact_info': fake.phone_number(),
                'dob': fake.date_of_birth(minimum_age=16, maximum_age=40),
            })


# Generate dummy data for libraries
def generate_libraries(num_records):
    with open('libraries.csv', 'w', newline='') as csvfile:
        fieldnames = ['library_id', 'name', 'address', 'contact_info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(num_records):
            writer.writerow({
                'library_id': i + 1,
                'name': fake.company(),
                'address': fake.address(),
                'contact_info': fake.phone_number()
            })


# Generate dummy data for category
def generate_category(library_categories):
    with open('category.csv', 'w', newline='') as csvfile:
        fieldnames = ['category_id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        idx = 1
        for i in library_categories:
            writer.writerow({
                'category_id': idx,
                'name': i
            })
            idx += 1


# Generate dummy data for books
def generate_books(num_records, library_categories):
    with open('books.csv', 'w', newline='') as csvfile:
        fieldnames = ['book_id', 'titles', 'authors', 'category_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(num_records):
            writer.writerow({
                'book_id': i + 1,
                'titles': fake.sentence(),
                'authors': [fake.name() for _ in range(random.randint(1, 3))],
                'category_id': random.randint(1, len(library_categories))
            })


# Generate dummy data for book_library
def generate_book_library(num_libraries, num_books):
    with open('book_library.csv', 'w', newline='') as csvfile:
        fieldnames = ['library_id', 'book_id', 'qty_available']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for library_id in range(1, num_libraries + 1):
            for book_id in range(1, num_books + 1):
                writer.writerow({
                    'library_id': library_id,
                    'book_id': book_id,
                    'qty_available': random.randint(0, 20)
                })


# Generate dummy data for loan status
def generate_loan_status(loan_status_list):
    with open('loan_status.csv', 'w', newline='') as csvfile:
        fieldnames = ['status_id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        idx = 1
        for i in loan_status_list:
            writer.writerow({
                'status_id': idx,
                'name': i
            })
            idx += 1


# Generate dummy data for booking status
def generate_booking_status(booking_status_list):
    with open('booking_status.csv', 'w', newline='') as csvfile:
        fieldnames = ['status_id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        idx = 1
        for i in booking_status_list:
            writer.writerow({
                'status_id': idx,
                'name': i
            })
            idx += 1


# Generate dummy data for loan_trx
def generate_loan_trx(num_users, num_books, num_libraries):
    with open('loan_trx.csv', 'w', newline='') as csvfile:
        fieldnames = ['loan_id', 'user_id', 'book_id', 'library_id', 'loan_date', 'due_date', 'return_date',
                      'loan_status_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        idx_id = 1
        for i in range(1, num_users + 1):
            loan_date = fake.date_time_between(start_date='-30d', end_date='-20d')
            due_date = loan_date + timedelta(days=14)
            return_date = loan_date + timedelta(days=random.randint(1, 13))
            writer.writerow({
                'loan_id': idx_id,
                'user_id': i,
                'book_id': random.randint(1, num_books),
                'library_id': random.randint(1, num_libraries),
                'loan_date': loan_date.strftime('%Y-%m-%d %H:%M:%S'),
                'due_date': due_date.strftime('%Y-%m-%d %H:%M:%S'),
                'return_date': return_date.strftime('%Y-%m-%d %H:%M:%S'),
                'loan_status_id': 2
            })
            idx_id += 1

        for j in range(1, num_users + 1):
            loan_date = fake.date_time_between(start_date='-5d', end_date='now')
            due_date = loan_date + timedelta(days=14)
            return_date = None
            writer.writerow({
                'loan_id': idx_id + 1,
                'user_id': j,
                'book_id': random.randint(1, num_books),
                'library_id': random.randint(1, num_libraries),
                'loan_date': loan_date.strftime('%Y-%m-%d %H:%M:%S'),
                'due_date': due_date.strftime('%Y-%m-%d %H:%M:%S'),
                'return_date': return_date,
                'loan_status_id': 2
            })
            idx_id += 1

        nums_overdue = 20
        for n in range(1, nums_overdue + 1):
            loan_date = fake.date_time_between(start_date='-28d', end_date='-20d')
            due_date = loan_date + timedelta(days=14)
            return_date = None
            writer.writerow({
                'loan_id': idx_id + 1,
                'user_id': n,
                'book_id': random.randint(1, num_books),
                'library_id': random.randint(1, num_libraries),
                'loan_date': loan_date.strftime('%Y-%m-%d %H:%M:%S'),
                'due_date': due_date.strftime('%Y-%m-%d %H:%M:%S'),
                'return_date': return_date,
                'loan_status_id': 2
            })

            idx_id += 1


# Generate dummy data for booking_trx
def generate_booking_trx(num_booking_trx, num_books, num_libraries):
    with open('booking_trx.csv', 'w', newline='') as csvfile:
        fieldnames = ['booking_id', 'user_id', 'book_id', 'library_id', 'booking_date', 'available_date', 'due_date',
                      'booking_status_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, num_booking_trx + 1):
            booking_date = fake.date_time_between(start_date='-30d', end_date='now')
            available_date = None
            due_date = None
            writer.writerow({
                'booking_id': i,
                'user_id': i,
                'book_id': random.randint(1, num_books),
                'library_id': random.randint(1, num_libraries),
                'booking_date': booking_date.strftime('%Y-%m-%d %H:%M:%S'),
                'available_date': available_date,
                'due_date': due_date,
                'booking_status_id': random.randint(1, len(booking_status_list))
            })


def import_csv_to_postgres(table_name, csv_file_path, conn_string):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    try:

        # Truncate the table before importing data to avoid duplicates
        cursor.execute(f"TRUNCATE {table_name} CASCADE;")
        print(f"TRUNCATE table successfully on table {table_name} ")

        # Copy data from CSV file to the table
        with open(csv_file_path, 'r') as f:
            cursor.copy_expert(f"COPY {table_name} FROM STDIN CSV HEADER", f)

        conn.commit()
        print(f"Data imported successfully into table {table_name}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    num_users = 1000
    num_libraries = 10
    num_categories = 5
    num_books = 500
    num_booking_trx = 10

    library_categories = [
        "Computer Science, Information & General Works",
        "Philosophy & Psychology",
        "Religion",
        "Social Sciences",
        "Language",
        "Science",
        "Technology",
        "Arts & Recreation",
        "Literature",
        "History & Geography"
    ]
    loan_status_list = ['On loan', 'Returned']
    booking_status_list = ['Active', 'Done', 'Expired']

    generate_users(num_users)
    generate_libraries(num_libraries)
    generate_category(library_categories)
    generate_books(num_books, library_categories)
    generate_loan_status(loan_status_list)
    generate_booking_status(booking_status_list)
    generate_book_library(num_libraries, num_books)
    generate_loan_trx(num_users, num_books, num_libraries)
    generate_booking_trx(num_booking_trx, num_books, num_libraries)

    conn_string = "dbname='elibrary' user='dev' host='localhost' password='adminroot'"
    table_list = ['users', 'category', 'books', 'libraries', 'book_library', 'loan_status', 'booking_status',
                  'loan_trx', 'booking_trx']
    for table in table_list:
        table_name = table
        csv_path = table_name + '.csv'
        import_csv_to_postgres(table_name, csv_path, conn_string)
