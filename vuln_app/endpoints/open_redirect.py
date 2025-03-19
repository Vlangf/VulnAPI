from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/open_redirect")
def open_redirect(redirect_to: str = Query(...)):
    return f"""
    <html>
    <body>
    <a href="{redirect_to}">redirecting</a>
    </body></html>
    """
