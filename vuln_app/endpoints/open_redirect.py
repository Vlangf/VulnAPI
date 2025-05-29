from fastapi import APIRouter, Query
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
