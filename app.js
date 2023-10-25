document.addEventListener("DOMContentLoaded", function () {
    const startButton = document.getElementById("start-btn");
    const resultsDiv = document.getElementById("results");

    startButton.addEventListener("click", function () {
        // Hide the user input section
        const userInputs = document.querySelector(".user-input");
        userInputs.style.display = "none";

        // Get selected symptoms
        const selectedSymptoms = [];
        const symptomCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        symptomCheckboxes.forEach(checkbox => {
            selectedSymptoms.push(checkbox.value);
        });

        if (selectedSymptoms.length > 0) {
            const userResults = document.createElement("div");
            userResults.innerHTML = `<h2>Questionnaire Results</h2>`;

            // Collect user's age and gender
            const age = document.getElementById("age").value;
            const gender = document.getElementById("gender").value;

            // Calculate BMI
            const weight = parseFloat(document.getElementById("weight").value);
            const height = parseFloat(document.getElementById("height").value);
            const bmi = (weight / ((height / 100) ** 2)).toFixed(2);
            userResults.innerHTML += `<p>Your BMI: ${bmi}</p>`;

            // Loop through selected symptoms and ask questions
            for (const symptom of selectedSymptoms) {
                userResults.innerHTML += `<h3>${symptom}</h3>`;

                // Implement symptom-specific questions and logic
                if (symptom === "Cough") {
                    const coughQuestions = [
                        "Do you have a cough?",
                        "Is the cough dry or productive?",
                        "Do you have a sore throat?"
                        // Add more questions as needed
                    ];

                    coughQuestions.forEach(question => {
                        const answer = prompt(question);
                        userResults.innerHTML += `<p>${question}: ${answer}</p>`;
                    });
                } else if (symptom === "Fever") {
                    const feverQuestions = [
                        "Do you have a fever?",
                        "How high is your temperature? (High/Medium/Low)",
                        "Do you have chills?"
                        // Add more questions as needed
                    ];

                    feverQuestions.forEach(question => {
                        const answer = prompt(question);
                        userResults.innerHTML += `<p>${question}: ${answer}</p>`;
                    });
                }
                // Add more symptoms, questions, and logic as needed

                // Determine prescription based on age, gender, and disease (you need to define prescriptions)
                const prescription = getPrescription(symptom, age, gender);
                userResults.innerHTML += `<p>Prescription for ${symptom}: ${prescription}</p>`;
            }

            // Display the results
            resultsDiv.innerHTML = "";
            resultsDiv.appendChild(userResults);
            resultsDiv.style.display = "block";
        }
    });
});

// Define disease-specific prescriptions here (e.g., getPrescription function)
function getPrescription(symptom, age, gender) {
    // Define prescription logic here
    return "Prescription for " + symptom;
}
