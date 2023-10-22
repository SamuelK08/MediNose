from flask import Flask, render_template, request
import numpy as np
import pickle 
import joblib

model = joblib.load('svm_model.pkl')
app = Flask(__name__)

symptom_mapping = {
    'itching':1,
    'skin_rash':3,
    'nodal_skin_eruptions':4,
    'continuous_sneezing':4,
    'shivering':5,
    'chills':3,
    'joint_pain':3,
    'stomach_pain':5,
    'acidity':3,
    'ulcers_on_tongue':4,
    'muscle_wasting':3,
    'vomiting':5,
    'burning_micturition':6,
    'spotting_urination':6,
    'fatigue':4,
    'weight_gain':3,
    'anxiety':4,
    'cold_hands_and_feet':5,
    'mood_swings':3,
    'weight_loss':3,
    'restlessness':5,
    'lethargy':2,
    'patches_in_throat':6,
    'irregular_sugar_level':5,
    'cough':4,
    'high_fever':7,
    'sunken_eyes':3,
    'breathlessness':4,
    'sweating':3,
    'dehydration':4,
    'indigestion':5,
    'headache':3,
    'yellowish_skin':3,
    'dark_urine':4,
    'nausea':5,
    'loss_of_appetite':4,
    'pain_behind_the_eyes':4,
    'back_pain':3,
    'constipation':4,
    'abdominal_pain':4,
    'diarrhoea':6,
    'mild_fever':5,
    'yellow_urine':4,
    'yellowing_of_eyes':4,
    'acute_liver_failure':6,
    'fluid_overload':6,
    'swelling_of_stomach':7,
    'swelled_lymph_nodes':6,
    'malaise':6,
    'blurred_and_distorted_vision':5,
    'phlegm':5,
    'throat_irritation':4,
    'redness_of_eyes':5,
    'sinus_pressure':4,
    'runny_nose':5,
    'congestion':5,
    'chest_pain':7,
    'weakness_in_limbs':7,
    'fast_heart_rate':5,
    'pain_during_bowel_movements':5,
    'pain_in_anal_region':6,
    'bloody_stool':5,
    'irritation_in_anus':6,
    'neck_pain':5,
    'dizziness':4,
    'cramps':4,
    'bruising':4,
    'obesity':4,
    'swollen_legs':5,
    'swollen_blood_vessels':5,
    'puffy_face_and_eyes':5,
    'enlarged_thyroid':6,
    'brittle_nails':5,
    'swollen_extremeties':5,
    'excessive_hunger':4,
    'extra_marital_contacts':5,
    'drying_and_tingling_lips':4,
    'slurred_speech':4,
    'knee_pain':3,
    'hip_joint_pain':2,
    'muscle_weakness':2,
    'stiff_neck':4,
    'swelling_joints':5,
    'movement_stiffness':5,
    'spinning_movements':6,
    'loss_of_balance':4,
    'unsteadiness':4,
    'weakness_of_one_body_side':4,
    'loss_of_smell':3,
    'bladder_discomfort':4,
    'foul_smell_ofurine':5,
    'continuous_feel_of_urine':6,
    'passage_of_gases':5,
    'internal_itching':4,
    'toxic_look_(typhos)':5,
    'depression':3,
    'irritability':2,
    'muscle_pain':2,
    'altered_sensorium':2,
    'red_spots_over_body':3,
    'belly_pain':4,
    'abnormal_menstruation':6,
    'dischromic_patches':6,
    'watering_from_eyes':4,
    'increased_appetite':5,
    'polyuria':4,
    'family_history':5,
    'mucoid_sputum':4,
    'rusty_sputum':4,
    'lack_of_concentration':3,
    'receiving_blood_transfusion':5,
    'receiving_unsterile_injections':2,
    'coma':7,
    'stomach_bleeding':6,
    'distention_of_abdomen':4,
    'history_of_alcohol_consumption':5,
    'fluid_overload':4,
    'blood_in_sputum':5,
    'prominent_veins_on_calf':6,
    'palpitations':4,
    'painful_walking':2,
    'pus_filled_pimples':2,
    'blackheads':2,
    'scurring':2,
    'skin_peeling':3,
    'silver_like_dusting':2,
    'small_dents_in_nails':2,
    'inflammatory_nails':2,
    'blister':4,
    'red_sore_around_nose':2,
    'yellow_crust_ooze':3,
    'prognosis':5,
}

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/check_symptoms', methods=['post'])
def predict():
    #get the list of symptoms from the form
    selected_symptoms = request.form.getlist('symptoms')
    print(selected_symptoms)
    
    #create a zero-initialized array of length 17
    symptoms_array = np.zeros(17, dtype=int)
    
    #create a temporary list to store the values from symptom_mapping for the selected symptoms
    temp_values = [symptom_mapping[symptom] for symptom in selected_symptoms if symptom in symptom_mapping]

    #assign the values from temp_values to the beginning of symptoms_array
    symptoms_array[:len(temp_values)] = temp_values
    
    #print the modified symptoms_array
    print(symptoms_array.tolist())

    #reshape the array to match the input shape for the model
    symptoms_array = symptoms_array.reshape(1, -1)
    
    pred = model.predict(symptoms_array)
    return render_template('results.html', results=pred)

if __name__ == "__main__":
    app.run(debug=True)



