import random

responses= {
    "greeting": ["hello, how can i help you?", "Hello Welcome to our grocery shop","Hi, how can i assist you?"],
    "farewell":["Good bye, have a great day","Thank you for visiting","Take Care"],
    "thanks":["you're welcome", "No problem", "My Pleasure"],
    "products":["We have dairy Products","We have fresh food and vegetables","We also contains the bakery products"],
    "opening_hours":["We are open from 9 AM to 10 PM Monday to Saturday", "Our store hours are from 8:00 AM to 9:00 PM every day except Sunday.","We open at 7:00 AM and close at 10:00 PM, Monday through Friday."],
    "default": ["could you please rephrase that?", "I am unsure about what you are asking","I am sorry, i didn't understand that"],
    "location":["our shop is at akurdi","You can find us near akurdi railway station", "We are situated in shopping plaza in akurdi"]
}
def get_responses(user_input):
    if user_input in ["hi","hello" ,"hii"]:
        return random.choice(responses["greeting"])
    elif user_input in ["bye","good bye"]:
        return random.choice(responses["farewell"])
    elif "hours" in user_input or "open" in user_input or "close" in user_input:
        return random.choice(responses["opening_hours"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    elif "location" in user_input or "address" in user_input:
        return random.choice(responses["location"])
    elif "product" in user_input or "grocery" in user_input:
        return random.choice(responses["products"])
    else:
        return random.choice(responses["default"])




def main():
    print("Welcome to the grocery shop chatbot")
    while True:
        user_input= input("You : ").lower()
        if(user_input=="exit"):
            print("Thank you")
            break
        else:
            response= get_responses(user_input)
            print("Bot :", response)


if __name__== "__main__":
    main()