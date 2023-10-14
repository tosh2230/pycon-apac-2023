def format(messages):
    if isinstance(messages, list):
        return " ".join([message.capitalize() for message in messages])
    return messages.capitalize()
