from mlcycle.experiment import Experiment
from mlcycle.sklearn import SkLearn
import pandas as pd

experiment = Experiment()
run1 = experiment.create_run()
experiment2 = Experiment()
run2 = experiment2.create_run()
run2.log_metric("loss", 0.9)
# model = ""
# run2.log_model("sklearn", model, "model1.pkl")
print(experiment.df)

experiment = Experiment()
df = pd.read_json("data.json")
experiment.load_df(df)
run_for_new_experiment = experiment.create_run()
print(experiment.df)

# experiment.df.to_json("data.json")
# experiment2 = Experiment()
# run3 = experiment2.create_run()
# print(experiment.save_method.df)
