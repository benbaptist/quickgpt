from quickgpt import QuickGPT
from quickgpt.thread.messagetypes import *
from quickgpt.thread.function import Function
from quickgpt.thread.function.parameter import Parameter

""" Testing functions. """

if __name__ == "__main__":
    chat = QuickGPT()

    thread = chat.new_thread(model="gpt-4-0613")

    def get_current_weather(**kwargs):
        print(kwargs)

    thread.add_function(get_current_weather)

    while True:
        prompt = None

        while not prompt:
            # prompt = input("<You> ")
            prompt = "What's the weather in Benton Harbor area like?"

            thread.feed(
                User(prompt)
            )

        # response = thread.run(
        #         functions={
        #             "weather": Function(
        #                 name="Weather",
        #                 description="Get the weather forecast",
        #                 properties={
        #                     "zip": Parameter(type="string", description="The ZIP code to retrieve the weather from")
        #                 },
        #                 required=["zip"]
        #             )
        #         }
        # )

        response = thread.run(
                functions=[{
                        "name": "get_current_weather",
                        "description": "Get the current weather in a given location",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and state, e.g. San Francisco, CA",
                                },
                                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                            },
                            "required": ["location"]
                        }
                    }
                ]
        )

        print(response)

        # thread.feed(
        #     Assistant(response.message)
        # )

        break
