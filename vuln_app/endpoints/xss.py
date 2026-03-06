from fastapi import Query, APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse


router = APIRouter()


def _make_search_handler(path: str):
    @router.get(path, response_class=HTMLResponse)
    async def search(query: str = Query(...)):
        """XSS"""
        result = f'Search results for "{query}"'
        return f"<html><body><h1>{result}</h1></body></html>"
    search.__name__ = f"search_{path.replace('/', '_')}"
    return search


search_paths = [
    "/search",
    *[f"/search_{i}" for i in range(1, 12)],
    *[f"/search/{i}" for i in range(1, 4)],
]

for path in search_paths:
    _make_search_handler(path)


stored_comments = []


@router.get("/xss", response_class=HTMLResponse)
async def xss_index():
    return """
    <h2>XSS Тестирование</h2>
    <form action="/xss/reflected" method="GET">
        <label>Reflected XSS:</label>
        <input type="text" name="input" placeholder="Введите текст">
        <button type="submit">Отправить</button>
    </form>

    <form action="/xss/stored" method="POST">
        <label>Stored XSS:</label>
        <input type="text" name="comment" placeholder="Комментарий">
        <button type="submit">Добавить</button>
    </form>

    <form action="/xss/dom" method="GET">
        <label>DOM XSS:</label>
        <input type="text" name="data" placeholder="Данные">
        <button type="submit">Показать</button>
    </form>
    """


@router.get("/xss/reflected", response_class=HTMLResponse)
async def xss_reflected(input: str = Query("")):
    return f'<h3>Вы ввели: {input}</h3><a href="/xss">Назад</a>'


@router.post("/xss/stored", response_class=HTMLResponse)
async def xss_stored_post(comment: str = Form("")):
    stored_comments.append(comment)
    return RedirectResponse(url="/xss/stored", status_code=303)


@router.get("/xss/stored", response_class=HTMLResponse)
async def xss_stored_get():
    comments_html = "".join([f"<p>{comment}</p>" for comment in stored_comments])
    return f"""
    <h3>Сохраненные комментарии:</h3>
    {comments_html}
    <a href="/xss">Назад</a>
    """


@router.get("/xss/dom", response_class=HTMLResponse)
async def xss_dom(data: str = Query("")):
    return f'''
    <h3>DOM XSS Test</h3>
    <div id="output"></div>
    <script>
        var data = "{data}";
        document.getElementById("output").innerHTML = "Данные: " + data;
    </script>
    <a href="/xss">Назад</a>
    '''
