from fastapi import FastAPI, File

app = FastAPI()

@app.post("/files")
#bytes로 리턴하게 됨
async def upload_file(file: bytes = File(...)):
    #파일 크리 리턴
    """
        {
    "file_size": 71457
    }
    """
    return {'file_size' : len(file)}

    