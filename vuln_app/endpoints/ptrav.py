from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/ptrav", response_class=HTMLResponse)
async def ptrav_form():
    return """
    <html>
        <body>
            <h2>Path Traversal Test</h2>
            <form action="/ptrav" method="get">
                <label>File to read:</label>
                <input type="text" name="file" placeholder="../../../etc/passwd">
                <br><br>
                <input type="submit" value="Read File">
            </form>
        </body>
    </html>
    """


@router.get("/ptrav/read")
async def ptrav_vulnerable(file: str = Query(...)):
    try:
        file_path = f"./files/{file}"
        print(f"Attempting to read file: {file_path}")

        with open(file_path, "r") as f:
            content = f.read()

        return {"status": "success", "file_path": file_path, "content": content}
    except FileNotFoundError:
        return {"status": "error", "message": "File not found"}
    except Exception as e:
        return {"status": "error", "message": f"File reading error: {str(e)}"}
