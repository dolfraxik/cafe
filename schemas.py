from pydantic import BaseModel, Field

class CreateDrink(BaseModel):
    name: str = Field(min_length=2)
    price: int 
    is_available: bool