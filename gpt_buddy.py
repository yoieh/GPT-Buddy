from dotenv import load_dotenv

load_dotenv()

import os
import openai
import discord
from discord.ext import commands

from actions import get_actions


openai_api_key = os.getenv("OPENAI_API_KEY")
bot_token = os.getenv("DISCORD_BOT_TOKEN")

# Set up the discord.py bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Set up GPT-3.5-turbo chat model
MODEL = "gpt-3.5-turbo"

actions = get_actions()


async def ask_gpt(prompt):
    openai.api_key = openai_api_key

    # A message describing the available actions
    action_descriptions = {
        "sing_dramatic_jingle": "The bot sings a dramatic jingle.",
        "flip_invisible_pancake": "The bot flips an invisible pancake.",
        "count_to_potato": "The bot counts numbers but ends with 'potato'.",
        "tap_dance_on_grapes": "The bot performs a tap dance on imaginary grapes.",
        "whistle_underwater": "The bot attempts to whistle while pretending to be underwater.",
        "paint_invisible_portrait": "The bot paints an invisible portrait of an imaginary person.",
        "juggle_invisible_fruits": "The bot juggles a set of invisible fruits with great skill.",
        "mime_stuck_in_box": "The bot pretends to be a mime stuck inside an invisible box.",
        "sing_gibberish": "The bot sings gibberish in a musical manner.",
        "do_the_robot": "The bot performs the robot dance.",
        "tell_a_useless_fact": "The bot shares a useless fact.",
    }

    action_descriptions_list = [
        f"{key}: {value}" for key, value in action_descriptions.items()
    ]
    action_descriptions_string = "".join(action_descriptions_list)
    action_message = (
        "Here are the available actions:\n" + "\n" + action_descriptions_string
    )
    # Include the action_message in the list of messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "system",
            "content": "If need to preform an action, only respond with the action name and nothing else",
        },
        {"role": "user", "content": action_message},
        {"role": "user", "content": prompt},
    ]

    print(messages)

    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    print(completions.choices)

    message = completions.choices[0].message.content.strip()

    # remove . from the end of the message
    if message.endswith("."):
        message = message[:-1]

    # Check if the message matches any of the available actions
    if message in actions:
        return await actions[message]()
    else:
        return message + "."


@bot.event
async def on_ready():
    print(f"GPT-Buddy is logged in as {bot.user}")


@bot.command()
async def ask(ctx, *, question):
    prompt = f"{question}"
    print(f"Question: {question}")
    response_text = await ask_gpt(prompt)
    print(f"Response: {response_text}")
    await ctx.send(response_text)


# Replace with your bot token
bot.run(bot_token)
