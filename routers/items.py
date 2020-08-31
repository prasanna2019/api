from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

class Items(BaseModel):
        products:str

router= APIRouter()

@router.get("/allproducts")
async def productsList():
    products={
        "pizza":[{"name":"Margaretha", "price": "200", "description":"pizza with cheese only"},
                {"name":"Farmhouse", "price": "300", "description":"pizza with cheese and vegetables"},
                {"name":"Deluxe", "price": "200", "description":"pizza with lots of cheese and vegetables"}
        ],
        "pasta":[{"name":"Creamy alfredo", "price": "250", "description":"pasta with white sauce"},
                {"name":"Spicy pasta", "price": "200", "description":"pasta with red sauce"}

        ],
        "sides":[{"name":"cheese garlic bread", "price": "200", "description":"tasty garlic bread with cheese"},
                {"name":"Garlic bread", "price": "150", "description":"hot garlic bread"}

        ]

    }
    return products
