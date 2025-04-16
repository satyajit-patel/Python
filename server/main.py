from fastapi import FastAPI  # framework
from pydantic import BaseModel  # for validation

app = FastAPI()

class Quote(BaseModel):
    id: int
    quote: str
    author: str

quote_list = []

@app.get("/")
def home():
    return {"message": "server is up"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/api/v1/quote")
def get_quote():
    return {"quotes": quote_list}

@app.post("/api/v1/quote") 
def add_quote(quote: Quote):
    quote_list.append(quote)
    print("quote added successfully")
    return quote_list

@app.put("/api/v1/quote/{quote_id}")  
def update_quote(quote_id: int, updated_quote: Quote):
    for index, it in enumerate(quote_list):  # need enumerate to get both index and iterator at same time
        if it.id == quote_id:
            quote_list[index] = updated_quote
            return updated_quote
    return {"error": "quote not found"}

@app.delete("/api/v1/quote/{quote_id}")  
def delete_quote(quote_id: int): 
    for index, it in enumerate(quote_list):  
        if it.id == quote_id:
            deleted_item = quote_list.pop(index)
            return deleted_item
    return {"error": "id not found"}



# http://localhost:8000/docs
