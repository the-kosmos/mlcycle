from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def log_metric(self, metric_name, val, step):
        pass

    @abstractmethod
    def log_model(self, model_framework, model):
        pass
