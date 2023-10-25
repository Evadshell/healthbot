import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox
from tkinter.simpledialog import askstring

app = tk.Tk()
app.title("HealthBot")
style = ThemedStyle(app)
style.set_theme("radiance")

# Dictionary of languages
languages = {
    "English": {
        "name_question": "Enter your name:",
        "language_question": "Select your language:",
        "age_question": "Enter your age:",
        "gender_question": "Select your gender:",
        "blood_group_question": "Select your blood group:",
        "health_disease_question": "Do you have any serious health conditions?",
        "allergy_question": "Do you have any allergies?",
    },
    "Hindi": {
        "name_question": "अपना नाम दर्ज करें:",
        "language_question": "अपनी भाषा चुनें:",
        "age_question": "अपनी आयु दर्ज करें:",
        "gender_question": "अपना लिंग चुनें:",
        "blood_group_question": "अपना रक्त समूह चुनें:",
        "health_disease_question": "क्या आपकी सारीरिक स्वास्थ्य स्थितियों में कोई गंभीर समस्या है?",
        "allergy_question": "क्या आपकी कोई एलर्जी है?",
    },
    # Add more languages as needed
}

# User details
name_var = tk.StringVar()
language_var = tk.StringVar(value=list(languages.keys())[0])
age_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")
blood_group_var = tk.StringVar()
health_disease_var = tk.StringVar(value="No")
allergy_var = tk.StringVar(value="None")
weight_var = tk.DoubleVar()
height_var = tk.DoubleVar()

# Health issues and questions
questions = {
    "Cough": [
        "Do you have a cough?",
        "Is the cough dry or productive?",
        "Do you have a sore throat?",
    ],
    "Fever": [
        "Do you have a fever?",
        "How high is your temperature? (High/Medium/Low)",
        "Do you have chills?",
    ],
    "Chest Pain": [
        "Do you experience chest pain?",
        "Is the pain sharp or dull?",
        "Is the pain radiating?",
    ],
    "Heart Palpitations": [
        "Do you have heart palpitations?",
        "How often do they occur? (Frequent/Occasional/Rare)",
    ],
    "Stomach Pain": [
        "Do you have stomach pain?",
        "Is the pain continuous or intermittent?",
        "Do you have nausea?",
    ],
    "Headache": [
        "Do you have a headache?",
        "Is the headache severe or mild?",
        "Is the headache throbbing?",
    ],
    "Shortness of Breath": [
        "Do you experience shortness of breath?",
        "Is it constant or occasional?",
        "Do you have a cough along with it?",
    ],
    # Add more health issues and questions as needed
}

