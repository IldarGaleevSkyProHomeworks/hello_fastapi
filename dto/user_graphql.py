from database import get_db
import services.user as UserService
import strawberry
import typing
from dto.user import User as DBUser

@strawberry.type
class User:
    id: int
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, user_id: int) -> User:
        db=next(get_db())
        return UserService.get_user(user_id, db)
    
    @strawberry.field
    def users(self, info) -> typing.List[User]:
        db=next(get_db())
        return UserService.get_users(db)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str) -> User:
        db=next(get_db())
        return UserService.create_user(DBUser(name=name), db)
    
    @strawberry.mutation
    def update_user(self, info, name: str, user_id: int) -> User:
        db=next(get_db())
        return UserService.update_user(DBUser(name=name), user_id, db)
    
    @strawberry.mutation
    def delete_user(self, info, user_id: int )->int:
        db=next(get_db())
        return UserService.remove_user(user_id, db)