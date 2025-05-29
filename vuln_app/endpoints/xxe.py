import xml.etree.ElementTree as ET
from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/xxe")
async def xxe_vulnerable(xml_data: str = Form(...)):
    try:
        root = ET.fromstring(xml_data)
        result = {}
        for child in root:
            result[child.tag] = child.text
        return {"status": "success", "parsed_data": result}
    except Exception as e:
        return {"status": "error", "message": f"XML parsing error: {str(e)}"}


@router.get("/xxe", response_class=HTMLResponse)
async def xxe_form():
    return """
    <html>
        <body>
            <h2>XXE Test</h2>
            <form action="/xxe" method="post" enctype="application/x-www-form-urlencoded">
                <label>XML Data:</label><br>
                <textarea name="xml_data" rows="10" cols="50" placeholder='<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<user><name>&xxe;</name></user>'></textarea>
                <br><br>
                <input type="submit" value="Parse XML">
            </form>
        </body>
    </html>
    """
