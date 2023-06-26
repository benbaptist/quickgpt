from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

import sys

"""
Short example that shows quickGPT's streaming response capabilities, alongside
basic function support as well.
"""

DO_STREAM = True

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread()

    def addition(a, b):
        a, b = int(a), int(b)

        return a + b

    thread.add_function(
        method=addition,
        description="Add two numbers together and get a result.",
        properties={
            "a": {
                "type": "integer",
                "description": "First number to add."
            },
            "b": {
                "type": "integer",
                "description": "Second number to add."
            }
        },
        required=["a", "b"]
    )

    fresh_iter = True

    while True:

        if fresh_iter:
            # prompt = input("You: ")
            prompt = "What is 5+5?"

            thread.feed(
                User(prompt)
            )

        response = thread.run(stream=DO_STREAM)

        if DO_STREAM:
            sys.stdout.write("Bot: ")

            if type(response) == Function:
                print("[executed function]")
                fresh_iter = False
                continue
            else:

                for resp in response.message:

                    if type(resp) == str:
                        sys.stdout.write(resp)
                        sys.stdout.flush()

                print("")

                fresh_iter = True
        else:
            print("Bot: %s" % response.message)

        break
