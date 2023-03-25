import random


async def sing_dramatic_jingle():
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    lyrics = ["la", "da", "ba", "ta", "na", "ma"]
    jingle = " ".join(
        [f"{random.choice(notes)}{random.choice(lyrics)}" for _ in range(10)]
    )
    return f"🎵 Singing a dramatic jingle: {jingle} 🎵"


async def flip_invisible_pancake():
    return "🥞 Flipping an invisible pancake in the air! Whoosh! 🥞"


async def count_to_potato():
    random_number = random.randint(1, 10)
    counting = ", ".join(str(i) for i in range(1, random_number + 1))
    return f"Counting to potato: {counting}, potato 🥔"


def tap_dance_on_grapes():
    return "🍇🕺 The bot is now tap dancing on imaginary grapes! 🍇🕺"


def whistle_underwater():
    return "💦🎶 The bot is attempting to whistle while pretending to be underwater! 💦🎶"


def paint_invisible_portrait():
    return "🎨👤 The bot is painting an invisible portrait of an imaginary person! 🎨👤"


def juggle_invisible_fruits():
    return "🍏🍌🍊🤹 The bot is juggling a set of invisible fruits with great skill! 🍏🍌🍊🤹"


def mime_stuck_in_box():
    return "🤡📦 The bot is pretending to be a mime stuck inside an invisible box! 🤡📦"


def sing_gibberish():
    return "🎶 La la la... skibidi wapapap, skibidi wapapap, bapapapapapap... 🎶 I just sang some gibberish for you!"


def do_the_robot():
    return "🤖 *beep boop* Performing the robot dance... *beep boop* 🤖"


def tell_a_useless_fact():
    return "Here's a useless fact for you: Bananas are curved because they grow towards the sun!"


def get_actions():
    return {
        "sing_dramatic_jingle": sing_dramatic_jingle,
        "flip_invisible_pancake": flip_invisible_pancake,
        "count_to_potato": count_to_potato,
        "sing_gibberish": sing_gibberish,
        "do_the_robot": do_the_robot,
        "tell_a_useless_fact": tell_a_useless_fact,
        "tap_dance_on_grapes": tap_dance_on_grapes,
        "whistle_underwater": whistle_underwater,
        "paint_invisible_portrait": paint_invisible_portrait,
        "juggle_invisible_fruits": juggle_invisible_fruits,
        "mime_stuck_in_box": mime_stuck_in_box,
    }
