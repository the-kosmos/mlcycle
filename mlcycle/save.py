from abc import ABC, abstractmethod
from mlcycle.sklearn import SkLearn

class SaveMethod(ABC):
    unique_instance = None
    def __init__(self):
        self.df = None

    @classmethod
    def save_model(cls, model_framework, model):
        model_framework = model_framework.lower()
        framework_map = {"sklearn": SkLearn, "pytorch": None, "tensorflow": None}  # these all follow the ModelFramework interface
        if model_framework in framework_map.keys():
            framework_map[model_framework].framework_save_model(model)  # TODO: work out how i am going to let users decide where they save their model
        else:
            raise ValueError(f"Model framework, {model_framework}, is not supported.")

    @abstractmethod
    def get_instance(self):
        pass

    @abstractmethod
    def create_row(self, run):
        pass

    @abstractmethod
    def log_metric(self, metric_name, val, step, run_name):
        pass

    @abstractmethod
    def log_model(self, model_framework, model, run_name):
        pass
