import pickle

# a = {0: 'a', 1: 'b', 2: 'c'}
# with open('test.pickle', 'wb') as f:
#     pickle.dump(a, f)


with open('test.pickle',  'rb') as f:
    a = pickle.load(f)
    a.pop(0)
    pickle.dump(a, f)