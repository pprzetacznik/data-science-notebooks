import os
from pkg_resources import resource_filename
from pytest import fixture
from cf import CollaborativeFiltering
from cf.utils import resource_filepath, resource_file_content, remove_file


@fixture
def items_columns():
    return [
        "movie id",
        "movie title",
        "release date",
        "video release date",
        "IMDb URL",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children's",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ]


@fixture
def ranks_columns():
    return ["user_id", "item_id", "rating", "timestamp"]


def test_serialization(items_columns, ranks_columns):
    model_filepath = resource_filepath("model.pkl")
    items_filepath = resource_filepath("u.item")
    ranks_filepath = resource_filepath("u.base")
    cf = CollaborativeFiltering()
    cf.load_data(items_filepath, ranks_filepath, items_columns, ranks_columns)
    cf.serialize(model_filepath)
    cf2 = CollaborativeFiltering.deserialize(model_filepath)
    assert cf2.items_filepath == cf.items_filepath
    remove_file(model_filepath)


def test_cf(items_columns, ranks_columns):
    items_filepath = resource_filepath("u.item")
    ranks_filepath = resource_filepath("u.base")
    cf = CollaborativeFiltering()
    cf.load_data(items_filepath, ranks_filepath, items_columns, ranks_columns)
    cf.train()
    assert len(cf.get_ranking(1)) == 4
