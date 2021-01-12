from carbonnow import Carbon
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import KeyboardButton
from pyrogram.types import ForceReply
from pykeyboard import InlineKeyboard
from pykeyboard import ReplyKeyboard
from pyromod import listen
import re
from config import Config
import logging
logging.basicConfig(level=logging.INFO)


bot = Client(
    ":memory:",
    api_id=Config.api_id,
    api_hash=Config.api_hash,
    bot_token=Config.bot_token
)

caches = {}
color = {}


@bot.on_message(filters.private & filters.command("start"))
async def carbon_func(client: bot, message: Message):
    keyboard = InlineKeyboard(row_width=3)
    keyboard.add(
        InlineKeyboardButton("3024 Night", "carbon_3024-night"),
        InlineKeyboardButton("A11y Dark", "carbon_a11y-dark"),
        InlineKeyboardButton("Blackboard", "carbon_blackboard"),
        InlineKeyboardButton("Base 16 (Dark)", "carbon_base16-dark"),
        InlineKeyboardButton("Base 16 (Light)", "carbon_base16-light"),
        InlineKeyboardButton("Cobalt", "carbon_cobalt"),
        InlineKeyboardButton("Duotone", "carbon_duotone-dark"),
        InlineKeyboardButton("Dracula", "carbon_dracula-pro"),
        InlineKeyboardButton("Hopscotch", "carbon_hopscotch"),
        InlineKeyboardButton("Lucario", "carbon_lucario"),
        InlineKeyboardButton("Material", "carbon_material"),
        InlineKeyboardButton("Monokai", "carbon_monokai"),
        InlineKeyboardButton("Night Owl", "carbon_nightowl"),
        InlineKeyboardButton("Nord", "carbon_nord"),
        InlineKeyboardButton("Oceanic Next", "carbon_oceanic-next"),
        InlineKeyboardButton("One Light", "carbon_one-light"),
        InlineKeyboardButton("One Dark", "carbon_one-dark"),
        InlineKeyboardButton("Panda", "carbon_panda-syntax"),
        InlineKeyboardButton("Parasio", "carbon_parasio-dark"),
        InlineKeyboardButton("Seti", "carbon_seti"),
        InlineKeyboardButton("Shades of purple", "carbon_shades-of-purple"),
        InlineKeyboardButton("Solarized (Dark)", "carbon_solarized+dark"),
        InlineKeyboardButton("Solarized (Light)", "carbon_solarized+light"),
        InlineKeyboardButton("SynthWave '84", "carbon_synthwave-84"),
        InlineKeyboardButton("Twilight", "carbon_twilight"),
        InlineKeyboardButton("Verminal", "carbon_verminal"),
        InlineKeyboardButton("VSCode", "carbon_vscode"),
        InlineKeyboardButton("Yeti", "carbon_yeti"),
        InlineKeyboardButton("Zenburn", "carbon_zenburn"),
    )
    await message.reply(
        "Select a theme:",
        reply_markup=keyboard
    )


async def button_callback(_, __, query):
    if re.match(r'carbon_', query.data):
        return True


button_create = filters.create(button_callback)


@bot.on_callback_query(button_create)
async def theme_button(_, query):
    keyboard = InlineKeyboard(row_width=4)
    keyboard.add(
        InlineKeyboardButton("Red", "color_#FF0000"),
        InlineKeyboardButton("Orange", "color_#FF5733"),
        InlineKeyboardButton("Yellow", "color_#FFFF00"),
        InlineKeyboardButton("Green", "color_#008000"),
        InlineKeyboardButton("Blue", "color_#0000FF"),
        InlineKeyboardButton("Purple", "color_#800080"),
        InlineKeyboardButton("Brown", "color_#A52A2A"),
        InlineKeyboardButton("Magenta", "color_#FF00FF"),
        InlineKeyboardButton("Tan", "color_#D2B48C"),
        InlineKeyboardButton("Cyan", "color_#00FFFF"),
        InlineKeyboardButton("Olive", "color_#808000"),
        InlineKeyboardButton("Maroon", "color_#800000"),
        InlineKeyboardButton("Aquamarine", "color_#00FFFF"),
        InlineKeyboardButton("Turquoise", "color_#30D5C8"),
        InlineKeyboardButton("Lime", "color_#00FF00"),
        InlineKeyboardButton("Teal", "color_#008080"),
        InlineKeyboardButton("Indigo", "color_#4B0082"),
        InlineKeyboardButton("Violet", "color_#EE82EE"),
        InlineKeyboardButton("Pink", "color_#FFC0CB"),
        InlineKeyboardButton("Black", "color_#000000"),
        InlineKeyboardButton("White", "color_#FFFFFF"),
        InlineKeyboardButton("Gray", "color_#808080"),
    )
    caches[str(query.from_user.id) + "theme"] = query.data.split("_")[1]
    print(caches)

    await query.message.edit(
        "Choose a color:",
        reply_markup=keyboard
    )


async def color_callback(_, __, query):
    if re.match(r'color_', query.data):
        return True

color_create = filters.create(color_callback)

@bot.on_callback_query(color_create)
async def color_button(client, query):
    await query.message.delete()
    keyboard = ReplyKeyboard(row_width=1)
    keyboard.add(
        KeyboardButton('Yes'),
        KeyboardButton('No'),
    )
    watermarker = await client.ask(
        query.message.chat.id,
        "Would you like to have a WaterMark on the carbonized code?",
        reply_markup=keyboard
    )
    color[str(query.from_user.id) + "color"] = query.data.split("_")[1]
    if watermarker.text.lower() == "no":
        watermark = False
    elif watermarker.text.lower() == "yes":
        watermark = True
    else:
        await query.message.reply(
            "Can't get that, I assume you said no"
        )
        watermark = False
    final = await client.ask(
            query.message.chat.id,
            "Okay, Now send me the Code to parse on carbon.now.sh",
            reply_markup=ForceReply(True)
        )
    carbon = Carbon(
        code=final.text,
        theme=caches[str(query.from_user.id) + "theme"],
        background=color[str(query.from_user.id) + "color"],
        language="auto",
        drop_shadow=True,
        drop_shadow_blur='68px',
        drop_shadow_offset='20px',
        font_family='Fira Code',
        width_adjustment=True,
        watermark=watermark,
    )
    await query.message.reply_chat_action(
        "upload_photo"
    )
    photo = await carbon.memorize(str(client.rnd_id()))
    await query.message.reply_photo(photo)
    await query.message.reply(
        "if you like it and want to try again you can send me /start again :D"
    )

if __name__ == "__main__":
    bot.run()