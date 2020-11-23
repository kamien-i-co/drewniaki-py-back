import graphene
import map.schema

class Query(map.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)