# Mapping of symptoms to diseases, precautions, and medicines
symptom_mappings = {
    "Cough": {
        "Disease": "Common Cold",
        "Precautions": "Rest, drink fluids, and take OTC cold medication.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's cough syrup",
                "19-40": "Adult cough syrup",
                "41-60": "Cough syrup plus antibiotics",
                "61+": "Cough syrup for seniors",
            },
            "Female": {
                "Under 18": "Children's cough syrup",
                "19-40": "Adult cough syrup",
                "41-60": "Cough syrup plus antibiotics",
                "61+": "Cough syrup for seniors",
            },
        },
        "Color": "blue",
    },
    "Fever": {
        "Disease": "Influenza (Flu)",
        "Precautions": "Rest, drink fluids, and take antiviral medication if prescribed.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's fever reducer",
                "19-40": "Adult fever reducer",
                "41-60": "Fever reducer plus antiviral",
                "61+": "Fever reducer for seniors",
            },
            "Female": {
                "Under 18": "Children's fever reducer",
                "19-40": "Adult fever reducer",
                "41-60": "Fever reducer plus antiviral",
                "61+": "Fever reducer for seniors",
            },
        },
        "Color": "red",
    },
    "Chest Pain": {
        "Disease": "Heart Attack",
        "Precautions": "Call 112, take aspirin if recommended.",
        "Medicines": {
            "Male": {
                "Under 18": "Not recommended",
                "19-40": "Aspirin",
                "41-60": "Aspirin and nitroglycerin",
                "61+": "Aspirin and nitroglycerin for seniors",
            },
            "Female": {
                "Under 18": "Not recommended",
                "19-40": "Aspirin",
                "41-60": "Aspirin and nitroglycerin",
                "61+": "Aspirin and nitroglycerin for seniors",
            },
        },
        "Color": "orange",
    },
    "Heart Palpitations": {
        "Disease": "Arrhythmia",
        "Precautions": "See a cardiologist for evaluation.",
        "Medicines": {
            "Male": {
                "Under 18": "Not recommended",
                "19-40": "Antiarrhythmic medications",
                "41-60": "Antiarrhythmic medications and beta-blockers",
                "61+": "Antiarrhythmic medications and beta-blockers for seniors",
            },
            "Female": {
                "Under 18": "Not recommended",
                "19-40": "Antiarrhythmic medications",
                "41-60": "Antiarrhythmic medications and beta-blockers",
                "61+": "Antiarrhythmic medications and beta-blockers for seniors",
            },
        },
        "Color": "purple",
    },
    "Stomach Pain": {
        "Disease": "Gastritis",
        "Precautions": "Avoid spicy foods, take antacids.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's antacids",
                "19-40": "Adult antacids",
                "41-60": "Antacids and proton pump inhibitors",
                "61+": "Antacids and proton pump inhibitors for seniors",
            },
            "Female": {
                "Under 18": "Children's antacids",
                "19-40": "Adult antacids",
                "41-60": "Antacids and proton pump inhibitors",
                "61+": "Antacids and proton pump inhibitors for seniors",
            },
        },
        "Color": "green",
    },
    "Headache": {
        "Disease": "Tension Headache",
        "Precautions": "Relax, apply hot/cold compress.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's pain relievers",
                "19-40": "Adult pain relievers",
                "41-60": "Pain relievers and muscle relaxants",
                "61+": "Pain relievers and muscle relaxants for seniors",
            },
            "Female": {
                "Under 18": "Children's pain relievers",
                "19-40": "Adult pain relievers",
                "41-60": "Pain relievers and muscle relaxants",
                "61+": "Pain relievers and muscle relaxants for seniors",
            },
        },
        "Color": "yellow",
    },
    "Shortness of Breath": {
        "Disease": "Asthma",
        "Precautions": "Use inhalers as prescribed, avoid triggers.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's inhaler",
                "19-40": "Adult inhaler",
                "41-60": "Inhaler and corticosteroids",
                "61+": "Inhaler and corticosteroids for seniors",
            },
            "Female": {
                "Under 18": "Children's inhaler",
                "19-40": "Adult inhaler",
                "41-60": "Inhaler and corticosteroids",
                "61+": "Inhaler and corticosteroids for seniors",
            },
        },
        "Color": "pink",
    },
    "Back Pain": {
        "Disease": "Muscle Strain",
        "Precautions": "Rest, apply ice/heat, perform gentle stretches.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's pain relievers",
                "19-40": "Adult pain relievers",
                "41-60": "Pain relievers and muscle relaxants",
                "61+": "Pain relievers and muscle relaxants for seniors",
            },
            "Female": {
                "Under 18": "Children's pain relievers",
                "19-40": "Adult pain relievers",
                "41-60": "Pain relievers and muscle relaxants",
                "61+": "Pain relievers and muscle relaxants for seniors",
            },
        },
        "Color": "light blue",
    },
    "Joint Pain": {
        "Disease": "Arthritis",
        "Precautions": "Regular exercise, maintain a healthy weight.",
        "Medicines": {
            "Male": {
                "Under 18": "Children's pain relievers",
                "19-40": "Adult pain relievers",
                "41-60": "Pain relievers and disease-modifying antirheumatic drugs",
                "61+": "Pain relievers and disease-modifying antirheumatic drugs for seniors",
            },
            "Female": {
                "Under 18": "Children's pain relievers",
                "19-40": "Adult pain relievers",
                "41-60": "Pain relievers and disease-modifying antirheumatic drugs",
                "61+": "Pain relievers and disease-modifying antirheumatic drugs for seniors",
            },
        },
        "Color": "brown",
    },
    # Add more mappings as needed
}

