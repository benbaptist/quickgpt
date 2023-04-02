from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread()

    response = thread.run(
        System("This is a lot of text! It may be too much for the model." * 1024)
    )

    print(response)
