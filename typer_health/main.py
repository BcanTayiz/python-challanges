import typer

app = typer.Typer()


@app.command()
def calculate_bmi(weight_kg: float, height_m: float):
    if weight_kg <= 0 or height_m <= 0:
        return "Invalid input. Weight and height must be positive numbers."

    bmi = weight_kg / (height_m ** 2)
    print(bmi)

@app.command()
def calculate_bmr(weight_kg:float, height_m:float, age:float, gender:str):
    """
    Calculate Basal Metabolic Rate (BMR) using weight in kilograms, height in meters, age, and gender.
    (Mifflin-St Jeor Equation)
    """
    if weight_kg <= 0 or height_m <= 0:
        return "Invalid input. Weight and height must be positive numbers."
    if age <= 0:
        return "Invalid input. Age must be a positive number."
    
    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_m * 100 - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight_kg + 6.25 * height_m * 100 - 5 * age - 161
    else:
        return "Invalid input. Gender must be 'male' or 'female'."
    
    print(bmr)

@app.command()
def calculate_body_fat_percentage(weight_kg:float, height_m:float, age:float, gender:str):
    """
    Calculate body fat percentage using weight in kilograms, height in meters, age, and gender.
    (Note: This is a simple example and may not be highly accurate.)
    """
    if weight_kg <= 0 or height_m <= 0:
        return "Invalid input. Weight and height must be positive numbers."
    if age <= 0:
        return "Invalid input. Age must be a positive number."
    
    # Example formula (for demonstration purposes, not highly accurate)
    if gender.lower() == 'male':
        body_fat_percentage = 0.2 * age + 0.25
    elif gender.lower() == 'female':
        body_fat_percentage = 0.2 * age + 0.32
    else:
        return "Invalid input. Gender must be 'male' or 'female'."
    
    print(body_fat_percentage)


@app.command()
def analyze_blood_test(hemoglobin:float, white_blood_cells:float, platelets:float, glucose:float, cholesterol:float, triglycerides:float):
    """
    Analyze blood test results and print if the patient is sick or not.
    Adjust the parameter ranges based on medical guidelines.
    """
    # Example parameter ranges (arbitrary values for demonstration)
    hemoglobin_range = (12, 16)  # g/dL
    white_blood_cells_range = (4, 11)  # x10^3/μL
    platelets_range = (150, 450)  # x10^3/μL
    glucose_range = (70, 100)  # mg/dL
    cholesterol_range = (120, 200)  # mg/dL
    triglycerides_range = (50, 150)  # mg/dL

    # Check if values are within normal ranges
    hemoglobin_normal = hemoglobin_range[0] <= hemoglobin <= hemoglobin_range[1]
    white_blood_cells_normal = white_blood_cells_range[0] <= white_blood_cells <= white_blood_cells_range[1]
    platelets_normal = platelets_range[0] <= platelets <= platelets_range[1]
    glucose_normal = glucose_range[0] <= glucose <= glucose_range[1]
    cholesterol_normal = cholesterol_range[0] <= cholesterol <= cholesterol_range[1]
    triglycerides_normal = triglycerides_range[0] <= triglycerides <= triglycerides_range[1]

    # Print analysis based on blood test results
    if all([hemoglobin_normal, white_blood_cells_normal, platelets_normal,
            glucose_normal, cholesterol_normal, triglycerides_normal]):
        print("Patient's blood test results are within normal ranges. No apparent issues.")
    else:
        print("Warning: Abnormal blood test results. Further medical evaluation may be needed.")



@app.command()
def goodbye():
    print("Goodbye")


if __name__ == "__main__":
    app()