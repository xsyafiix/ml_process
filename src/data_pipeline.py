from sklearn.model_selection import train_test_split
from tqdm import tqdm
import pandas as pd
import os
import copy
import util as util

def read_raw_data(config: dict) -> pd.DataFrame:
    # Create variable to store raw dataset
    raw_dataset = pd.DataFrame()

    # Raw dataset dir
    raw_dataset_file = config["raw_dataset_file"]

    # Look and load add CSV files
    raw_dataset = pd.read_excel(raw_dataset_file,engine='pyxlsb')
    
    # Return raw dataset
    return raw_dataset

def check_data(input_data, params, api = False):
    input_data = copy.deepcopy(input_data)
    params = copy.deepcopy(params)
    
    if not api:
        # Check data types
        assert input_data.select_dtypes("object").columns.to_list() == params["object_columns"], "an error occurs in object column(s)."
        assert input_data.select_dtypes("int").columns.to_list() == params["int32_columns"], "an error occurs in int32 column(s)."
    else:
        # In case checking data from api
        # Predictor that has object dtype
        object_columns = params["object_columns"]
        del object_columns[1:]


        # Check data types
        assert input_data.select_dtypes("object").columns.to_list() == \
            object_columns, "an error occurs in object column(s)."
        assert input_data.select_dtypes("int").columns.to_list() == \
            int_columns, "an error occurs in int32 column(s)."        
    

    # Check range of data
    assert input_data['total_number_of_previous_ivf_cycles'].between(params['range_total_number_of_previous_ivf_cycles'][0], params['range_total_number_of_previous_ivf_cycles'][1]).sum() == len(input_data), 'an error occurs in total_number_of_previous_ivf_cycles range.'
    assert input_data['total_number_of_ivf_pregnancies'].between(params['range_total_number_of_ivf_pregnancies'][0], params['range_total_number_of_ivf_pregnancies'][1]).sum() == len(input_data), 'an error occurs in total_number_of_ivf_pregnancies range.'
    assert input_data['total_number_of_live_births_conceived_through_ivf'].between(params['range_total_number_of_live_births_conceived_through_ivf'][0], params['range_total_number_of_live_births_conceived_through_ivf'][1]).sum() == len(input_data), 'an error occurs in total_number_of_live_births_-_conceived_through_ivf range.'
    assert input_data['type_of_infertility_female_primary'].between(params['range_type_of_infertility_female_primary'][0], params['range_type_of_infertility_female_primary'][1]).sum() == len(input_data), 'an error occurs in type_of_infertility_-_female_primary range.'
    assert input_data['type_of_infertility_female_secondary'].between(params['range_type_of_infertility_female_secondary'][0], params['range_type_of_infertility_female_secondary'][1]).sum() == len(input_data), 'an error occurs in type_of_infertility_-_female_secondary range.'
    assert input_data['type_of_infertility_male_primary'].between(params['range_type_of_infertility_male_primary'][0], params['range_type_of_infertility_male_primary'][1]).sum() == len(input_data), 'an error occurs in type_of_infertility_-_male_primary range.'
    assert input_data['type_of_infertility_male_secondary'].between(params['range_type_of_infertility_male_secondary'][0], params['range_type_of_infertility_male_secondary'][1]).sum() == len(input_data), 'an error occurs in type_of_infertility_-_male_secondary range.'
    assert input_data['type_of_infertility_couple_primary'].between(params['range_type_of_infertility_couple_primary'][0], params['range_type_of_infertility_couple_primary'][1]).sum() == len(input_data), 'an error occurs in type_of_infertility_-couple_primary range.'
    assert input_data['type_of_infertility_couple_secondary'].between(params['range_type_of_infertility_couple_secondary'][0], params['range_type_of_infertility_couple_secondary'][1]).sum() == len(input_data), 'an error occurs in type_of_infertility_-couple_secondary range.'
    assert input_data['cause_of_infertility_tubal_disease'].between(params['range_cause_of_infertility_tubal_disease'][0], params['range_cause_of_infertility_tubal_disease'][1]).sum() == len(input_data), 'an error occurs in cause__of_infertility_-_tubal_disease range.'
    assert input_data['cause_of_infertility_ovulatory_disorder'].between(params['range_cause_of_infertility_ovulatory_disorder'][0], params['range_cause_of_infertility_ovulatory_disorder'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_ovulatory_disorder range.'
    assert input_data['cause_of_infertility_male_factor'].between(params['range_cause_of_infertility_male_factor'][0], params['range_cause_of_infertility_male_factor'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_male_factor range.'
    assert input_data['cause_of_infertility_patient_unexplained'].between(params['range_cause_of_infertility_patient_unexplained'][0], params['range_cause_of_infertility_patient_unexplained'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_patient_unexplained range.'
    assert input_data['cause_of_infertility_endometriosis'].between(params['range_cause_of_infertility_endometriosis'][0], params['range_cause_of_infertility_endometriosis'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_endometriosis range.'
    assert input_data['cause_of_infertility_cervical_factors'].between(params['range_cause_of_infertility_cervical_factors'][0], params['range_cause_of_infertility_cervical_factors'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_cervical_factors range.'
    assert input_data['cause_of_infertility_female_factors'].between(params['range_cause_of_infertility_female_factors'][0], params['range_cause_of_infertility_female_factors'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_female_factors range.'
    assert input_data['cause_of_infertility_partner_sperm_concentration'].between(params['range_cause_of_infertility_partner_sperm_concentration'][0], params['range_cause_of_infertility_partner_sperm_concentration'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-_partner_sperm_concentration range.'
    assert input_data['cause_of_infertility_partner_sperm_morphology'].between(params['range_cause_of_infertility_partner_sperm_morphology'][0], params['range_cause_of_infertility_partner_sperm_morphology'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-__partner_sperm_morphology range.'
    assert input_data['causes_of_infertility_partner_sperm_motility'].between(params['range_causes_of_infertility_partner_sperm_motility'][0], params['range_causes_of_infertility_partner_sperm_motility'][1]).sum() == len(input_data), 'an error occurs in causes_of_infertility_-_partner_sperm_motility range.'
    assert input_data['cause_of_infertility_partner_sperm_immunological_factors'].between(params['range_cause_of_infertility_partner_sperm_immunological_factors'][0], params['range_cause_of_infertility_partner_sperm_immunological_factors'][1]).sum() == len(input_data), 'an error occurs in cause_of_infertility_-__partner_sperm_immunological_factors range.'
    assert input_data['stimulation_used'].between(params['range_stimulation_used'][0], params['range_stimulation_used'][1]).sum() == len(input_data), 'an error occurs in stimulation_used range.'
    assert input_data['fresh_cycle'].between(params['range_fresh_cycle'][0], params['range_fresh_cycle'][1]).sum() == len(input_data), 'an error occurs in fresh_cycle range.'
    assert input_data['frozen_cycle'].between(params['range_frozen_cycle'][0], params['range_frozen_cycle'][1]).sum() == len(input_data), 'an error occurs in frozen_cycle range.'
    assert input_data['eggs_thawed'].between(params['range_eggs_thawed'][0], params['range_eggs_thawed'][1]).sum() == len(input_data), 'an error occurs in eggs_thawed range.'
    assert input_data['fresh_eggs_collected'].between(params['range_fresh_eggs_collected'][0], params['range_fresh_eggs_collected'][1]).sum() == len(input_data), 'an error occurs in fresh_eggs_collected range.'
    assert input_data['eggs_mixed_with_partner_sperm'].between(params['range_eggs_mixed_with_partner_sperm'][0], params['range_eggs_mixed_with_partner_sperm'][1]).sum() == len(input_data), 'an error occurs in eggs_mixed_with_partner_sperm range.'
    

if __name__ == "__main__":
    # 1. Load configuration file
    config_data = util.load_config()

    # 2. Read all raw dataset
    raw_dataset = read_raw_data(config_data)

    # 3. Reset index
    raw_dataset.reset_index(
        inplace = True,
        drop = True
    )
    
    # 4 Renaming Columns
    raw_dataset.columns = raw_dataset.columns.str.lower().str.replace(' ','_')
    
    # 5. Save raw dataset
    util.pickle_dump(
        raw_dataset,
        config_data["raw_dataset_path"]
    )

    # 6. Handing Variabel 'Total Number of Previous IVF cycles'
    raw_dataset['total_number_of_previous_ivf_cycles'] = raw_dataset['total_number_of_previous_ivf_cycles'].replace(">=5", 6).astype(int)

    # 7. Handling variable Total number of IVF pregnancies
    raw_dataset['total_number_of_ivf_pregnancies'] = raw_dataset['total_number_of_ivf_pregnancies'].replace(">=5", 6).astype(int)
    
    # 8. Handling variable Fresh Cycle
    raw_dataset['fresh_cycle'] = raw_dataset['fresh_cycle'].fillna(0).astype(int)
    
    # 9. Handling variable Frozen Cycle
    raw_dataset['frozen_cycle'] = raw_dataset['frozen_cycle'].fillna(0).astype(int)
    
    # 10. Handling variable Egg Source
    raw_dataset['egg_source'] = raw_dataset['egg_source'].fillna('not assigned')

    # 11. Handling variable Eggs Thawed
    raw_dataset['eggs_thawed'] = raw_dataset['eggs_thawed'].fillna(0).astype(int)
    
    
    # 12. Handling variable Fresh Eggs Collected
    raw_dataset['fresh_eggs_collected'] = raw_dataset['fresh_eggs_collected'].replace("> 50", 51)
    raw_dataset['fresh_eggs_collected'] = raw_dataset['fresh_eggs_collected'].fillna(0).astype(int)

    # 13. Handling variable Eggs Mixed With Partner Sperm
    raw_dataset['eggs_mixed_with_partner_sperm'] = raw_dataset['eggs_mixed_with_partner_sperm'].replace("> 50", 51)
    rraw_dataset['eggs_mixed_with_partner_sperm'] = raw_dataset['eggs_mixed_with_partner_sperm'].fillna(0).astype(int)

    # 14. Handling variable Embryos Transfered
    raw_dataset['embryos_transfered'] = raw_dataset['embryos_transfered'].fillna(0).astype(int)

    # 15. Handling variable live birth occurrence
    raw_dataset['live_birth_occurrence'] = raw_dataset['live_birth_occurrence'].fillna(0)
    raw_dataset['live_birth_occurrence'] = raw_dataset['live_birth_occurrence'].astype(int)
    raw_dataset.drop(index = raw_dataset[raw_dataset["date_of_egg_thawing"] == 999].index, inplace = True)
    raw_dataset.drop(index = raw_dataset[raw_dataset["patient_age_at_treatment"] == '999'].index, inplace = True)
   
    util.pickle_dump(
        raw_dataset,
        config_data["cleaned_raw_dataset_path"]
    )

    # 16. Check data definition
    check_data(raw_dataset, config_data)

    # 17. Splitting input output
    x = raw_dataset[config_data["predictors"]].copy()
    y = raw_dataset['live_birth_occurrence'].copy()

    # 18. Splitting train test
    x_train, x_test, \
    y_train, y_test = train_test_split(
        x, y,
        test_size = 0.3,
        random_state = 42,
        stratify = y
    )

    # 19. Splitting test valid
    x_valid, x_test, \
    y_valid, y_test = train_test_split(
        x_test, y_test,
        test_size = 0.5,
        random_state = 42,
        stratify = y_test
    )

    # 20. Save train, valid and test set
    util.pickle_dump(x_train, config_data["train_set_path"][0])
    util.pickle_dump(y_train, config_data["train_set_path"][1])

    util.pickle_dump(x_valid, config_data["valid_set_path"][0])
    util.pickle_dump(y_valid, config_data["valid_set_path"][1])

    util.pickle_dump(x_test, config_data["test_set_path"][0])
    util.pickle_dump(y_test, config_data["test_set_path"][1])