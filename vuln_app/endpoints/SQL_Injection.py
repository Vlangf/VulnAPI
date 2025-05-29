import sqlite3
from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse

app = APIRouter()


def init_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT
        )
    """)
    cursor.execute(
        "INSERT OR IGNORE INTO users (id, username, password, email) VALUES (1, 'admin', 'secret123', 'admin@test.com')"
    )
    cursor.execute(
        "INSERT OR IGNORE INTO users (id, username, password, email) VALUES (2, 'user', 'password', 'user@test.com')"
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/sqli", response_class=HTMLResponse)
async def sqli_form():
    return """
    <html>
        <body>
            <h2>SQL Injection Test</h2>
            <form action="/sqli" method="post">
                <label>Username:</label>
                <input type="text" name="username" placeholder="admin' OR '1'='1">
                <br><br>
                <label>Password:</label>
                <input type="password" name="password" placeholder="anything">
                <br><br>
                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    """


@app.post("/sqli")
async def sqli_vulnerable(username: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            return {"status": "success", "message": "Login successful", "users": result}
        else:
            return {"status": "error", "message": "Invalid credentials"}
    except Exception as e:
        conn.close()
        return {"status": "error", "message": f"Database error: {str(e)}"}
