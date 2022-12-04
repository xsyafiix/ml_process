import streamlit as st
import requests
from PIL import Image

# Load and set images in the first place
# header_images = Image.open('assets/header_images.jpg')
# st.image(header_images)

# Add some information about the service
st.title("IVF Occurrence Prediction")
st.subheader("Enter variables below to get prediction of IVF")

# Create form of input
with st.form(key = "air_data_form"):
    # Create box for number input
    patient_age_at_treatment = st.number_input(
        label = "1.\tEnter Patient Age at Treatment Value:",
        min_value = 0,
        max_value = 5,
        help = "Value= {'18-34':0,'35-37':1,'38-39':2,'40-42':3,'43-44':4,'45-50':5}"
    )
    
    total_number_of_previous_ivf_cycles = st.number_input(
        label = "2.\tEnter Total Number of Previous IVF cycles  Value:",
        min_value = 0,
        max_value = 20,
        help = "Value range from 0 to 20"
    )
    
    total_number_of_ivf_pregnancies = st.number_input(
        label = "3.\tEnter Total number of IVF pregnancies Value:",
        min_value = 0,
        max_value = 20,
        help = "Value range from 0 to 20"
    )
    total_number_of_live_births_conceived_through_ivf = st.number_input(
        label = "4.\tEnter Total number of live births - conceived through IVF  Value:",
        min_value = 0,
        max_value = 20,
        help = "Value range from 0 to 20"
    )
    
    type_of_infertility_female_primary = st.number_input(
        label = "5.\tEnter Type of Infertility - Female Primary  Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    
    type_of_infertility_female_secondary = st.number_input(
        label = "6.\tEnter Type of Infertility - Female Secondary Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    
    type_of_infertility_male_primary = st.number_input(
        label = "7.\tEnter Type of Infertility - Male Primary Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    
    type_of_infertility_male_secondary = st.number_input(
        label = "8.\tEnter Type of Infertility - Male Secondary Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    type_of_infertility_couple_primary = st.number_input(
        label = "9.\tEnter Type of Infertility -Couple Primary Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    type_of_infertility_couple_secondary = st.number_input(
        label = "10.\tEnter Type of Infertility -Couple Secondary Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_tubal_disease = st.number_input(
        label = "11.\tEnter Cause  of Infertility - Tubal disease Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_ovulatory_disorder = st.number_input(
        label = "12.\tEnter Cause of Infertility - Ovulatory Disorder Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_male_factor = st.number_input(
        label = "13.\tEnter Cause of Infertility - Male Factor Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_patient_unexplained = st.number_input(
        label = "14.\tEnter Cause of Infertility - Patient Unexplained Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_endometriosis = st.number_input(
        label = "15.\tEnter Cause of Infertility - Endometriosis Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_cervical_factors = st.number_input(
        label = "16.\tEnter Cause of Infertility - Cervical factors Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_female_factors = st.number_input(
        label = "17.\tEnter Cause of Infertility - Female Factors Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_partner_sperm_concentration = st.number_input(
        label = "18.\tEnter Cause of Infertility - Partner Sperm Concentration Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_partner_sperm_morphology = st.number_input(
        label = "19.\tEnter Cause of Infertility -  Partner Sperm Morphology Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    causes_of_infertility_partner_sperm_motility = st.number_input(
        label = "20.\tEnter Causes of Infertility - Partner Sperm Motility Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    cause_of_infertility_partner_sperm_immunological_factors = st.number_input(
        label = "21.\tEnter Cause of Infertility -  Partner Sperm Immunological factors Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    stimulation_used = st.number_input(
        label = "22.\tEnter Stimulation used Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    fresh_cycle = st.number_input(
        label = "23.\tEnter Fresh Cycle Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    frozen_cycle = st.number_input(
        label = "24.\tEnter Frozen Cycle Value:",
        min_value = 0,
        max_value = 1,
        help = "Value range from 0 to 1"
    )
    eggs_thawed = st.number_input(
        label = "25.\tEnter Eggs Thawed Value:",
        min_value = 0,
        max_value = 100,
        help = "Value range from 0 to 100"
    )
    fresh_eggs_collected = st.number_input(
        label = "26.\tEnter Fresh Eggs Collected Value:",
        min_value = 0,
        max_value = 100,
        help = "Value range from 0 to 100"
    )
    eggs_mixed_with_partner_sperm = st.number_input(
        label = "27.\tEnter Eggs Mixed With Partner Sperm Value:",
        min_value = 0,
        max_value = 100,
        help = "Value range from 0 to 100"
    )
    embryos_transfered = st.number_input(
        label = "28.\tEnter  Embryos Transfered Value:",
        min_value = 0,
        max_value = 10,
        help = "Value range from 0 to 10"
    )
    
    
    # Create button to submit the form
    submitted = st.form_submit_button("Predict")

    # Condition when form submitted
    if submitted:
        # Create dict of all data in the form
        raw_data = {
            "patient_age_at_treatment": patient_age_at_treatment,
            "total_number_of_previous_ivf_cycles": total_number_of_previous_ivf_cycles,
            "total_number_of_ivf_pregnancies_total_number_of_ivf_pregnancies": total_number_of_ivf_pregnancies_total_number_of_ivf_pregnancies,
            "total_number_of_live_births_conceived_through_ivf": total_number_of_live_births_conceived_through_ivf,
            "type_of_infertility_female_primary": type_of_infertility_female_primary,
            "type_of_infertility_female_secondary": type_of_infertility_female_secondary,
            "type_of_infertility_male_primary": type_of_infertility_male_primary,
            "type_of_infertility_male_secondary": type_of_infertility_male_secondary,
            "type_of_infertility_couple_primary": type_of_infertility_couple_primary,
            "type_of_infertility_couple_secondary": type_of_infertility_couple_secondary,
            "cause_of_infertility_tubal_disease": cause_of_infertility_tubal_disease,
            "cause_of_infertility_ovulatory_disorder": cause_of_infertility_ovulatory_disorder,
            "cause_of_infertility_male_factor": cause_of_infertility_male_factor,
            "cause_of_infertility_patient_unexplained": cause_of_infertility_patient_unexplained,
            "cause_of_infertility_endometriosis": cause_of_infertility_endometriosis,
            "cause_of_infertility_cervical_factors": cause_of_infertility_cervical_factors,
            "cause_of_infertility_female_factors": cause_of_infertility_female_factors,
            "cause_of_infertility_partner_sperm_concentration": cause_of_infertility_partner_sperm_concentration,
            "cause_of_infertility_partner_sperm_morphology": cause_of_infertility_partner_sperm_morphology,
            "causes_of_infertility_partner_sperm_motility": causes_of_infertility_partner_sperm_motility,
            "cause_of_infertility_partner_sperm_immunological_factors": cause_of_infertility_partner_sperm_immunological_factors,
            "stimulation_used": stimulation_used,
            "fresh_cycle": fresh_cycle,
            "frozen_cycle": frozen_cycle,
            "eggs_thawed": eggs_thawed,
            "fresh_eggs_collected": fresh_eggs_collected,
            "eggs_mixed_with_partner_sperm": eggs_mixed_with_partner_sperm,
            "embryos_transfered": embryos_transfered
        }

        # Create loading animation while predicting
        with st.spinner("Sending data to prediction server ..."):
            res = requests.post("http://localhost:8080/predict", json = raw_data).json()

        # Parse the prediction result
        if res["error_msg"] != "":
            st.error("Error Occurs While Predicting: {}".format(res["error_msg"]))
        else:
            if res["res"] != 1:
                st.warning("Predicted IVF: GAGAL.")
            else:
                st.success("Predicted IVF: BERHASIL.")