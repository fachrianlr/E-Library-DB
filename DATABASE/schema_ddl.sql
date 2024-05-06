-- Create Database
create database elibrary;


-- Table: users
CREATE TABLE users (
   user_id SERIAL PRIMARY KEY,
   user_name VARCHAR(20) NOT NULL,
   password VARCHAR(100) NOT NULL,
   full_name varchar(100) NOT NULL,
   email VARCHAR(50) NOT NULL,
   contact_info VARCHAR(50),
   dob DATE
);


-- Table: libraries
CREATE TABLE libraries (
   library_id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   address VARCHAR(255) NOT NULL,
   contact_info VARCHAR(50)
);


-- Table: category
CREATE TABLE category (
   category_id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL
);


-- Table: books
CREATE TABLE books (
   book_id SERIAL PRIMARY KEY,
   titles varchar(255) NOT NULL ,
   authors varchar(255) NOT NULL ,
   category_id INT REFERENCES category(category_id)
);


-- Table: book_library
CREATE TABLE book_library (
   library_id INT REFERENCES libraries(library_id),
   book_id INT REFERENCES books(book_id),
   available_qty INT CHECK (available_qty >= 0),
   PRIMARY KEY (library_id, book_id)
);


-- Table: loan_status
CREATE TABLE loan_status (
   status_id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL
);


-- Table: loan_trx
CREATE TABLE loan_trx (
   loan_id SERIAL PRIMARY KEY,
   user_id INT REFERENCES users(user_id),
   book_id INT REFERENCES books(book_id),
   library_id INT REFERENCES libraries(library_id),
   loan_date timestamp NOT NULL,
   due_date timestamp NOT NULL,
   return_date timestamp,
   loan_status_id INT REFERENCES loan_status(status_id)
);


-- Table: booking_status
CREATE TABLE booking_status (
   status_id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL
);


-- Table: booking_trx
CREATE TABLE booking_trx (
   booking_id SERIAL PRIMARY KEY,
   user_id INT REFERENCES users(user_id),
   book_id INT REFERENCES books(book_id),
   library_id INT REFERENCES libraries(library_id),
   booking_date TIMESTAMP NOT NULL,
   available_date TIMESTAMP,
   due_date DATE,
   booking_status_id INT REFERENCES booking_status(status_id)
);
