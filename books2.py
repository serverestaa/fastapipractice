from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5),
    Book(2, 'FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request = Body()):
    BOOKS.append(book_request)
