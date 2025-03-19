from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

router = APIRouter()

db = create_engine("sqlite:///mydatabase.db")


class Item(BaseModel):
    name: str
    description: str


@router.post("/items")
async def create_item(item: Item):
    name = item.name
    description = item.description
    query = f"INSERT INTO items (name, description) VALUES (\'{name}\', \'{description}\')"

    try:
        conn = db.connect()
        conn.execute(text(query))
        conn.commit()
        return {"message": "Item created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()


class ItemsTable(Base):
    __tablename__ = 'items'

    name = Column(String, primary_key=True)
    description = Column(String)


Base.metadata.create_all(db)
