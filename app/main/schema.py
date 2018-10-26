import graphene
from graphene import relay
from app.main.services.user_service import UserService
from app.main.models.user import User
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Users(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    registered_on = graphene.DateTime()
    password = graphene.String()


class Query(graphene.ObjectType):
    find_user = graphene.Field(User, username=graphene.String())
    all_users = SQLAlchemyConnectionField(Users)

    def resolve_find_user(self, info, username):
        return UserService.get_a_user(username)


schema = graphene.Schema(query=Query)