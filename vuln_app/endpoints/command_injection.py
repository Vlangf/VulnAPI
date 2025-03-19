import subprocess

from fastapi import Query, APIRouter

router = APIRouter()


@router.get('/ping')
async def ping_host(host: str = Query(...)):
    """
    Command Injection
    """
    cmd = f"ping -c 3 {host}"
    subprocess.call(cmd, shell=True)
    return {"result": f"Pinged {host} successfully"}
