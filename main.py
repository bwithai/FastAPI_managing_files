from fastapi import FastAPI

from api.get_file import getfile_router
from api.upload_file import upload_file_router

app = FastAPI()

app.include_router(upload_file_router)

app.include_router(getfile_router)
