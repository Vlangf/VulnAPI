from fastapi import File, UploadFile, APIRouter

router = APIRouter()


@router.post("/upload_file")
async def create_upload_file(file: UploadFile = File(...)):
    """
    Uploads a file to the server
    """
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
