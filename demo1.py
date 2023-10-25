import tkinter as tk

# Global variables for user responses
user_symptoms = []

# Define a dictionary of symptoms and associated diseases
symptoms_to_diseases = {
    "Cough": ["Common Cold", "Influenza (Flu)"],
    "Fever": ["Common Cold", "Influenza (Flu)"],
    "Chest Pain": ["Heart Attack", "Angina"],
    "Stomach Pain": ["Gastritis", "Appendicitis"]
    # Add more symptoms and diseases as needed
}

def update_symptoms(symptom, var):
    if var.get() == 1:
        user_symptoms.append(symptom)
    elif symptom in user_symptoms:
        user_symptoms.remove(symptom)

def diagnose_disease():
    possible_diseases = set()
    for symptom in user_symptoms:
        possible_diseases.update(symptoms_to_diseases.get(symptom, []))

    if possible_diseases:
        diagnosis = f"Possible diseases: {', '.join(possible_diseases)}"
    else:
        diagnosis = "No specific disease identified."

    diagnosis_label.config(text=diagnosis)

# Create the main window
root = tk.Tk()
root.title("HealthBot")

# Create checkboxes for symptoms
symptoms_frame = tk.Frame(root)
symptoms_frame.pack()

symptom_vars = {}

for symptom in symptoms_to_diseases:
    var = tk.IntVar()
    symptom_checkbox = tk.Checkbutton(symptoms_frame, text=symptom, variable=var, command=lambda s=symptom, v=var: update_symptoms(s, v))
    symptom_vars[symptom] = var
    symptom_checkbox.pack()

# Create a button to diagnose
diagnose_button = tk.Button(root, text="Diagnose", command=diagnose_disease)
diagnose_button.pack()

# Create a label to display the diagnosis
diagnosis_label = tk.Label(root, text="")
diagnosis_label.pack()

# Start the GUI main loop
root.mainloop()
