import os
import logging
import mysql.connector

log_file = os.path.join("logs", "app.log")

def get_connection():
    config = {"host": "localhost",
              "port": 3310,
              "user": "root",
              "password": "secret",
              "database": "Equipment-Registry"}
    conn = mysql.connector.connect(**config)
    return conn

def create_table():
    conn = mysql.connector.connect(host="localhost",
                                   port=3310,
                                   user="root",
                                   password="secret",
                                   database="Equipment-Registry")

    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    quantity INT DEFAULT 0,
    available BOOLEAN DEFAULT TRUE)    
    """)
    conn.commit()
    cursor.close()
    conn.close()
