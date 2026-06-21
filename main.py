from fastapi import FastAPI, HTTPException
from schemas import CreateDrink

app = FastAPI()

MENU = [
    {"id": 1, "name": "Эспрессо", "price": 150, "is_available": True},
    {"id": 2, "name": "Капучино", "price": 200, "is_available": True},
    {"id": 3, "name": "Латте", "price": 220, "is_available": False}
]

@app.get('/menu')
async def get_all_menu():
    return MENU

@app.post('/add_in_menu')
async def create_drink(new_drink: CreateDrink):
    MENU.append({
        'id': len(MENU) + 1,
        'name': new_drink.name,
        'price': new_drink.price,
        'is_available': new_drink.is_available
    })
    return {'success':True, 'message': 'Everything was added'}

@app.post("/orders")
async def make_order(item_id: int):
    for drink in MENU:
        if drink['id'] == item_id:
            if drink['is_available'] == True:
                price = drink['price']
                return {'success':True, 'message': f'Here is your drink from you {price} dollars'}
            else:
                 raise HTTPException(status_code=400, detail='Drink is gone')
    raise HTTPException(status_code=404, detail='Drink not found')