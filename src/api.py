from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import util as util
import data_pipeline as data_pipeline
import preprocessing as preprocessing

config_data = util.load_config()
model_data = util.pickle_load(config_data["production_model_path"])

class api_data(BaseModel):
    patient_age_at_treatment : int
    total_number_of_previous_ivf_cycles : int
    total_number_of_ivf_pregnancies : int
    total_number_of_live_births_conceived_through_ivf : int
    type_of_infertility_female_primary : int
    type_of_infertility_female_secondary : int
    type_of_infertility_male_primary : int
    type_of_infertility_male_secondary : int
    type_of_infertility_couple_primary : int
    type_of_infertility_couple_secondary : int
    cause_of_infertility_tubal_disease : int
    cause_of_infertility_ovulatory_disorder : int
    cause_of_infertility_male_factor : int
    cause_of_infertility_patient_unexplained : int
    cause_of_infertility_endometriosis : int
    cause_of_infertility_cervical_factors : int
    cause_of_infertility_female_factors : int
    cause_of_infertility_partner_sperm_concentration : int
    cause_of_infertility_partner_sperm_morphology : int
    causes_of_infertility_partner_sperm_motility : int
    cause_of_infertility_partner_sperm_immunological_factors : int
    stimulation_used : int
    fresh_cycle : int
    frozen_cycle : int
    eggs_thawed : int
    fresh_eggs_collected : int
    eggs_mixed_with_partner_sperm : int
    embryos_transfered : int

app = FastAPI()

@app.get("/")
def home():
    return "Hello, FastAPI up!"

@app.post("/predict/")
def predict(data: api_data):    
    # Convert data api to dataframe
    data = pd.DataFrame(data).set_index(0).T.reset_index(drop = True)

    # Convert dtype
    data = pd.concat(
        [
            data[config_data["predictors"][0]],
            data[config_data["predictors"][1:]].astype(int)
        ],
        axis = 1
    )

    # Check range data
    try:
        data_pipeline.check_data(data, config_data, True)
    except AssertionError as ae:
        return {"res": [], "error_msg": str(ae)}


    # Predict data
    y_pred = model_data["model_data"]["model_object"].predict(data)

    return {"res" : y_pred, "error_msg": ""}

if __name__ == "__main__":
    uvicorn.run("api:app", host = "0.0.0.0", port = 8080)
