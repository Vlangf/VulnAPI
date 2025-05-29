from fastapi import APIRouter, Query, Form
from fastapi.responses import RedirectResponse, HTMLResponse

router = APIRouter()


@router.get("/open_redirect")
def open_redirect(redirect_to: str = Query(...)):
    return f"""
    <html>
    <body>
    <a href="{redirect_to}">redirecting</a>
    </body></html>
    """


@router.get("/redir", response_class=HTMLResponse)
async def redir_form():
    return """
    <html>
        <body>
            <h2>Open Redirect Test</h2>
            <form action="/redir/redirect" method="get">
                <label>Redirect URL:</label>
                <input type="text" name="url" placeholder="http://evil.com">
                <br><br>
                <input type="submit" value="Redirect">
            </form>
            <br>
            <p>Try: <a href="/redir/redirect?url=http://google.com">Redirect to Google</a></p>
        </body>
    </html>
    """


@router.get("/redir/redirect")
async def redir_vulnerable(url: str = Query(...)):
    print(f"Redirecting to: {url}")
    return RedirectResponse(url=url)


@router.get("/redirect", response_class=HTMLResponse)
async def redirect_index():
    return """
    <h2>Open Redirect Тестирование</h2>
    <form action="/redirect/go" method="GET">
        <label>URL для перенаправления:</label>
        <input type="text" name="url" placeholder="https://example.com">
        <button type="submit">Перейти</button>
    </form>
    
    <form action="/redirect/login" method="POST">
        <label>Логин (с редиректом):</label>
        <input type="text" name="username" placeholder="admin">
        <input type="hidden" name="next" value="/dashboard">
        <button type="submit">Войти</button>
    </form>
    """


@router.get("/redirect/go")
async def redirect_go(url: str = Query("")):
    if url:
        return RedirectResponse(url=url)
    else:
        return HTMLResponse('<h3>URL не указан</h3><a href="/redirect">Назад</a>')


@router.post("/redirect/login")
async def redirect_login(username: str = Form(""), next: str = Form("/")):
    if username:
        return RedirectResponse(url=next, status_code=303)
    else:
        return HTMLResponse('<h3>Имя пользователя не указано</h3><a href="/redirect">Назад</a>')
