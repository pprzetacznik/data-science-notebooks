import pickle
import pandas as pd
from scipy.spatial import distance
from functools import lru_cache


class CollaborativeFiltering:
    def __init__(self):
        pass

    def load_data(
        self, items_filepath, ranks_filepath, items_columns, ranks_columns
    ):
        self.items_filepath = items_filepath
        self.ranks_filepath = ranks_filepath
        self.data, self.items = self._load_dataframes(
            items_filepath, ranks_filepath, items_columns, ranks_columns
        )
        self.my_private_field = self._calculate_bucket(1, 2, 10)

    def train(self):
        self.cf_data = self.data.pivot(
            columns="item_id", index="user_id", values="rating"
        ).reindex(columns=self.items["movie id"])
        self.cf_data_final = self.cf_data.fillna(3)
        self.cf_data_final_numpy = self.cf_data_final.to_numpy()

    def get_ranking(self, user_id):
        cf_rank = self._compute_rank(user_id)
        neighbours = sorted(cf_rank.items(), reverse=True)[1:5]
        return [value for _, value in neighbours]

    @lru_cache
    def _compute_rank(self, user_id):
        user = self.cf_data_final.iloc[user_id].to_numpy()
        rank = {}
        for id, row in enumerate(self.cf_data_final_numpy):
            dist = 1 - distance.cosine(user, row)
            rank[dist] = id
        return rank

    def _load_dataframes(
        self, items_filepath, ranks_filepath, items_columns, ranks_columns
    ):
        data = pd.read_csv(
            ranks_filepath, sep="\t", header=None, names=ranks_columns,
        )
        items = pd.read_csv(
            items_filepath, sep="|", header=None, names=items_columns,
        )
        return data, items

    def serialize(self, model_filepath):
        with open(model_filepath, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def deserialize(model_filepath):
        with open(model_filepath, "rb") as f:
            return pickle.load(f)
