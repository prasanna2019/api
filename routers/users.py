from fastapi import APIRouter, FastAPI, Body, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import json


class User(BaseModel):
    firstname: str=Body(...,max_length=12)
    lastname:str=Body(...,max_length=12)
    address:str=Body(...,max_length=30)
    username:str=Body(...,max_length=12)
    password:str=Body(...,max_length=12)
    token: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

MY_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, MY_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

router= APIRouter()

@router.post("/register")
async def new_user(user:User):
    access_token= create_access_token(
        data={"sub":user.username}
    )
    hashed_password= get_password_hash(user.password)
    
    setattr(user,'token',access_token)
    setattr(user,'password',hashed_password)
    return user

@router.post("/login")
async def login_user(username:str=Body(..., max_length=12), password:str=Body(..., max_length=12) ):
    hashed_password= get_password_hash(password)
    return {"username" : username, "password" : hashed_password}

@router.post("/logout")
async def logout_user():
    return 0    

@router.get("/cart")
async def getCartItems(token: str=Header(...)):
    return 0

@router.post("/cart")
async def addToCartItems(token: str=Header(...), items:str=Body(...)):
    return 0

@router.delete("/cart/{item_id}")
async def deleteFromCart(item_id:str, token: str=Header(...)):
    return 0

@router.get("/order")
async def orderDetail(token: str=Header(...)):
    return 0


