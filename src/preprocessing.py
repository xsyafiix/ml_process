import pandas as pd
import numpy as np
import util as util
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def load_dataset(config_data: dict) -> pd.DataFrame:
    # Load every set of data
    x_train = util.pickle_load(config_data["train_set_path"][0])
    y_train = util.pickle_load(config_data["train_set_path"][1])

    x_valid = util.pickle_load(config_data["valid_set_path"][0])
    y_valid = util.pickle_load(config_data["valid_set_path"][1])

    x_test = util.pickle_load(config_data["test_set_path"][0])
    y_test = util.pickle_load(config_data["test_set_path"][1])

    # Concatenate x and y each set
    train_set = pd.concat(
        [x_train, y_train],
        axis = 1
    )
    valid_set = pd.concat(
        [x_valid, y_valid],
        axis = 1
    )
    test_set = pd.concat(
        [x_test, y_test],
        axis = 1
    )

    # Return 3 set of data
    return train_set, valid_set, test_set


def rus_fit_resample(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # Create sampling object
    rus = RandomUnderSampler(random_state = 26)

    # Balancing set data
    x_rus, y_rus = rus.fit_resample(
        set_data.drop("live_birth_occurrence", axis = 1), 
        set_data["live_birth_occurrence"]
    )

    # Concatenate balanced data
    set_data_rus = pd.concat(
        [x_rus, y_rus], 
        axis = 1
    )

    # Return balanced data
    return set_data_rus

def ros_fit_resample(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # Create sampling object
    ros = RandomOverSampler(random_state = 11)

    # Balancing set data
    x_ros, y_ros = ros.fit_resample(
        set_data.drop("live_birth_occurrence", axis = 1), 
        set_data["live_birth_occurrence"]
    )

    # Concatenate balanced data
    set_data_ros = pd.concat(
        [x_ros, y_ros], 
        axis = 1
    )

    # Return balanced data
    return set_data_ros

def sm_fit_resample(set_data: pd.DataFrame) -> pd.DataFrame:
    # Create copy of set data
    set_data = set_data.copy()

    # Create sampling object
    sm = SMOTE(random_state = 112)

    # Balancing set data
    x_sm, y_sm = sm.fit_resample(
        set_data.drop("live_birth_occurrence", 
                      axis = 1), 
        set_data["live_birth_occurrence"]
    )

    # Concatenate balanced data
    set_data_sm = pd.concat(
        [x_sm, y_sm], 
        axis = 1
    )

    # Return balanced data
    return set_data_sm



if __name__ == "__main__":
    # 1. Load configuration file
    config_data = util.load_config()

    # 2. Load dataset
    train_set, valid_set, test_set = load_dataset(config_data)


    # 3. Convert into categorical data
    # 3.1. Train set
    pmap = {'18 - 34':0,'35-37':1,'38-39':2,'40-42':3,'43-44':4,'45-50':5}
    train_set['patient_age_at_treatment'] = train_set['patient_age_at_treatment'].map(pmap)

    # 3.2. Validation set
    pmap = {'18 - 34':0,'35-37':1,'38-39':2,'40-42':3,'43-44':4,'45-50':5}
    valid_set['patient_age_at_treatment'] = valid_set['patient_age_at_treatment'].map(pmap)


    # 3.3. Test set
    pmap = {'18 - 34':0,'35-37':1,'38-39':2,'40-42':3,'43-44':4,'45-50':5}
    test_set['patient_age_at_treatment'] = test_set['patient_age_at_treatment'].map(pmap)


    # 4. Undersampling dataset
    train_set_rus = rus_fit_resample(train_set)

    # 5. Oversampling dataset
    train_set_ros = ros_fit_resample(train_set)

    # 6. SMOTE dataset
    train_set_sm = sm_fit_resample(train_set)

    # 7. Dumping dataset
    x_train = {
        "Undersampling" : train_set_rus.drop(columns = "live_birth_occurrence"),
        "Oversampling" : train_set_ros.drop(columns = "live_birth_occurrence"),
        "SMOTE" : train_set_sm.drop(columns = "live_birth_occurrence")
    }
    y_train = {
        "Undersampling" : train_set_rus["live_birth_occurrence"],
        "Oversampling" : train_set_ros["live_birth_occurrence"],
        "SMOTE" : train_set_sm["live_birth_occurrence"]
    }

    util.pickle_dump(
        x_train,
        "data/processed/x_train_feng.pkl"
    )
    util.pickle_dump(
        y_train,
        "data/processed/y_train_feng.pkl"
    )

    util.pickle_dump(
        valid_set.drop(columns = "categori"),
        "data/processed/x_valid_feng.pkl"
    )
    util.pickle_dump(
        valid_set.categori,
        "data/processed/y_valid_feng.pkl"
    )

    util.pickle_dump(
        test_set.drop(columns = "categori"),
        "data/processed/x_test_feng.pkl"
    )
    util.pickle_dump(
        test_set.categori,
        "data/processed/y_test_feng.pkl"
    )