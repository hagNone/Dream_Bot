import google.generativeai as genai

API_KEY = "AIzaSyBjB_TNG1aCJvW8vbfXBLk7QON2cu1NUq0"  

if not API_KEY:
    print("Error: API key is missing. Please provide a valid API key.")
    exit()

# Configure Gemini AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_dream_gemini(dream_text, mode="analysis"):
    """Analyzes or extends a dream based on user choice."""
    
    prompts = {
        "analysis": f"Analyze the following dream: {dream_text}\nProvide a psychological and symbolic interpretation.",
        "story": f"Expand and complete this dream story in a realistic yet simple way: {dream_text}"
    }
    
    if mode not in prompts:
        return " Invalid mode selected. Please choose 'story' or 'analysis'."

    try:
        response = model.generate_content(prompts[mode])
        return response.text.strip().replace("*", "").replace("**", "")  # Remove unnecessary formatting
    except Exception as e:
        return f" Error occurred: {str(e)}"

if __name__ == "__main__":
    print("\nWelcome to the Dream Interpreter! 💤\n")
    
    choice_1 = input("Do you have a dream to share? (Yes/No): ").strip().lower()

    if choice_1 == "yes":
        dream_input = input("\nAwesome! Tell me about your dream: ").strip()
        
        choice_2 = input("\nWould you like an analysis or a story extension? (Enter 'analysis' or 'story'): ").strip().lower()
        
        if choice_2 in ["story", "analysis"]:
            result = analyze_dream_gemini(dream_input, mode=choice_2)
            print("\n Here’s your result:\n")
            print(result)
        else:
            print("\n Invalid choice. Please enter 'story' or 'analysis'.")

    elif choice_1 == "no":
        print("\nNo worries! If you remember a dream later, feel free to share. ")

    else:
        print("\n Invalid input. Please enter 'Yes' or 'No'.")
 
