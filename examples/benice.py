from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

""" Example using OpenAI's Moderation API to verify that the
prompt does not violate their ToS. """

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread()

    thread.feed(
        System("Don't let the user be mean to you!")
    )

    while True:
        response = thread.run()
        print(response)

        prompt = None

        while not prompt:
            prompt = input("<You> ")

            if thread.moderate(prompt)["flagged"]:
                print("Sorry, I can't let you say that. Try again.")

                prompt = None
                continue

        thread.feed(
            Assistant(response.message),
            User(prompt)
        )
