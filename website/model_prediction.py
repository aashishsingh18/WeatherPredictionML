import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

def load_model(location):
    """
    input is a string to file location of the model
    output is the model
    """
    f = open(location, "rb")
    model = pickle.load(f)
    f.close()
    return model

def make_prediction(X: np.array) -> np.array:
    """
    Input is 2d array and output is 1d array
    Loads model and returns prediction 
    """
    MODEL_LOCATION = "website/model.pickle"
    model = load_model(MODEL_LOCATION)
    return (model.predict(X))


def main():
    #Base prediction to check if correct prediction was made 
    decoder = ["clear-day", "cloudy", "partly-cloudy-day", "rain", "snow"]
    temp = [32,70,100]
    humidity = [80, 60,40]
    precip = [0.5, 0.1, 0.05]
    windspeed = [15, 8 , 6]
    sealevelpressure = [1010, 1020, 1030]

    datapoint1 = [temp[0], humidity[0], precip[0], windspeed[0], sealevelpressure[0]]
    datapoint2 = [temp[1], humidity[1], precip[1], windspeed[1], sealevelpressure[1]]
    datapoint3 = [temp[2], humidity[2], precip[2], windspeed[2], sealevelpressure[2]]

    encoded_predictions = make_prediction(np.array([datapoint1, datapoint2,datapoint3]))

    print(list(round(prediction) for prediction in encoded_predictions))
    for prediction in encoded_predictions:
        print(decoder[round(prediction)])

if __name__ == "__main__":
    main()

