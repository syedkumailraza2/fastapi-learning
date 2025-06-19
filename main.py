from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def root():
    return {'message':'Hello world!'}

@app.get("/teas")
def tea_route():
    return teas

@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return teas

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = tea
            return tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas.pop(index)
            return {"Tea Deleted successfully"}
    return {"error": "Tea not found"}