import numpy as np

def standarize_features(df,feature_names,input_features):
    
    """This is a function that takes in the values of the features given by the user of the
    and returns and standarized version of them. This is done because the model was trained
    using standarized features. 

    Args:
        df (pandas DataFrame): Data dataframe from the original dataset of heart failure prediction. 
        feature_names (list): Names of the seven features the model was trained on. 
        input_features (list): Values of the features the user input to the API. 

    Returns:
        standarized_features (list): A standarized version of the input features for the prediction. 
    """
    standarized_features = [(input_features[i] - np.mean(df[feature_names[i]]))/(np.std(df[feature_names[i]])) for i in range(len(feature_names))]
    
    return standarized_features