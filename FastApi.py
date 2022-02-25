from fastapi import FastAPI, Path
import requests

tits = FastAPI()

@tits.get('/')
async def root():
    return {"message": "hello World"}
