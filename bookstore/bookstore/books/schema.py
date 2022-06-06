import graphene
from graphene import ObjectType, Schema, Mutation
from graphene_django import DjangoObjectType

from bookstore.books.models import Publisher, Book

class PublisherType(DjangoObjectType):
    class Meta:
        model  = Publisher
        fields = ("id", "p_name", "city", "zip")

class BookType(DjangoObjectType):
    class Meta:
        model  = Book
        fields = ("id", "pub", "title", "price", "category", "quantity", "b_format", "prod_year", "filesize")

class Query(ObjectType):
    all_book      = graphene.List(BookType)
    all_publisher = graphene.List(PublisherType)

    @graphene.resolve_only_args
    def resolve_all_book(self):
        return Book.objects.all()

    @graphene.resolve_only_args
    def resolve_all_publisher(self):
        return Publisher.objects.all()


class CreatePublisher(Mutation):
    id     = graphene.String()
    p_name = graphene.String()
    city   = graphene.String()
    zip    = graphene.String()

    class Arguments:
        id = graphene.NonNull(graphene.Int)
        p_name = graphene.String()
        city   = graphene.String()
        zip    = graphene.String()

    def mutate(self, info, id, p_name, city, zip):
        publisher = Publisher(id=id, p_name=p_name, city=city, zip=zip)
        publisher.save()

        return CreatePublisher(
            id     = publisher.id,
            p_name = publisher.p_name,
            city   = publisher.city,
            zip    = publisher.zip,
        )

class Mutation(graphene.ObjectType):
    create_publisher = CreatePublisher.Field()

schema = Schema(query=Query, mutation=Mutation)