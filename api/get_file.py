from fastapi import APIRouter

getfile_router = APIRouter(prefix="", tags=["File Management"])


@getfile_router.get("/get_file/")
async def get_file():
    pass
