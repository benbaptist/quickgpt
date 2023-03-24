from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

from elevenlabs import ElevenLabs

from uuid import uuid4

import os
import time
import traceback
import sys

""" Generate a podcast between two bots, and use ElevenLabs to generate vocals. """

if __name__ == "__main__":
    eleven = ElevenLabs(os.environ.get("ELEVENLABS_API_KEY"))

    session_id = str(uuid4())
    session_path = "transcripts/%s" % session_id

    if not os.path.exists(session_path):
        os.makedirs(session_path)

    cohost1_voice = eleven.voices["Coffeezilla"]
    cohost2_voice = eleven.voices["Russ"]

    chat = QuickGPT()

    cohost1 = chat.new_thread()
    cohost2 = chat.new_thread()

    instructions = [
        System("You are the host of a popular podcast, alongside another co-host."),
        System("You will engage with the conversation and talk about a topic of your choosing."),
        System("You decide what your name is, and if your co-host hasn't decided yet, on a topic as well."),
        System("You only need to generate one message at a time, as I will take care of providing responses for your other cohost."),
        # System("When it comes time to end the podcast, after your saluations, write the command [[EOF]]")
    ]

    cohost1.feed(instructions)
    cohost2.feed(instructions)

    def chat():
        t = ""

        # Only allows up to 32 iterations, to prevent accidentially blowing up your API quota
        for i in range(16):
            cohost1_response = cohost1.run()

            t += "<cohost1> %s\n" % cohost1_response.message
            print("<cohost1> %s" % cohost1_response.message)

            audio = cohost1_voice.generate(
                cohost1_response.message,
                voice_settings={"stability": 0.0, "similarity_boost": 1.0}
            )

            audio.save(os.path.join(session_path, "cohost1-%s" % i))

            cohost2.feed(
                User(cohost1_response.message)
            )

            cohost2_response = cohost2.run()

            t += "<cohost2> %s\n" % cohost2_response.message
            print("<cohost2> %s" % cohost2_response.message)

            audio = cohost2_voice.generate(
                cohost2_response.message,
                voice_settings={"stability": 0.0, "similarity_boost": 1.0}
            )

            audio.save(os.path.join(session_path, "cohost2-%s" % i))

            cohost1.feed(
                User(cohost2_response.message)
            )

        return t

    transcript = ""

    try:
        transcript = chat()
    except KeyboardInterrupt:
        print("Alright, we're done.")
    except:
        print("-" * 16)
        print("We failed, y'all.")
        traceback.print_exc()
    finally:
        # Save transcript

        if not os.path.exists("transcripts"):
            os.mkdir("transcripts")

        with open("%s/transcript.log" % session_path, "w") as f:
            f.write(transcript)
