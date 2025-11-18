def display_welcome():
    """Display program header"""
    print("=== Welcome to College Application Tracker! ===")
def get_college_count():
    """
    Get number of colleges user is applying to
    Return
        count (int)
    """
    num_colleges = input("How many colleges are you applying to? ")
    return int(num_colleges)

def get_application_costs(num_colleges):
    """
    Calculate total application cost

    Return
        total_cost (float)
    """
    application_cost = 50.00
    total_cost = application_cost * num_colleges
    return total_cost

def get_sat_score():
    """
    Get the user's SAT score

    Return:
        score (int)
    """
    score = input("SAT Score: ")
    return int(score)

def analyze_sat(score):
    """
    Provide feedback on SAT score
    >= 1400 - Excellent
    >= 1200 - Good Score
    >= 1000 - Solid Foundation
    else - Consider retaking to improve college options.
    """
    if score >= 1400:
        return "Excellent"
    elif score >= 1200:
        return "Good Score"
    elif score >= 1000:
        return "Solid Foundation"
    else:
        return "Consider retaking to improve college options."

def display_summary(num_colleges, total_cost, sat_score, sat_feedback):
    """
    Display summary of application information
    """
    print("\n=== Application Summary ===")
    print(f"Number of Colleges applied to: {num_colleges}")
    print(f"Total Application Cost: {total_cost}")
    print(f"SAT Score: {sat_score}")
    print(f"Feedback: {sat_feedback}")



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