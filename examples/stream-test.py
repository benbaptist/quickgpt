from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

import sys

"""
Short example that shows quickGPT's streaming response capabilities.
"""

DO_STREAM = True

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread()

    # Start a fresh thread.
    thread.feed(
        System("Assist the user with their questions.")
    )

    while True:
        prompt = input("You: ")

        thread.feed(
            User(prompt)
        )

        response = thread.run(stream=DO_STREAM)

        if DO_STREAM:
            sys.stdout.write("Bot: ")

            for resp in response.message:
                sys.stdout.write(resp)
                sys.stdout.flush()

            print("")
        else:
            print("Bot: %s" % response.message)
