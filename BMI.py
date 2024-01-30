def calculate_bmi(weight, height):
    # Calculate BMI using the formula
    bmi = weight / ((height / 100) ** 2)
    return bmi

def classify_bmi(bmi):
    # Classify BMI into categories based on standard ranges
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    print("---------------")

    try:
        # Getting user input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
    except ValueError:
        # Handle the case where the user enters non-numeric values
        print("Invalid input. Please enter numeric values for weight and height.")
        return

    # Validate that weight and height are positive values
    if weight <= 0 or height <= 0:
        print("Invalid input. Weight and height must be positive values.")
        return

    # Calculate BMI and classify into a category
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    # Display BMI result and category
    print("\nBMI Result:")
    print("BMI: {:.2f}".format(bmi))
    print("Category: {}".format(category))

if __name__ == "__main__":
    # Execute the main function if the script is run as the main program
    main()
