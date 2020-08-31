from typing import Optional

from fastapi import FastAPI
from routers import items, users
app = FastAPI()

app.include_router(
    items.router,
    prefix="/items"
) 
app.include_router(
    users.router,
    prefix="/users"
)



    
