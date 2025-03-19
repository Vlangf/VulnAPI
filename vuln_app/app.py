import uvicorn

from fastapi import FastAPI

from endpoints.command_injection import router as command_injection
from endpoints.csrf import router as csrf
from endpoints.file_inclusion import router as file_inclusion
from endpoints.file_upload import router as file_upload
from endpoints.insecure_CAPTCHA import router as insecure_CAPTCHA
from endpoints.SQL_Injection import router as SQL_Injection
from endpoints.xss import router as xss
from endpoints.open_redirect import router as open_redirect

app = FastAPI()

app.include_router(command_injection)
app.include_router(csrf)
app.include_router(file_inclusion)
app.include_router(file_upload)
app.include_router(insecure_CAPTCHA)
app.include_router(SQL_Injection)
app.include_router(xss)
app.include_router(open_redirect)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5035)
