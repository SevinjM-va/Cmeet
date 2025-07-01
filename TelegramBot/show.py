from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", response_class = JSONResponse)
async def process():
  try:
    with open("messages.json","r",encoding="utf-8") as f:
      data = json.load(f)
    return data
  except FileNotFoundError:
    return {"error":"messages.json not found"}