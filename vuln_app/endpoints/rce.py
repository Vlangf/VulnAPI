from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse
import subprocess

router = APIRouter()


@router.get("/rce", response_class=HTMLResponse)
async def rce_index():
    return """
    <h2>RCE Тестирование</h2>
    <form action="/rce/ping" method="POST">
        <label>Ping хост:</label>
        <input type="text" name="host" placeholder="127.0.0.1">
        <button type="submit">Ping</button>
    </form>
    
    <form action="/rce/eval" method="POST">
        <label>Python выражение:</label>
        <input type="text" name="expr" placeholder="2+2">
        <button type="submit">Выполнить</button>
    </form>
    """


@router.post("/rce/ping", response_class=HTMLResponse)
async def rce_ping(host: str = Form("")):
    try:
        # Уязвимость: выполнение команды без валидации
        command = f"ping -c 1 {host}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)

        output = f"<h3>Результат ping:</h3><pre>{result.stdout}</pre>"
        if result.stderr:
            output += f"<pre>Ошибки: {result.stderr}</pre>"

        return output + '<a href="/rce">Назад</a>'

    except subprocess.TimeoutExpired:
        return '<h3>Timeout при выполнении команды</h3><a href="/rce">Назад</a>'
    except Exception as e:
        return f'<h3>Ошибка: {str(e)}</h3><a href="/rce">Назад</a>'


@router.post("/rce/eval", response_class=HTMLResponse)
async def rce_eval(expr: str = Form("")):
    try:
        # Уязвимость: выполнение произвольного Python кода
        result = eval(expr)
        return f'<h3>Результат: {result}</h3><a href="/rce">Назад</a>'
    except Exception as e:
        return f'<h3>Ошибка: {str(e)}</h3><a href="/rce">Назад</a>'
