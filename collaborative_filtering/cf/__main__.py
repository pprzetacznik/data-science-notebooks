from json import dumps
from argparse import Namespace, ArgumentParser
from cf import CollaborativeFiltering
from cf.utils import resource_filepath


def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Collaborative Filtering runner")
    parser.add_argument(
        "--model-name",
        type=str,
        help="Model name",
        dest="model_name",
        default="model.pkl",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--train", help="Train mode", action="store_true")
    parser.add_argument(
        "--items-filename",
        type=str,
        help="Name of items data file",
        dest="items_filename",
        default="u.item",
    )
    parser.add_argument(
        "--ranks-filename",
        type=str,
        help="Name of ranks data file",
        dest="ranks_filename",
        default="u.base",
    )
    group.add_argument("--test", help="Test mode", action="store_true")
    parser.add_argument("--user-id", type=int, help="User id", dest="user_id")
    return parser.parse_args()


def train(model_filepath: str, items_filepath: str, ranks_filepath: str):
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
    cf = CollaborativeFiltering()
    cf.load_data(items_filepath, ranks_filepath, items_columns, ranks_columns)
    cf.train()
    cf.serialize(model_filepath)
    print(dumps({"model_filepath": model_filepath}, indent=4))


def test(model_filepath: str):
    cf = CollaborativeFiltering.deserialize(model_filepath)
    print(
        dumps(
            {
                "model_filepath": model_filepath,
                "neighbours": cf.get_ranking(args.user_id),
            },
            indent=4,
        )
    )


def main(args: Namespace) -> None:
    model_filepath = resource_filepath(args.model_name)
    if args.train:
        items_filepath = resource_filepath(args.items_filename)
        ranks_filepath = resource_filepath(args.ranks_filename)
        train(model_filepath, items_filepath, ranks_filepath)
    elif args.test:
        test(model_filepath)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
