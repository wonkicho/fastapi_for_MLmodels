from fastapi import FastAPI, Path


app = FastAPI()

#min, max length 설정 가능

@app.get("/license-plates/{license}")
async def get_license_plate(license : str = Path(..., min_length=9, max_length=9)):
    return {"license" : license}