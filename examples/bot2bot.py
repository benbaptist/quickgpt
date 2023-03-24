from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

import os
import time

""" Forces ChatGPT to talk to itself. """

if __name__ == "__main__":
    chat = QuickGPT()

    buddy = chat.new_thread()
    bot = chat.new_thread()

    bot.feed(
        System("You are a chat assistant. Please greet the user and help with their questions.")
    )

    buddy.feed(
        System("You are a person. You can make up your own name. You will be conversing with a chatbot. You are pretending to be a human user. Keep the conversation alive as long as you can.")
    )

    def chat():
        t = ""

        # Only allows up to 32 iterations, to prevent accidentially blowing up your API quota
        for i in range(32):
            bot_response = bot.run()

            t += "<Bot> %s\n" % bot_response.message
            print("<Bot> %s" % bot_response.message)

            buddy.feed(
                User(bot_response.message)
            )

            buddy_response = buddy.run()

            t += "<Buddy> %s\n" % buddy_response.message
            print("<Buddy> %s" % buddy_response.message)

            bot.feed(
                User(buddy_response.message)
            )

        return t

    transcript = ""

    try:
        transcript = chat()
    except KeyboardInterrupt:
        print("Alright, we're done.")
    finally:
        # Save transcript

        if not os.path.exists("transcripts"):
            os.mkdir("transcripts")

        with open("transcripts/%s.log" % time.strftime("%Y-%m-%d_%H-%M-%S"), "w") as f:
            f.write(transcript)
