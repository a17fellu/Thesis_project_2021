# You have to do two steps here when you add a new model
# 1. Import the model (Plenty of examples below)
# 2. Add the model to the list of models. List is at the end of this file
from Main.Models.Model_0 import Model_0
from Main.Models.Model_1 import Model_1
from Main.Models.Model_2 import Model_2
from Main.Models.Model_3 import Model_3
from Main.Models.Model_9 import Model_9
from Main.Models.Model_10 import Model_10
from Main.Models.Model_11 import Model_11
from Main.Models.Model_12 import Model_12
from Main.Models.Model_50 import Model_50
from Main.Models.Model_51 import Model_51
from Main.Models.Model_52 import Model_52
from Main.Models.Model_53 import Model_53
from Main.Models.Model_54 import Model_54

''' Models distribution
Model_0 = baseline model
1-9 = Dummies for fast training and testing
10-19 = Drazen
20-29 = Andreas
50-59 = Anton
'''

models_temp = [Model_0, Model_1, Model_2, Model_3, Model_9, Model_10, Model_50, Model_51, Model_52, Model_53, Model_54,
               Model_11, Model_12]

# Making sure that the model ends up at the correct index. Expand the list if necessary
models = [None] * 100
for mod in models_temp:
    separated = mod.__name__.split("_", 1)
    models[int(separated[1])] = mod
