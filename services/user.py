from sqlalchemy.orm import Session
from models.user import User
from dto import user


def create_user(data: user.User, db: Session):
    new_user = User(name=data.name)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        print(e)

    return new_user


def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def update_user(data: user.User, user_id: int, db: Session):
    updated_user = db.query(User).filter(User.id == user_id).first()
    updated_user.name = data.name

    db.add(updated_user)
    db.commit()
    db.refresh(updated_user)

    return updated_user


def remove_user(user_id: int, db: Session):
    removed_user = db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return removed_user
