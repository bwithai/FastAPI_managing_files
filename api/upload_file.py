import hashlib
import os
import shutil
from fastapi import UploadFile, File, APIRouter

from database import session
from models import Files
from utils import add_file

upload_file_router = APIRouter(prefix="", tags=["File Management"])


@upload_file_router.post("/upload_file/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        contents = await file.read()
        hashed_content = hashlib.sha256(contents).hexdigest()

        with session as db_session:
            existing_file: Files = db_session.query(Files).filter_by(hashed_content=hashed_content).first()

            if existing_file:
                return {
                    "message": "This file already exist",
                    "id": existing_file.id
                }

        length = len(contents) / 1000
        file_size = str(round(length, 1)) + " KB"

        file_name, extension = os.path.splitext(file.filename)
        dist_path = os.path.join(os.getcwd(), 'storage')
        if not os.path.exists(dist_path):
            os.makedirs(dist_path)

        with open(f"{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        new_file_src = f"{file.filename}"
        store_new_file_at_dist = f"{dist_path}"
        shutil.move(new_file_src, store_new_file_at_dist)

        new_file_id = add_file(file_name, extension, file_size, hashed_content)
        return {
            "message": "File added with id",
            "id": new_file_id
        }
