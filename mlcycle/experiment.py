from mlcycle.pandas import Pandas
from mlcycle.save import SaveMethod
from mlcycle.run import Run
from random_word import RandomWords

r = RandomWords()

class Experiment:
    def __init__(self, save_method=Pandas.get_instance()):  # Singleton design pattern
        self.save_method: SaveMethod = save_method
        self.df = self.save_method.df
        self.experiment_name = f"{r.get_random_word()}_{r.get_random_word()}"

    def create_run(self, run_name=None):
        if run_name is None:
            run_name = f"{r.get_random_word()}_{r.get_random_word()}"
        return Run(run_name, self)

    def load_df(self, df):
        self.df = self.save_method.load_df(df)
        # self.df = self.save_method.df
