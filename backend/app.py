from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.environ['MYSQL_HOST'],
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'database': os.environ['MYSQL_DATABASE']
}

@app.route('/')
def hello():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM message LIMIT 1")
    message = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
