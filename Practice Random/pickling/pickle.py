
import pickle

cars = ['maruti', 'suzuki', 'toyota']
fileobj = open('car.pkl', 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

# fileobj = open('cars.pkl', 'rb')
# v = pickle.load(fileobj)
# print(v)
# fileobj.close()
