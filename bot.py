from carbonnow import Carbon
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import ForceReply
from pykeyboard import InlineKeyboard
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
        InlineKeyboardButton("3024 Night", "carbon_night"),
        InlineKeyboardButton("A11y Dark", "carbon_a11ydark"),
        InlineKeyboardButton("Blackboard", "carbon_blackboard"),
        InlineKeyboardButton("Base 16 (Dark)", "carbon_bdark"),
        InlineKeyboardButton("Base 16 (Light)", "carbon_blight"),
        InlineKeyboardButton("Cobalt", "carbon_cobalt"),
        InlineKeyboardButton("Duotone", "carbon_Duotone"),
        InlineKeyboardButton("Dracula", "carbon_dracula"),
        InlineKeyboardButton("Hopscotch", "carbon_hopscotch"),
        InlineKeyboardButton("Lucario", "carbon_lucario"),
        InlineKeyboardButton("Material", "carbon_material"),
        InlineKeyboardButton("Monokai", "carbon_monokai"),
        InlineKeyboardButton("Night Owl", "carbon_nightowl"),
        InlineKeyboardButton("Nord", "carbon_nord"),
        InlineKeyboardButton("Oceanic Next", "carbon_oceanicnext"),
        InlineKeyboardButton("Panda", "carbon_panda"),
        InlineKeyboardButton("Parasio", "carbon_parasio"),
        InlineKeyboardButton("Seti", "carbon_seti"),
        InlineKeyboardButton("Shades of purple", "carbon_sop"),
        InlineKeyboardButton("Solarized (Dark)", "carbon_sdark"),
        InlineKeyboardButton("Solarized (Light)", "carbon_slight"),
        InlineKeyboardButton("SynthWave '84", "carbon_synthwave"),
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
    matching = re.findall(
        r"night|a11ydark|blackboard|bdark|blight|cobalt|Duotone|dracula|" \
        r"material|monokai|nightowl|nord|oceanicnext|panda|parasio|seti|sop|" \
        r"sdark|slight|synthwave|twilight|verminal|vscode|yeti|zenburn|hopscotch|lucario",
        query.data
    )
    if matching:
        keyboard = InlineKeyboard(row_width=4)
        keyboard.add(
            InlineKeyboardButton("Red", "color_red"),
            InlineKeyboardButton("Orange", "color_orange"),
            InlineKeyboardButton("Yellow", "color_yellow"),
            InlineKeyboardButton("Green", "color_green"),
            InlineKeyboardButton("Blue", "color_blue"),
            InlineKeyboardButton("Purple", "color_purple"),
            InlineKeyboardButton("Brown", "color_brown"),
            InlineKeyboardButton("Magenta", "color_magenta"),
            InlineKeyboardButton("Tan", "color_tan"),
            InlineKeyboardButton("Cyan", "color_cyan"),
            InlineKeyboardButton("Olive", "color_olive"),
            InlineKeyboardButton("Maroon", "color_maroon"),
            InlineKeyboardButton("Navy", "color_navy"),
            InlineKeyboardButton("Aquamarine", "color_aquamarine"),
            InlineKeyboardButton("Turquoise", "color_turquoise"),
            InlineKeyboardButton("Lime", "color_lime"),
            InlineKeyboardButton("Teal", "color_teal"),
            InlineKeyboardButton("Indigo", "color_indigo"),
            InlineKeyboardButton("Violet", "color_violet"),
            InlineKeyboardButton("Pink", "color_pink"),
            InlineKeyboardButton("Black", "color_black"),
            InlineKeyboardButton("White", "color_white"),
            InlineKeyboardButton("Gray", "color_gray"),
        )
        if matching[0] == "night":
            caches[str(query.from_user.id) + "theme"] = "3024 Night"
        if matching[0] == "a11ydark":
            caches[str(query.from_user.id) + "theme"] = "A11y Dark"
        if matching[0] == "bdark":
            caches[str(query.from_user.id) + "theme"] = "Base 16 (Dark)"
        if matching[0] == "blight":
            caches[str(query.from_user.id) + "theme"] = "Base 16 (Light)"
        if matching[0] == "cobalt":
            caches[str(query.from_user.id) + "theme"] = "Cobalt"
        if matching[0] == "Duotone":
            caches[str(query.from_user.id) + "theme"] = "Duotone"
        if matching[0] == "dracula":
            caches[str(query.from_user.id) + "theme"] = "Dracula Pro"
        if matching[0] == "hopscotch":
            caches[str(query.from_user.id) + "theme"] = "Hopscotch"
        if matching[0] == "lucario":
            caches[str(query.from_user.id) + "theme"] = "Lucario"
        if matching[0] == "material":
            caches[str(query.from_user.id) + "theme"] = "Material"
        if matching[0] == "monokai":
            caches[str(query.from_user.id) + "theme"] = "Monokai"
        if matching[0] == "nightowl":
            caches[str(query.from_user.id) + "theme"] = "Night Owl"
        if matching[0] == "nord":
            caches[str(query.from_user.id) + "theme"] = "Nord"
        if matching[0] == "oceanicnext":
            caches[str(query.from_user.id) + "theme"] = "Oceanic Next"
        if matching[0] == "panda":
            caches[str(query.from_user.id) + "theme"] = "Panda"
        if matching[0] == "parasio":
            caches[str(query.from_user.id) + "theme"] = "Parasio"
        if matching[0] == "seti":
            caches[str(query.from_user.id) + "theme"] = "Seti"
        if matching[0] == "sop":
            caches[str(query.from_user.id) + "theme"] = "Shades of Puple"
        if matching[0] == "sdark":
            caches[str(query.from_user.id) + "theme"] = "Solarized (Dark)"
        if matching[0] == "slight":
            caches[str(query.from_user.id) + "theme"] = "Solarized (Light)"
        if matching[0] == "synthwave":
            caches[str(query.from_user.id) + "theme"] = "SynthWave '84"
        if matching[0] == "twilight":
            caches[str(query.from_user.id) + "theme"] = "Twilight"
        if matching[0] == "verminal":
            caches[str(query.from_user.id) + "theme"] = "Verminal"
        if matching[0] == "vscode":
            caches[str(query.from_user.id) + "theme"] = "VSCode"
        if matching[0] == "yeti":
            caches[str(query.from_user.id) + "theme"] = "Yeti"
        if matching[0] == "zenburn":
            caches[str(query.from_user.id) + "theme"] = "Zenburn"

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
    matching = re.findall(
        r"red|orange|yellow|green|blue|purple|brown|magenta|tan|cyan|" \
        r"olive|maroon|aquamarine|turquoise|lime|teal|indigo|voiolet|pink|" \
        r"black|white|gray",
        query.data
    )
    if matching:
        if matching[0] == "red":
            color[str(query.from_user.id) + "color"] = "#FF0000"
        if matching[0] == "orange":
            color[str(query.from_user.id) + "color"] = "#FF5733"
        if matching[0] == "yellow":
            color[str(query.from_user.id) + "color"] = "#FFFF00"
        if matching[0] == "green":
            color[str(query.from_user.id) + "color"] = "#008000"
        if matching[0] == "blue":
            color[str(query.from_user.id) + "color"] = "#0000FF"
        if matching[0] == "purple":
            color[str(query.from_user.id) + "color"] = "#800080"
        if matching[0] == "brown":
            color[str(query.from_user.id) + "color"] = "#A52A2A"
        if matching[0] == "magenta":
            color[str(query.from_user.id) + "color"] = "#FF00FF"
        if matching[0] == "tan":
            color[str(query.from_user.id) + "color"] = "#D2B48C"
        if matching[0] == "cyan":
            color[str(query.from_user.id) + "color"] = "#00FFFF"
        if matching[0] == "olive":
            color[str(query.from_user.id) + "color"] = "#808000"
        if matching[0] == "maroon":
            color[str(query.from_user.id) + "color"] = "#800000"
        if matching[0] == "aquamarine":
            color[str(query.from_user.id) + "color"] = "#00FFFF"
        if matching[0] == "turquoise":
            color[str(query.from_user.id) + "color"] = "#30D5C8"
        if matching[0] == "slime":
            color[str(query.from_user.id) + "color"] = "#00FF00"
        if matching[0] == "teal":
            color[str(query.from_user.id) + "color"] = "#008080"
        if matching[0] == "indigo":
            color[str(query.from_user.id) + "color"] = "#4B0082"
        if matching[0] == "voiolet":
            color[str(query.from_user.id) + "color"] = "#EE82EE"
        if matching[0] == "pink":
            color[str(query.from_user.id) + "color"] = "#FFC0CB"
        if matching[0] == "black":
            color[str(query.from_user.id) + "color"] = "#000000"
        if matching[0] == "white":
            color[str(query.from_user.id) + "color"] = "#FFFFFF"
        if matching[0] == "gray":
            color[str(query.from_user.id) + "color"] = "#808080"
        await query.message.delete()
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
            window_theme=caches[str(query.from_user.id) + "theme"],
            width_adjustment=True,
        )
        photo = await carbon.memorize(str(client.rnd_id()))
        await query.message.reply_photo(photo)
        await query.message.reply(
            "if you like it and want to try again you can send me /start again :D"
        )

if __name__ == "__main__":
    bot.run()