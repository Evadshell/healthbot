import tkinter as tk

# Define a dictionary of questions and possible responses
questions = {
    "Fever": ["Yes", "No"],
    "Cough or Cold": ["Yes", "No"],
    # Add more questions related to other symptoms here
}

# Define a function to calculate the diagnosis based on user responses
def calculate_diagnosis():
    fever_response = fever_var.get()
    cough_cold_response = cough_cold_var.get()

    # You can implement a more complex diagnosis logic here
    if fever_response == "Yes" and cough_cold_response == "Yes":
        diagnosis_label.config(text="Possible flu or viral infection")
    elif fever_response == "Yes":
        diagnosis_label.config(text="Fever")
    elif cough_cold_response == "Yes":
        diagnosis_label.config(text="Cough/Cold")
    else:
        diagnosis_label.config(text="No specific diagnosis")

# Create the main Tkinter window
root = tk.Tk()
root.title("Medical Diagnosis Chatbot")

# Create Tkinter variables to store user responses
fever_var = tk.StringVar()
cough_cold_var = tk.StringVar()

# Create a label and radio buttons for each question
for question, options in questions.items():
    question_label = tk.Label(root, text=question)
    question_label.pack()

    for option in options:
        radio_button = tk.Radiobutton(root, text=option, variable=fever_var if question == "Fever" else cough_cold_var, value=option)
        radio_button.pack()

# Create a button to calculate the diagnosis
calculate_button = tk.Button(root, text="Calculate Diagnosis", command=calculate_diagnosis)
calculate_button.pack()

# Create a label to display the diagnosis
diagnosis_label = tk.Label(root, text="")
diagnosis_label.pack()

# Start the Tkinter main loop
root.mainloop()
