import disable_ssl
from dotenv import load_dotenv

load_dotenv()
import os

use_proxy = os.getenv('USE_PROXY', 'FALSE').upper() == 'TRUE'

if use_proxy:
    os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
    os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
else:
    os.environ.pop("HTTP_PROXY", None)
    os.environ.pop("HTTPS_PROXY", None)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)
