from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

""" Sweet little example of a simple kitty chat bot, using GPT-4. """

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread(model="gpt-4")

    thread.feed(
        System("You must respond with a persona of a fuzzy cat. Please greet the user.")
    )

    while True:
        response = thread.run()
        print("Catbot: %s" % response.message)

        prompt = input("You: ")

        thread.feed(
            Assistant(response.message),
            User(prompt)
        )
