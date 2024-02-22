from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService
from dto import user as UserDTO

router = APIRouter()

@router.post('/', tags=["user"])
async def create(data:UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{user_id}', tags=["user"])
async def get(user_id:int = None, db: Session = Depends(get_db)):
    return UserService.get_user(user_id, db)

@router.get('/', tags=["user"])
async def get_list(db: Session = Depends(get_db)):
    return UserService.get_users(db)

@router.put('/{user_id}', tags=["user"])
async def update(data:UserDTO.User = None, user_id:int = None, db: Session = Depends(get_db)):
    return UserService.update_user(data,user_id, db)

@router.delete('/{user_id}', tags=["user"])
async def delete(user_id:int = None, db: Session = Depends(get_db)):
    return UserService.remove_user(user_id, db)
