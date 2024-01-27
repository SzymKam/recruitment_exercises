import pickle

# Serializacja za pomocą Pickle
data = {'klucz': 'wartość'}
with open('plik.pkl', 'wb') as file:
    pickle.dump(data, file)




# Deserializacja za pomocą Pickle
with open('plik.pkl', 'rb') as file:
    restored_data = pickle.load(file)
    x = 'a'

print(restored_data)
print(x)
