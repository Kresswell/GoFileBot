from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can upload any media to gofile.io and return the link.
Just send me the media and you will get the link!

By @InfinityHack3rsKE 
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/InfinityHack3rsKE")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/InfinityHack3rsKE")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/InfinityHack3rs")],
    ]

    # Help Message
    HELP = """
Just send me the media and you will get the link!

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to upload files to gofile.io by @StarkBots

WEBSITE : [Click Here](https://www.infinityhackers.xyz)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @EscaliBud
    """
