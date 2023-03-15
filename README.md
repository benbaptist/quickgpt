# quickGPT

[![PyPI - Downloads](https://img.shields.io/pypi/dm/quickgpt?style=for-the-badge)](https://pypi.org/project/quickgpt/)
![PyPI - Status](https://img.shields.io/pypi/status/quickgpt?style=for-the-badge)
[![PyPI](https://img.shields.io/pypi/v/quickgpt?style=for-the-badge)](https://pypi.org/project/quickgpt/)

**quickGPT** is a lightweight and easy-to-use Python library that provides a simplified interface for working with the new API interface of OpenAI's ChatGPT. With quickGPT, you can easily generate natural language responses to prompts and questions using state-of-the-art language models trained by OpenAI.

For the record, this README.md was (mostly) generated with ChatGPT. That's why it's a little braggy.

## Installation

You can install **quickGPT** using pip:

```sh
pip install quickGPT
```

## Usage
To use quickGPT, you'll need an OpenAI API key, which you can obtain from the OpenAI website. Once you have your API key, you can create a quickGPT object and start generating responses:

```
from chattylib import ChattyLib
from chattylib.thread.messagetypes import *

if __name__ == "__main__":
    chat = ChattyLib()

    thread = chat.new_thread()

    thread.feed(
        System("The world is your oyster.")
    )

    while True:
        response = thread.run()
        print("Bot: %s" % response.message)

        prompt = input("You: ")

        thread.feed(
            Assistant(response.message),
            User(prompt)
        )
```

Try out `catbot.py` in the examples folder for an interactive fuzzface experience.

## Documentation
There's no documentation yet. Stay tuned.

## Contributing
If you find a bug or have an idea for a new feature, please submit an issue on the GitHub repository. Pull requests are also welcome!

## License
This project is licensed under the MIT License.
