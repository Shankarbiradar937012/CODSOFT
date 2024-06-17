def chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! Welcome to chatBot, How can I help you"
    elif "how are you" in user_input.lower():
        return "I'm just a machine, thanks for asking"
    elif "bye" in user_input.lower():
        return "goodbye! Have a nice day!"
    elif "hi" in user_input.lower():
        return "hi !! welcome to chatbot, How can I help you"
    elif "what is your name" in user_input.lower():
        return "my name is shankarchatBot."
    elif "how old are you" in user_input.lower():
        return "i am a machine, so i dont have age like human."
    else:
        return "I'm sorry, I didn't understand that."


while True:
    user_query = input("you: ")
    response = chatbot(user_query)
    print("chatbot:", response)
    if "bye" in user_query.lower():
        break
