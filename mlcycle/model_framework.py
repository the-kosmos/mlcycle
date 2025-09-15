from abc import ABC, abstractmethod

class ModelFramework(ABC):
    @abstractmethod
    def framework_save_model(self, model, file_name):
        pass
