from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = APIRouter()


@app.get("/ssti", response_class=HTMLResponse)
async def ssti_form():
    return """
    <html>
        <body>
            <h2>SSTI Test</h2>
            <form action="/ssti" method="post">
                <label>Template:</label>
                <input type="text" name="template" placeholder="Hello {{7*7}}!" style="width: 300px;">
                <br><br>
                <input type="submit" value="Render Template">
            </form>
            <br>
            <p>Try: <code>{{7*7}}</code> or <code>{{''.__class__.__mro__[1].__subclasses__()}}</code></p>
        </body>
    </html>
    """


@app.post("/ssti")
async def ssti_vulnerable(template: str = Form(...)):
    try:
        jinja_template = Template(template)
        rendered = jinja_template.render()

        return {"status": "success", "template": template, "rendered": rendered}
    except Exception as e:
        return {"status": "error", "message": f"Template rendering error: {str(e)}"}
