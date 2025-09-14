from mlcycle.experiment import Experiment
from mlcycle.sklearn import SkLearn

experiment = Experiment()
run1 = experiment.create_run()
run2 = experiment.create_run()
run2.log_metric("loss", 0.5)
model = ""
run2.log_model("sklearn", model)
print(experiment.save_method.df)

# experiment2 = Experiment()
# run3 = experiment2.create_run()
# print(experiment.save_method.df)
