import os

path = "Users/Luxorv/Development/python/algorithms/coursera/resources/data_structures/basic_data_structures/tree_height/tests/"
s = open(path+'01')

for i in range(1, 24):
    name = str(i)

    if i < 10:
        name = '0' + name

    complete_path = "../resources/data_structures/basic_data_structures/tree_height/tests/"
    os.system('python3 tree_height.py < '+complete_path+name)
