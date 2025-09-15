from mlcycle.log import Log
from mlcycle.step import Step
from mlcycle.model_framework import ModelFramework
from mlcycle.sklearn import SkLearn

class Run(Log):
    def __init__(self, run_name, experiment):
        self.run_name = run_name
        self.experiment = experiment  # composition
        self.experiment.save_method.create_row(self)
        # self.df = self.experiment.save_method.df
        # self.row_num = self.df[self.df["run_name"] == self.run_name].index[0]

    def log_metric(self, metric_name, val, step=None):
        self.experiment.save_method.log_metric(metric_name, val, step, self.run_name)

    def log_model(self, model_framework, model, file_name="model.pkl"):
        self.experiment.save_method.log_model(model_framework, model, file_name, self.run_name)

# TODO: need to loosen the coupling between Run and the particular SaveMethod, Pandas.
# TODO: currently the methods log_metric and log_model in Run only work with Pandas SaveMethod.
# TODO: if we have future SaveMethod like SqL then log_metric and log_model need to be agnostic and loose.

    # @abstractmethod
    # def save_method_log_metric(self, metric_name, val, step=None):
    #     metrics_val = self.df.loc[self.row_num, "metrics"]
    #     if step is None:
    #         metrics_val[metric_name] = val
    #     elif metric_name not in metrics_val.keys():
    #         metrics_val[metric_name] = []
    #         metrics_val[metric_name].append(Step(step, val))
    #     else:
    #         try:
    #             metrics_val[metric_name].append(Step(step, val))
    #         except AttributeError:
    #             raise AttributeError("""Setting a step when a metric was logged without an initial step.
    #             To fix make that when first logging a metric, that you want to use step with,
    #             you use .log_metric(metric_name, val, step)""")


    # def log_model(self, model_framework, model):
    #     model_framework = model_framework.lower()
    #     framework_map = {"sklearn": SkLearn, "pytorch": None, "tensorflow": None}  # these all follow the ModelFramework interface
    #     if model_framework in framework_map.keys():
    #         framework_map[model_framework].framework_save_model(model)
    #     else:
    #         raise ValueError(f"Model framework, {model_framework}, is not supported.")
    #     # self.df.loc[self.row_num, "model"] = model  # the model default value is None, which is immutable
