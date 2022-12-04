import preprocessing
import util as utils
import pandas as pd
import numpy as np

def test_patient_categorical_age():
    # Arrange
    config = utils.load_config()

    mock_data = {
        "patient_age_at_treatment" : ['18 - 34','18 - 34','38-39','43-44','35-37','45-50']}
    mock_data = pd.DataFrame(mock_data)
    expected_data = {
        "patient_age_at_treatment" : [0, 0, 2, 4, 1, 5]}
    expected_data = pd.DataFrame(expected_data)

    # Act
    processed_data = preprocessing.join_label_categori(mock_data, config)

    # Assert
    assert processed_data.equals(expected_data)