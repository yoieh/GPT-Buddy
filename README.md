# GPT-Buddy

GPT-Buddy is a Discord bot powered by OpenAI's ChatGPT. The bot listens to user prompts and responds with creative and funny answers. GPT-Buddy can also perform a variety of imaginary actions for entertainment purposes.

## Features

- Responds to user prompts with creative answers
- Performs a variety of imaginary actions, such as:
    - tap_dance_on_grapes
    - whistle_underwater
    - paint_invisible_portrait
    - juggle_invisible_fruits
    - mime_stuck_in_box
    - sing_gibberish
    - do_the_robot
    - tell_a_useless_fact

## Setup

### Prerequisites

- Python 3.6 or higher
- Discord account and bot token
- OpenAI API key

### Installation

1. Clone the repository:
`
```
git clone https://github.com/yoieh/GPT-Buddy.git
```

2. Change directory to the project folder:

```
cd GPT-Buddy
```

3. Create a virtual environment:

```
python -m venv bot-env
```

4. Activate the virtual environment:

- On Windows: `bot-env\Scripts\activate`
- On macOS/Linux: `source bot-env/bin/activate`

5. Install the required packages:

```
pip install -r requirements.txt
```

6. Create a `.env` file in the project folder with the following content:

```
OPENAI_API_KEY=<your_openai_api_key>
DISCORD_BOT_TOKEN=<your_discord_bot_token>
```


7. Replace `<your_openai_api_key>` and `<your_discord_bot_token>` with your OpenAI API key and Discord bot token, respectively.

### Usage

1. Run the bot:

```
python gpt_buddy.py
```

2. Add the bot to your Discord server.

3. Start chatting with GPT-Buddy by using the `!ask` command:

```
!ask <your_prompt>
```

For example:

```
!ask tell me a joke
```

4. Request an imaginary action with the `!action` command:

```
!action <action_name>
```

For example:

```
!action tap_dance_on_grapes
```


## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
