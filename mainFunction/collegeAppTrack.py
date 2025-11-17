def display_welcome():
    """Display program header"""
    print("Welcome to College Application Tracker!")
def get_college_count():
    """
    Get number of colleges user is applying to
    Return
        count (int)
    """
    count_str = input("How many colleges are you applying to? ")
    count = int(count_str)

def get_application_costs(num_colleges):
    """
    Calculate total application cost

    Return
        total_cost (float)
    """
    application_cost = 50.00
    totalCost = application_cost * count
    total_cost = float(totalCost)
    return total_cost

def get_sat_score():
    """
    Get the user's SAT score

    Return:
        score (int)
    """
    score = int(input("SAT Score: "))

def analyze_sat(score):
    """
    Provide feedback on SAT score
    >= 1400 - Excellent
    >= 1200 - Good Score
    >= 1000 - Solid Foundation
    else - Consider retaking to improve college options.
    """
    if score >= 1400:
        print("Excellent")
    elif score >= 1200:
        print("Good Score")
    elif score >= 1000:
        print("Solid Foundation")
    else:
        print("Consider retaking to improve college options.")

def display_summary(colleges, cost, sat_score, sat_feedback):
    """
    Display summary of application information
    """
    print("\nCollege Count: " + str(colleges))
    print("Cost: $" + str(cost))
    print("SAT Score: " + str(sat_score))
    print("SAT Feedback: " + sat_feedback)



def main():
    """Main function - orchestrates the entire program"""
    # Welcome the User
    display_welcome()

    # collect information
    num_colleges = get_college_count()
    total_cost = get_application_costs(num_colleges)
    sat = get_sat_score()

    # Analyze data
    feedback = analyze_sat(sat)

    # Display results
    display_summary(num_colleges, total_cost, sat, feedback)

    print("\nGood luck wiuth your applications")



# entry point
if __name__ == "__main__":
    main()