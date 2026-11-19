def recognize_dialog_act(sentence):
    sentence = sentence.lower()

    if sentence.endswith("?"):
        return "Question"
    elif any(word in sentence for word in ["hello", "hi", "hey"]):
        return "Greeting"
    elif any(word in sentence for word in ["thanks", "thank you"]):
        return "Thanking"
    elif any(word in sentence for word in ["please", "could you", "can you"]):
        return "Request"
    elif any(word in sentence for word in ["bye", "goodbye"]):
        return "Farewell"
    else:
        return "Statement"

dialog = input("Enter a dialog: ")

print("Dialog Act:", recognize_dialog_act(dialog))
