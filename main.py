import uvicorn
from fastapi import FastAPI

from database import engine, Base
import strawberry
from strawberry.asgi import GraphQL


from routers import user as UserRouter
from dto.user_graphql import Query, Mutation

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(UserRouter.router, prefix='/user')

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app.add_route('/graphql', graphql_app)

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    