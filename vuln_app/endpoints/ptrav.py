from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
import os

router = APIRouter()


@router.get("/ptrav", response_class=HTMLResponse)
async def ptrav_index():
    # Создаем тестовые файлы
    os.makedirs("uploads", exist_ok=True)
    with open("uploads/test.txt", "w") as f:
        f.write("Это тестовый файл")
    with open("uploads/secret.txt", "w") as f:
        f.write("Секретная информация!")

    return """
    <h2>Path Traversal Тестирование</h2>
    <form action="/ptrav/read" method="GET">
        <label>Имя файла:</label>
        <input type="text" name="file" placeholder="test.txt">
        <button type="submit">Читать файл</button>
    </form>
    
    <form action="/ptrav/download" method="GET">
        <label>Скачать файл:</label>
        <input type="text" name="filename" placeholder="test.txt">
        <button type="submit">Скачать</button>
    </form>
    """


@router.get("/ptrav/read", response_class=HTMLResponse)
async def ptrav_read(file: str = Query("")):
    try:
        # Уязвимость: чтение файла без валидации пути
        filepath = os.path.join("uploads", file)
        with open(filepath, "r") as f:
            content = f.read()

        return f'<h3>Содержимое файла {file}:</h3><pre>{content}</pre><a href="/ptrav">Назад</a>'
    except Exception as e:
        return f'<h3>Ошибка: {str(e)}</h3><a href="/ptrav">Назад</a>'


@router.get("/ptrav/download")
async def ptrav_download(filename: str = Query("")):
    try:
        # Уязвимость: скачивание файла без валидации пути
        filepath = os.path.join("uploads", filename)
        return FileResponse(filepath, filename=filename)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Ошибка: {str(e)}")