# Slots for selected health issues
selected_issues = []

# Message box counter
message_box_counter = 0

def next_message_box():
    global message_box_counter
    message_box_counter += 1
    return message_box_counter

# Custom Message Box Class
class CustomMessageBox:
    def __init__(self, title, message):
        self.root = tk.Toplevel()
        self.root.title(title)
        style = ThemedStyle(self.root)
        style.set_theme("plastik")

        # Customize font
        custom_font = ("Helvetica", 12)

        tk.Label(
            self.root,
            text=message,
            font=custom_font,
        ).pack(padx=10, pady=10)

        ok_button = ttk.Button(self.root, text="OK", command=self.root.destroy)
        ok_button.pack(pady=10)

    def run(self):
        self.root.mainloop()

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        return None
    return round((weight / ((height / 100) ** 2)), 1)

def prescribe_medication(age_group, gender, symptoms, allergy):
    prescribed_meds = set()
    prescribed_precautions = set()
    for symptom in symptoms:
        mapping = symptom_mappings.get(symptom)
        if mapping:
            medicines = mapping["Medicines"][gender].get(age_group, "None")
            precautions = mapping["Precautions"]

            if medicines != "None":
                prescribed_meds.add(medicines)
            prescribed_precautions.add(precautions)

    return ", ".join(prescribed_meds), ", ".join(prescribed_precautions)

def select_issue(issue):
    if issue in selected_issues:
        selected_issues.remove(issue)
    else:
        selected_issues.append(issue)

def start_questionnaire():
    user_name = name_var.get()
    selected_language = language_var.get()
    age = age_var.get()
    gender = gender_var.get()
    blood_group = blood_group_var.get()
    has_health_disease = health_disease_var.get()
    allergy = allergy_var.get()
    weight = weight_var.get()
    height = height_var.get()

    # Check if the user provided age, blood group, and health disease info
    if not age or not blood_group:
        messagebox.showwarning("Missing Information", "Please provide your age and blood group.")
        return

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    bmi_message = ""
    if bmi is not None:
        bmi_message = f"\nBMI: {bmi}"
        if bmi < 18.5:
            bmi_message += "\nWarning: Your BMI is too low."
        elif bmi >= 25:
            bmi_message += "\nWarning: Your BMI is too high."
    
    # Prepare user details message
    user_details = f"Name: {user_name}\nLanguage: {selected_language}\nAge: {age}\nGender: {gender}\nBlood Group: {blood_group}"
    if has_health_disease:
        user_details += "\nHas Serious Health Disease: Yes"
    else:
        user_details += "\nHas Serious Health Disease: No"
    user_details += f"\nAllergies: {allergy}{bmi_message}"

    # Get selected issues and map to diseases, precautions, and medicines
    age_group = age_group_selector(int(age))
    selected_issues_text = "\nSelected Issues: " + ", ".join(selected_issues)

    # Check if any health issues are selected
    if not selected_issues:
        messagebox.showwarning("No Health Issues Selected", "Please select at least one health issue.")
        return

    message = user_details + selected_issues_text
    for symptom in selected_issues:
        ask_symptom_questions(symptom)
        prescribed_medicines, prescribed_precautions = prescribe_medication(age_group, gender, [symptom], allergy)
        message += f"\n\nFor {symptom}:\nPrescribed Medicines: {prescribed_medicines}\nPrecautions: {prescribed_precautions}"

    show_custom_message_box("Prescription", message)

