from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *

""" Testing functions. """

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread(model="gpt-4-0613")

    def get_current_weather(zip_code=None):
        return f"Weather for {zip_code}: It's 65 degrees and Sunny. Tomorrow, it'll rain."

    thread.add_function(get_current_weather)

    while True:
        prompt = None

        while not prompt:
            prompt = input("<You> ")

            thread.feed(
                User(prompt)
            )

        response = thread.run(
                functions=[{
                        "name": "get_current_weather",
                        "description": "Get the current weather in a given location",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "zip_code": {
                                    "type": "string",
                                    "description": "The zip code, e.g. 60052",
                                }
                            },
                            "required": ["zip_code"]
                        }
                    }
                ]
        )

        if type(response) == Function:
            response = thread.run()

        print(response)
