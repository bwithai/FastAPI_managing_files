import uuid

from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Files(Base):
    __tablename__ = "files"

    id = Column(String(32), primary_key=True, index=True)
    file_name = Column(String(100), nullable=True)
    file_extension = Column(String(100), nullable=True)
    file_size = Column(String(100), nullable=True)
    hashed_content = Column(String(200))

    __table_args__ = (UniqueConstraint('hashed_content'),)

    def __init__(self, file_name, file_extension, file_size, hashed_content):
        self.id = str(uuid.uuid4().hex)
        self.file_name = file_name
        self.file_extension = file_extension
        self.file_size = file_size
        self.hashed_content = hashed_content


Base.metadata.create_all(engine)
