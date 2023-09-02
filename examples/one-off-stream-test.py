from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

import sys

"""
Short example that shows quickGPT's streaming response capabilities in a
single-use QuickGPT.run().
"""

DO_STREAM = True

if __name__ == "__main__":
    chat = QuickGPT()

    response = chat.run(
        System("Talk like a fuzzy kitten."),
        stream=True
    )

    for resp in response.message:

        if type(resp) == str:
            sys.stdout.write(resp)
            sys.stdout.flush()

    print("")
