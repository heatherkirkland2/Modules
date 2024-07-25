'''
Objective: 
The aim of this assignment is to assess your understanding and ability to implement 
Python modules, both built-in and custom, and to apply data handling techniques 
using Python's data structures and error handling.

Task 1: 
Your Mood Today - Problem Statement: 
Create a Python program using a custom module that asks the user how they are feeling
today and responds with a custom message based on the mood entered. - 
Code Example:

    # mood_responses.py
    def mood_response(mood):
        # Implement your response logic here

    # main.py
    import mood_responses
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))
- Expected Outcome: 
The program should be able to take a user's mood as input 
(e.g., happy, sad, excited) and return a corresponding custom message.
'''
# mood_responses.py
def mood_responses(mood):
    responses = {
        'happy': "That's wonderful! Keep smiling! 😊",
        'sad': "I'm sorry to hear that. I hope things get better soon. 🙁",
        'excited': "Excitement is contagious! What's got you so excited? 😃",
        'angry': "It's okay to feel angry sometimes. Take some deep breaths. 😡",
        'tired': "You've been working hard! Rest is important. 😴",
        'nervous': "It's natural to feel nervous. I believe in you! 🌟",
        'confused': "Confusion can be a step towards clarity. Hang in there! 🤔",
        'stressed': "Remember to take breaks and relax. You've got this! 💪",
        'overwhelmed': "Take things one step at a time. You're not alone! 🤗",
        'content': "Feeling content is a great state to be in. Enjoy the moment! 😌",
        'hopeful': "Hope is a powerful thing. May your hopes lead to success! 🌈",
        'grateful': "Gratitude brings positivity. It's great to hear you're feeling thankful! 🙏",
        # Add more moods and responses as needed
    }
    # Convert mood to lowercase and strip whitespace
    normalized_mood = mood.lower().strip()
    # Return the corresponding response or a default message
    return responses.get(normalized_mood, "I'm not sure what that mood means, but I'm here for you! 🤗")
mood = input("How are you feeling today? ").strip()
print(mood_responses.mood_responses(mood))
