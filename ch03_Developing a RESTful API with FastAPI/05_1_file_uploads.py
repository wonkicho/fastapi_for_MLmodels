from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
#multiple file upload 가능
async def upload_file(file: UploadFile = File(...)):
    #파일 크리 리턴
    """
    {
    "file_name": "cat.jpg",
    "content_type": "image/jpeg"
    }
    """
    return {'file_name' : file.filename, 'content_type' : file.content_type}

    