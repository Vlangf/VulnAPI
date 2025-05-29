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
from endpoints.ssti import router as ssti
from endpoints.xxe import router as xxe
from endpoints.rce import router as rce
from endpoints.ptrav import router as ptrav
from endpoints.ldap_injection import router as ldap_injection
from endpoints.nosql_injection import router as nosql_injection
from endpoints.jwt_vulnerabilities import router as jwt_vulnerabilities
from endpoints.deserialization import router as deserialization
from endpoints.race_condition import router as race_condition
from endpoints.idor import router as idor

app = FastAPI()

app.include_router(command_injection)
app.include_router(csrf)
app.include_router(file_inclusion)
app.include_router(file_upload)
app.include_router(insecure_CAPTCHA)
app.include_router(SQL_Injection)
app.include_router(xss)
app.include_router(open_redirect)
app.include_router(ssti)
app.include_router(xxe)
app.include_router(rce)
app.include_router(ptrav)
app.include_router(ldap_injection)
app.include_router(nosql_injection)
app.include_router(jwt_vulnerabilities)
app.include_router(deserialization)
app.include_router(race_condition)
app.include_router(idor)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5035)
