from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

""" Testing functions. """

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread(model="gpt-4-0613")

    def get_current_weather(zip_code=None):
        return f"Weather for {zip_code}: It's 65 degrees and Sunny. Tomorrow, it'll rain."

    thread.add_function(
        method=get_current_weather,
        description="Get the current weather in a given location",
        properties={
            "zip_code": {
                "type": "string",
                "description": "The zip code for the weather, e.g. 60052"
            }
        },
        required=["zip_code"]
    )

    print("Try asking the AI about the weather.")
    print("Note: It'll return a hard-coded, fake weather report.")

    while True:
        prompt = None

        while not prompt:
            # e.g. ask "What's the weather like in Chicago?"
            prompt = input("<You> ")
            # prompt = "What's the weather like in chicago?"

            thread.feed(
                User(prompt)
            )

        response = thread.run()

        if type(response) == Function:
            # Run again with the function's response
            response = thread.run()

        print(response)
