from mlcycle.save import SaveMethod
import pandas as pd
from mlcycle.step import Step
from mlcycle.sklearn import SkLearn

class Pandas(SaveMethod):
    def __init__(self, df=pd.DataFrame(columns=["experiment_name", "run_name", "metrics", "model"])):
        super().__init__()
        self.df = df

    # TODO: make this eagerly so it doesn't fail with multiple threads
    @classmethod
    def get_instance(cls):
        # unique_instance is inherited from SaveMethod
        if cls.unique_instance is None:
            cls.unique_instance = cls()
        return cls.unique_instance

    def create_row(self, run):
        if run.run_name not in self.df["run_name"].values:
            self.df.loc[len(self.df)] = [run.experiment.experiment_name, run.run_name, {}, None]
        else:
            raise ValueError("Run name already exists.")

    def log_metric(self, metric_name, val, step, run_name):
        row_num = self.df[self.df["run_name"] == run_name].index[0]
        metrics_val = self.df.loc[row_num, "metrics"]
        if step is None:
            metrics_val[metric_name] = val
        elif metric_name not in metrics_val.keys():
            metrics_val[metric_name] = []
            metrics_val[metric_name].append(Step(step, val))
        else:
            try:
                metrics_val[metric_name].append(Step(step, val))
            except AttributeError:
                raise AttributeError("""Setting a step when a metric was logged without an initial step.
                        To fix make that when first logging a metric, that you want to use step with,
                        you use .log_metric(metric_name, val, step)""")

    def log_model(self, model_framework, model, run_name):
        self.save_model(model_framework, model)  # save_model inherited from SaveMethod
        row_num = self.df[self.df["run_name"] == run_name].index[0]
    # TODO: work out how i am going to save the model save location to the pandas df

    def save_to_sql(self):
        pass
