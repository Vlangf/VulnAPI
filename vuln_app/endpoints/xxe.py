from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse
import xml.etree.ElementTree as ET

router = APIRouter()


@router.get("/xxe", response_class=HTMLResponse)
async def xxe_index():
    return """
    <h2>XXE Тестирование</h2>
    <form action="/xxe/parse" method="POST" enctype="application/x-www-form-urlencoded">
        <label>XML данные:</label><br>
        <textarea name="xml" rows="10" cols="50" placeholder="<?xml version='1.0'?>
<user>
    <name>Test</name>
    <email>test@example.com</email>
</user>"></textarea><br>
        <button type="submit">Парсить XML</button>
    </form>
    """


@router.post("/xxe/parse", response_class=HTMLResponse)
async def xxe_parse(xml: str = Form("")):
    try:
        # Уязвимость: парсинг XML без отключения внешних сущностей
        root = ET.fromstring(xml)

        result = "<h3>Результат парсинга XML:</h3><ul>"
        for child in root:
            result += f"<li>{child.tag}: {child.text}</li>"
        result += "</ul>"

        return result + '<a href="/xxe">Назад</a>'

    except ET.ParseError as e:
        return f'<h3>Ошибка парсинга XML: {str(e)}</h3><a href="/xxe">Назад</a>'
    except Exception as e:
        return f'<h3>Ошибка: {str(e)}</h3><a href="/xxe">Назад</a>'
