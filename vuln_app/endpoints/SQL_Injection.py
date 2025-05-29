from fastapi import Form, APIRouter, Query
from fastapi.responses import HTMLResponse
import sqlite3

router = APIRouter()


@router.get("/sqli", response_class=HTMLResponse)
async def sqli_index():
    return """
    <h2>SQL Injection Тестирование</h2>
    <form action="/sqli/login" method="POST">
        <label>Username:</label>
        <input type="text" name="username" placeholder="admin">
        <label>Password:</label>
        <input type="password" name="password" placeholder="password">
        <button type="submit">Войти</button>
    </form>
    
    <form action="/sqli/search" method="GET">
        <label>Поиск пользователя:</label>
        <input type="text" name="id" placeholder="1">
        <button type="submit">Найти</button>
    </form>
    """


@router.post("/sqli/login", response_class=HTMLResponse)
async def sqli_login(username: str = Form(""), password: str = Form("")):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Уязвимость: SQL injection через конкатенацию строк
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            return f'<h3>Успешный вход! Добро пожаловать, {result[1]}</h3><a href="/sqli">Назад</a>'
        else:
            return f'<h3>Неверные учетные данные</h3><p>Query: {query}</p><a href="/sqli">Назад</a>'
    except Exception as e:
        conn.close()
        return f'<h3>Ошибка базы данных: {str(e)}</h3><p>Query: {query}</p><a href="/sqli">Назад</a>'


@router.get("/sqli/search", response_class=HTMLResponse)
async def sqli_search(id: str = Query("")):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Уязвимость: SQL injection в WHERE clause
    query = f"SELECT username, email FROM users WHERE id = {id}"

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            return f'<h3>Пользователь найден:</h3><p>Username: {result[0]}</p><p>Email: {result[1]}</p><a href="/sqli">Назад</a>'
        else:
            return f'<h3>Пользователь не найден</h3><p>Query: {query}</p><a href="/sqli">Назад</a>'
    except Exception as e:
        conn.close()
        return f'<h3>Ошибка базы данных: {str(e)}</h3><p>Query: {query}</p><a href="/sqli">Назад</a>'


@router.get("/api/users/{user_id}")
async def get_user_api(user_id: str):
    """API эндпоинт с SQL Injection уязвимостью"""
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = f"SELECT username, email FROM users WHERE id = {user_id}"

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            return {"username": result[0], "email": result[1], "query": query}
        else:
            return {"error": "User not found", "query": query}
    except Exception as e:
        conn.close()
        return {"error": str(e), "query": query}
