import pickle

file = open("Differences.pickle", "rb")
data = pickle.load(file)
file.close()

print(data)