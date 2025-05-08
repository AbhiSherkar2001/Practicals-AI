Expert system (stock market)
def stock_trading_expert():
    print("=== Stock Market Trading Expert System ===")
    
    name = input("Enter your name: ")
    print(f"\nWelcome, {name}! Please answer the following questions:")

    market_trend = input("Is the market currently bullish (rising)? (yes/no): ").lower()
    company_growth = input("Is the company showing strong financial growth? (yes/no): ").lower()
    news_sentiment = input("Is the recent news about the company positive? (yes/no): ").lower()
    risk_tolerance = input("What is your risk tolerance? (low/medium/high): ").lower()

    print("\nAnalyzing your inputs...")

    if market_trend == "yes" and company_growth == "yes" and news_sentiment == "yes":
        if risk_tolerance == "high":
            advice = "Strong Buy – High growth expected, good for aggressive investors."
        elif risk_tolerance == "medium":
            advice = "Buy – Stock is favorable, but invest moderately."
        else:
            advice = "Consider Buying – Favorable conditions, but proceed cautiously."
    elif news_sentiment == "no" and risk_tolerance == "low":
        advice = "Avoid – Negative news and low risk tolerance do not mix."
    elif market_trend == "no":
        advice = "Hold or Sell – Bearish market, consider reducing exposure."
    else:
        advice = "Monitor – Conditions are mixed. Wait for clearer signals."

    print("\n=== Trading Suggestion ===")
    print(f"Name: {name}")
    print(f"Suggestion: {advice}")

if __name__ == "__main__":
    stock_trading_expert()  

What is it?
A Stock Market Trading Expert System is a rule-based AI tool that provides buy/sell/hold suggestions to users based on market conditions and user input.

🧠 Components:
Component                   	Description
Knowledge Base	Contains rules like “If market is bullish and company is growing → Buy.”
Inference Engine	Applies rules to the user's input to give recommendations
User Interface	           Accepts user inputs (e.g., market trend, company status) and gives output

✅ Applications:
Helps new investors make informed decisions
Reduces emotional bias in trading
Acts as a decision support tool for portfolio managers

⚙ Example Rules:
Condition	Action
Market is Bullish + Company Growth + Positive News → Buy	
Market is Bearish → Hold or Sell	
Bad News + Low Risk → Avoid	

🎯 Benefits:
Easy to use for beginners
Makes consistent decisions

Fast and cost-effective guidance
