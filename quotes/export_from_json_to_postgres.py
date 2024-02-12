import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")

import django
django.setup()

from django.core.management import call_command


import json
from quoteapp.models import Author, Tag, Quote


def export_data():

    export_authors("authors_hw9.json")
    export_quotes("quotes_hw9.json")


def export_authors(filename):

    with open(filename, 'r') as file:
        authors_data = json.load(file)

    for author_data in authors_data:
        author_name = author_data["fullname"]
        born_date = author_data["born_date"]
        born_location = author_data["born_location"]
        description = author_data["description"]


        author, created = Author.objects.get_or_create(
            fullname=author_name,
            born_date=born_date,
            born_location=born_location,
            description=description
        )


def export_quotes(filename):

    with open(filename, "r") as file:
        quotes_data = json.load(file)

    all_tags = set()
    for quote_data in quotes_data:
        all_tags.update(quote_data["tags"])

    for tag_name in all_tags:
        print("1: ", tag_name)
        tag, created = Tag.objects.get_or_create(name=tag_name)

    for quote_data in quotes_data:
        print("2: ", quote_data)
        quote_text = quote_data["quote"]
        author_name = quote_data["author"]
        print(f"3 : {author_name}")
        author = Author.objects.get(fullname=author_name)

        quote, created = Quote.objects.get_or_create(quote=quote_text, author=author)

        for tag_name in quote_data["tags"]:
            print("4: ", tag_name)
            tag = Tag.objects.get(name=tag_name)
            quote.tags.add(tag)

            # The Quote model has a tags field, which is a ManyToManyField linking to Tag model
            # The above loop automatically takes care of associating tags with the quote
        quote.save()


if __name__ == "__main__":
    export_data()
