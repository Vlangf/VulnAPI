import subprocess
from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse

app = APIRouter()


@app.get("/rce", response_class=HTMLResponse)
async def rce_form():
    return """
    <html>
        <body>
            <h2>RCE Test (Ping Command)</h2>
            <form action="/rce" method="post">
                <label>Host to ping:</label>
                <input type="text" name="host" placeholder="127.0.0.1; cat /etc/passwd">
                <br><br>
                <input type="submit" value="Ping">
            </form>
        </body>
    </html>
    """


@app.post("/rce")
async def rce_vulnerable(host: str = Form(...)):
    try:
        command = f"ping -c 1 {host}"
        print(f"Executing command: {command}")

        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        return {
            "status": "success",
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Command timeout"}
    except Exception as e:
        return {"status": "error", "message": f"Command execution error: {str(e)}"}
