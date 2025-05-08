Expert system (employee)
def evaluate_employee():
    print("=== Expert System: Employee Performance Evaluation ===")
    
    name = input("Enter Employee Name: ")
    role = input("Enter Role/Department: ")
    
    print("\nRate the following on a scale of 1 (Poor) to 5 (Excellent):")
    teamwork = int(input("Teamwork: "))
    punctuality = int(input("Punctuality: "))
    task_completion = int(input("Task Completion: "))
    communication = int(input("Communication Skills: "))
    problem_solving = int(input("Problem Solving: "))
    leadership = int(input("Leadership (if applicable, else rate as 3): "))

    total_score = teamwork + punctuality + task_completion + communication + problem_solving + leadership
    average_score = total_score / 6

    if average_score >= 4.5:
        remark = "Outstanding"
        suggestion = "Keep up the great work. Consider for leadership roles or promotions."
    elif average_score >= 3.5:
        remark = "Good"
        suggestion = "Consistent performance. Minor improvements will boost further."
    elif average_score >= 2.5:
        remark = "Average"
        suggestion = "Needs improvement in some areas. Consider targeted training."
    else:
        remark = "Below Average"
        suggestion = "Immediate attention needed. Schedule a performance review and support plan."

    print("\n=== Performance Report ===")
    print(f"Employee Name: {name}")
    print(f"Department/Role: {role}")
    print(f"Average Score: {average_score:.2f}/5")
    print(f"Performance Remark: {remark}")
    print(f"Recommendation: {suggestion}")


if __name__ == "__main__":
    evaluate_employee()  


theory
This program acts as a simple expert system that evaluates an employee's performance based on ratings given for key attributes. It automates feedback and suggestions using logical conditions and scoring.

🔁 Working Process:
User Input:
Asks for:
Employee Name
Role or Department
Then, the evaluator provides ratings (1 to 5) on:
Teamwork
Punctuality
Task Completion
Communication Skills
Problem Solving
Leadership (or default as 3)

Score Calculation:

Total score is the sum of all 6 ratings.
Average score is calculated by dividing the total score by 6.
Evaluation Logic (Rule-Based):
Based on the average score:
≥ 4.5: Outstanding – promotion-worthy
≥ 3.5: Good – slight improvements recommended
≥ 2.5: Average – needs improvement/training
< 2.5: Below Average – requires urgent review

Output Report:
Displays:
Name and Role
Average score
Performance remark
Personalized recommendation

🧠 Key Concepts Used:
Expert System Logic: Uses fixed rules to provide automated evaluations and suggestions.
Simple AI Evaluation: Mimics basic Human Resource evaluation methods.

Condition-based Feedback: Uses if-elif statements to classify performance.

