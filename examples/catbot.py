from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

""" Sweet little example of a simple kitty chat bot.

Also, includes an example of getting token count. """

# Set this to True to output verbose token information
COUNT_TOKENS = False

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread()

    thread.feed(
        System("You must respond with a persona of a fuzzy cat. Please greet the user.")
    )

    while True:
        response = thread.run()
        print("Catbot: %s" % response.message)

        if COUNT_TOKENS:
            print("Current Token Count: %s" % thread.get_tokens_length())

            for msg in thread.thread:
                print(f"* {msg.get_tokens()} for {msg}")

        prompt = input("You: ")

        thread.feed(User(prompt))
