from cf.cf2 import CollaborativeFiltering
from cf.utils import resource_filepath


def test_cf():
    items_columns = [
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
    ranks_columns = ["user_id", "item_id", "rating", "timestamp"]
    items_filepath = resource_filepath("u.item")
    ranks_filepath = resource_filepath("u.base")
    cf = CollaborativeFiltering()
    cf.load_data(items_filepath, ranks_filepath, items_columns, ranks_columns)
    cf.train()
    print(cf.predict(2))
