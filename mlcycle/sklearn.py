from mlcycle.model_framework import ModelFramework
import joblib

class SkLearn(ModelFramework):
    @classmethod
    def framework_save_model(cls, model, file_name):
        joblib.dump(model, file_name)