def age_group_selector(age):
    if age < 16:
        return "Under 18"
    elif 16 <= age <= 30:
        return "19-40"
    elif 31 <= age <= 50:
        return "41-60"
    else:
        return "61+"

def ask_symptom_questions(symptom):
    symptom_questions = questions.get(symptom)
    if symptom_questions:
        for idx, question in enumerate(symptom_questions, start=1):
            answer = askstring(f"Question {idx}", question)
            if not answer:
                messagebox.showwarning("Missing Information", "Please provide answers to all questions.")
                return
        messagebox.showinfo("Information", "Thank you for providing the answers to the symptom-specific questions.")

# Create and configure the main frame
frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Language Selection
language_label = ttk.Label(frame, text=languages["English"]["language_question"])
language_label.grid(column=0, row=0, sticky=tk.W)
language_combo = ttk.Combobox(frame, textvariable=language_var, values=list(languages.keys()))
language_combo.grid(column=1, row=0, sticky=tk.W)

# Name Entry
name_label = ttk.Label(frame, text=languages["English"]["name_question"])
name_label.grid(column=0, row=1, sticky=tk.W)
name_entry = ttk.Entry(frame, textvariable=name_var)
name_entry.grid(column=1, row=1, sticky=tk.W)

# Age Entry
age_label = ttk.Label(frame, text=languages["English"]["age_question"])
age_label.grid(column=0, row=2, sticky=tk.W)
age_entry = ttk.Entry(frame, textvariable=age_var)
age_entry.grid(column=1, row=2, sticky=tk.W)

# Gender Selection
gender_label = ttk.Label(frame, text=languages["English"]["gender_question"])
gender_label.grid(column=0, row=3, sticky=tk.W)
gender_combo = ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combo.grid(column=1, row=3, sticky=tk.W)

# Blood Group Selection
blood_group_label = ttk.Label(frame, text=languages["English"]["blood_group_question"])
blood_group_label.grid(column=0, row=4, sticky=tk.W)
blood_group_combo = ttk.Combobox(
    frame, textvariable=blood_group_var, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)
blood_group_combo.grid(column=1, row=4, sticky=tk.W)

# Health Disease Checkbox
health_disease_check = ttk.Checkbutton(frame, text=languages["English"]["health_disease_question"], variable=health_disease_var)
health_disease_check.grid(column=0, row=5, columnspan=2, sticky=tk.W)

# Allergy Entry
allergy_label = ttk.Label(frame, text=languages["English"]["allergy_question"])
allergy_label.grid(column=0, row=6, sticky=tk.W)
allergy_entry = ttk.Entry(frame, textvariable=allergy_var)
allergy_entry.grid(column=1, row=6, sticky=tk.W)

# Weight Entry
weight_label = ttk.Label(frame, text="Enter your weight (kg):")
weight_label.grid(column=0, row=7, sticky=tk.W)
weight_entry = ttk.Entry(frame, textvariable=weight_var)
weight_entry.grid(column=1, row=7, sticky=tk.W)

# Height Entry
height_label = ttk.Label(frame, text="Enter your height (cm):")
height_label.grid(column=0, row=8, sticky=tk.W)
height_entry = ttk.Entry(frame, textvariable=height_var)
height_entry.grid(column=1, row=8, sticky=tk.W)

# Start Questionnaire Button
start_button = ttk.Button(frame, text="Start Questionnaire", command=start_questionnaire)
start_button.grid(column=0, row=9, columnspan=2)

def show_custom_message_box(title, message):
    custom_message_box = CustomMessageBox(title, message)
    custom_message_box.run()

# Health Issue Selection Frame
issues_frame = ttk.LabelFrame(app, text="Select Health Issues")
issues_frame.grid(column=1, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

for issue in questions:
    ttk.Checkbutton(issues_frame, text=issue, command=lambda issue=issue: select_issue(issue)).pack(anchor=tk.W)

app.mainloop()