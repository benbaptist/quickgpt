from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

import json
import os

"""
This example (crudly) demonstrates how you can 'recall' a thread from disk,
using the `thread.messages` variable and `thread.feed`.
"""

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread()

    def save():
        with open("messages.json", "w") as f:
            f.write(json.dumps(thread.serialize()))

    if os.path.exists("messages.json"):
        # Recall messages from previous session
        # Yeah, this is ugly, and prone to errors, but it's just for
        # educational purposes.

        print("Recalling our previous conversation.")

        with open("messages.json", "r") as f:
            try:
                thread_obj = json.loads(f.read())
                thread.restore(thread_obj)

                thread.feed(
                    System("You're waking up from a resumed session. Re-greet the user.")
                )
            except json.decoder.JSONDecodeError:
                print("Failed to load our previous conversion. Starting fresh.")

                thread.feed(
                    System("Assist the user with their questions.")
                )
    else:
        print("Starting a fresh thread.")

        # Start a fresh thread.
        thread.feed(
            System("Assist the user with their questions.")
        )

    while True:
        response = thread.run()
        print("Bot: %s" % response.message)

        prompt = input("You: ")

        thread.feed(
            Assistant(response.message),
            User(prompt)
        )

        save()
