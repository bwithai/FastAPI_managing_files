from database import session
from models import Files


def add_file(file_name, extension, file_size, hashed):
    with session as db_session:
        new_file: Files = Files(file_name=file_name, file_extension=extension,
                                file_size=file_size,
                                hashed_content=hashed)
        db_session.add(new_file)
        db_session.commit()
        return new_file.id


