Expert system
# Simple Expert System for Help Desk Management

def help_desk_system():
    print("=== Expert System: Help Desk Management Assistant ===")

    issues_db = {
        "password reset": "To reset your password, click on 'Forgot Password' and follow the instructions.",
        "internet issue": "Try restarting your router. If the issue persists, contact the IT department.",
        "email not working": "Check your network. Then try logging in from a different browser.",
        "system slow": "Close unused programs and restart your system. Clear cache and check for updates.",
        "printer not working": "Check power connection, paper tray, and ink levels. Reinstall printer drivers if needed.",
        "software installation": "Ensure you have admin rights. Contact IT for software approval and installation."
    }

    while True:
        query = input("\nEnter your issue (or type 'exit'): ").lower()

        if query == "exit":
            print("Thank you for contacting the Help Desk Assistant!")
            break
        elif query in issues_db:
            print("Solution:", issues_db[query])
        else:
            print("Sorry, I don't have a solution for that issue. Please contact the IT support team directly.")

if __name__ == "__main__":
    help_desk_system() 

theory
What is Help Desk Management?
Help Desk Management refers to providing technical support and guidance to users facing issues with IT systems, software, or hardware.

🧠 Role of an Expert System in Help Desk:
Problem Identification:
Recognizes keywords related to common issues.

Solution Suggestion:
Offers predefined solutions or next steps.

Reduces Load on Human Agents:
Handles basic queries automatically, saving time.

⚙️ Main Features of Help Desk Expert System:
Feature	                                  Description
Knowledge Base	Contains FAQs and solutions for common problems.
Inference Engine	Matches user queries with solutions using pattern recognition.
User Interface	                Text interface for user input and system replies.

✅ Advantages:
24/7 availability

Instant responses to common problems
Reduces workload for IT staff
Increases user satisfaction and efficiency
