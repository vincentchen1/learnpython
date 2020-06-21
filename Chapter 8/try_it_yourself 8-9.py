#8-9. Messages
text_messages = ['hey', 'what is up', 'how is it going']

def show_messages(text_messages):
    for text_message in text_messages:
        print(text_message)

show_messages(text_messages)


#8-10. Sending Messages
print()
text_messages = ['hey', 'what is up', 'how is it going']
sent_messages = []

def send_messages(text_messages, sent_messages):
    while text_messages:
        popped_message = text_messages.pop()
        print(f"This is the popped message: {popped_message}")
        sent_messages.append(popped_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

send_messages(text_messages, sent_messages)
show_sent_messages(sent_messages)

#8-11. Archived Mesages
print()

text_messages = ['hey', 'what is up', 'how is it going']
sent_messages = []

def send_messages(text_messages, sent_messages):
    while text_messages:
        popped_message = text_messages.pop()
        print(f"This is the popped message: {popped_message}")
        sent_messages.append(popped_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)


send_messages(text_messages[:], sent_messages)
show_sent_messages(sent_messages)

print()

print(text_messages)
print(sent_messages)
