import graphene
from graphene_django import DjangoObjectType
from graph_api.models import Account

class AccountType(DjangoObjectType):
  class Meta:
    model = Account
    fields = ("id", "name", "ownder")

class Query(graphene.ObjectType):
  """
  Queries for the Restaurant model
  """
  accounts = graphene.List(AccountType)

  def resolve_account(self, info, **kwargs):
    return Account.objects.all()
  
schema = graphene.Schema(query=Query)