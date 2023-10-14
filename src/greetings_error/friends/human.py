from datetime import datetime

from src.greetings.util.message import format


class Human:
    def __init__(self):
        self.phrase = "hello"

    def greet(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messages = [f"{self.phrase}.", f"The current time is {current_time}."]
        return format(messages)
