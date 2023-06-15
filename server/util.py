import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_price(squareMeters, numberOfRooms, hasYard, hasPool, floors, cityCode, 
                       cityPartRange, numPrevOwners, hasStormProtector, basement, attic,
                       garage, hasStorageRoom, hasGuestRoom, HouseAge):
    
    x = np.zeros(len(__data_columns))
    # Assign values in the same order as data_columns
    feature_values = [squareMeters, numberOfRooms, hasYard, hasPool, floors, cityCode,
                     cityPartRange, numPrevOwners, hasStormProtector, basement, attic,
                     garage, hasStorageRoom, hasGuestRoom, HouseAge]
    
    for i, column in enumerate(__data_columns):
        x[i] = feature_values[i]
    
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    with open("../model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('../model/paris_real_estate_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()