from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	name: str
	price: float
	is_offer: bool | None = None

class Accessory(BaseModel):
	name: str
	color: str
	in_stock: bool | None = None

accessories_example_db = [
    {"id":1, "name":"Coque iPhone 14", "color":"Noir", "in_stock":True},
    {"id":2, "name":"Chargeur Samsung", "color":"Blanc", "in_stock":False},
    {"id":3, "name":"Écouteurs Bluetooth", "color":"Bleu", "in_stock":True},
]

@app.get("/")
def read_root():
	return {"Hello": "World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
	return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
	return {"item_name": item.name, "item_id": item_id}


@app.get("/accessories")
def read_all_accessories():
	return {"accessories": accessories_example_db}

@app.get("/accessories/{accessory_id}")
def read_accessory(accessory_id: int):
	for acc in accessories_example_db:
		if acc["id"] == accessory_id:
			return acc
	return {"Error": "Not Found!"}

@app.post("/accessories")
def add_accessory(accessory: Accessory):
	new_id = len(accessories_example_db) + 1
	new_acc = {"id": new_id, **accessory.dict()}
	accessories_example_db.append(new_acc)
	return new_acc

@app.put("/accessories/{accessory_id}")
def update_accessory(accessory_id: int, accessory: Accessory):
	for i, acc in enumerate(accessories_example_db):
		if acc["id"]==accessory_id:
			accessories_example_db[i]={"id": accessory_id, **accessory.dict()}
			return {"accessory_name": accessory.name, "accessory_id":accessory_id}
	return {"error": "not found!"}

@app.delete("/accessories/{accessory_id}")
def delete_accessory(accessory_id: int):
	for i, acc in enumerate(accessories_example_db):
		if acc["id"]==accessory_id :
			accessories_example_db.pop(i)
			return {"result": "deleted"}
	return {"result": "not found!"}
