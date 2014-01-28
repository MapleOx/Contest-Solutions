# A dictionary for translating text lingo
txt_dict = {"CU": "see you", ":-)": "I'm happy", ":-(": "I'm unhappy", ';-)': 'wink',
            ':-P': 'stick out my tongue', '(~.~)': 'sleepy', 'TA': 'totally awesome',
            'CCC': 'Canadian Computing Competition', 'CUZ': 'because', 'TY': 'thank-you',
            'YW': "you're welcome", 'TTYL': 'talk to you later'}
while True:
    # Asks user for input and outputs corresponding translation 
    user_input = input("Enter phrase> ")
    if user_input in txt_dict:
        print(txt_dict[user_input])
    else:
        print (user_input)
    # Ends conversation when user inputs "TTYL"
    if user_input == "TTYL":
        break
