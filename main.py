import pandas as pd


class CondProbParameters(object):
    def __init__(self, rand_var_name, cond_var_name, rand_var_value, cond_var_value, df):
        self.prob = None
        self.rand_var_name = rand_var_name
        self.cond_var_name = cond_var_name
        self.rand_var_value = rand_var_value
        self.cond_var_value = cond_var_value
        self.set_prob(df)

    def set_prob(self, df):
        helpful_table = pd.crosstab(df[self.rand_var_name], df[self.cond_var_name], normalize='columns')
        self.prob = helpful_table[self.cond_var_value][self.rand_var_value]


data = pd.read_csv('nexus.csv')
param_names = data.columns.values.tolist()
param_names = param_names[2:]
useful = list()
useless0 = list()
useless1 = list()

for name in param_names:
    unique_values = set(data[name].tolist())
    if unique_values & set("01") == set("01"):
        useful.append(name)
    if unique_values & set("01") == set("0"):
        useless0.append(name)
    if unique_values & set("01") == set("1"):
        useless1.append(name)


all_cond_probs = list()
only_probs = list()

for rand_var in useful:
    for cond_var in useful:
        if rand_var != cond_var:
            print(rand_var, cond_var)
            cond_prob01 = CondProbParameters(rand_var, cond_var, "1", "0", data)
            all_cond_probs.append(cond_prob01)
            only_probs.append(cond_prob01.prob)


