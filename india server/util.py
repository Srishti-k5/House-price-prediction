import json
import pickle

__data_columns = None
__model = None
__type = None
__transaction = None
__status = None
__furnishing = None
__facing = None

def get_features():
    return __type, __transaction, __status, __furnishing, __facing

def load_saved_artifacts():
    print("Loading....")
    global __data_columns
    global __type
    global __transaction
    global __status
    global __furnishing
    global __facing

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __type = __data_columns[8:13]
        __transaction = __data_columns[13:14]
        __status = __data_columns[14:15]
        __furnishing = __data_columns[15:17]
        __facing = __data_columns[17:]

    with open("./artifacts/india_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("Loading Completed")

    if __name__ == "__main__":
        print(get_features())
