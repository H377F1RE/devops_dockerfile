from flask import Flask
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    for i in range(10):
        try:
            conn = psycopg2.connect(
                host=os.environ.get("POSTGRES_HOST", "localhost"),
                database=os.environ.get("POSTGRES_DB", "users_db"),
                user=os.environ.get("POSTGRES_USER", "postgres"),
                password=os.environ.get("POSTGRES_PASSWORD", "postgres")
            )
            return conn
        except psycopg2.OperationalError:
            print("Database not ready, retrying...")
            time.sleep(2)
    raise Exception("Could not connect to database")

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name FROM users;')
    users = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()

    users_list_html = "".join([f"<li>{name}</li>" for name in users])
    html = f"""
    <html>
    <body>
        <div style="text-align:center; margin-top:50px;">
            <h1>Hello from Flask + PostgreSQL!</h1>
            <h3>Current users in DB:</h3>
            <ul style="list-style-type:none; padding:0;">
                {users_list_html}
            </ul>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
