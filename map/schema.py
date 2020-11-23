import graphene
from graphene_django import DjangoObjectType
from .models import Monument, Marker, Photo

class MonumentType(DjangoObjectType):
    class Meta:
        model = Monument

class MarkerType(DjangoObjectType):
    class Meta:
        model = Marker

class PhotoType(DjangoObjectType):
    class Meta:
        model = Photo

class Query(graphene.ObjectType):
    monuments = graphene.List(MonumentType)
    def resolve_monuments(self, info, **kwargs):
        return Monument.objects.all()
