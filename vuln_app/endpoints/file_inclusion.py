from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


# TODO vuln in query

@router.get("/page/{page}")
def show_page(page: str):
    """
    Shows the specified page by including it in the template
    """
    with open(f"templates/{page}.html", "r") as f:
        content = f.read()

    return HTMLResponse(content)
