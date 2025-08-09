from fastapi import FastAPI, UploadFile, File
from app.processor import process_question
import uvicorn

app = FastAPI()

@app.post("/api/")
async def handle_question(file: UploadFile = File(...)):
    content = await file.read()
    return process_question(content.decode())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)