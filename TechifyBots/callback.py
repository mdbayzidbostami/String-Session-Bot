import traceback
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from config import ADMIN
from .main import generate_session, ask_ques, buttons_ques

CHANNEL_LINK = "https://t.me/NeoCloud_Ofc"

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    data = query.data

    try:
        if data == "start":
            await query.message.edit_text(
                text.START.format(query.from_user.mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("About", callback_data="about"),
                        InlineKeyboardButton("Help", callback_data="help")
                    ],
                    [
                        InlineKeyboardButton(
                            "Generate String Session",
                            callback_data="generate"
                        )
                    ]
                ])
            )

        elif data == "help":
            await query.message.edit_text(
                text.HELP.format(query.from_user.mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("Official Channel", url=CHANNEL_LINK)
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="start"),
                        InlineKeyboardButton("Close", callback_data="close")
                    ]
                ])
            )

        elif data == "about":
            await query.message.edit_text(
                "String Session Generator Bot\n\n"
                "Developed By: Team CineBuzzBD\n"
                "Author: Md Bayzid Bostami\n"
                "Official Telegram Channel:\n"
                f"{CHANNEL_LINK}",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            "Join Official Channel",
                            url=CHANNEL_LINK
                        )
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="start"),
                        InlineKeyboardButton("Close", callback_data="close")
                    ]
                ])
            )

        elif data == "close":
            await query.message.delete()
            await query.answer()

        elif data == "generate":
            await query.answer()
            await query.message.reply(
                ask_ques,
                reply_markup=InlineKeyboardMarkup(buttons_ques)
            )

        elif data in ["pyrogram", "pyrogram_bot", "telethon", "telethon_bot"]:
            await query.answer()

            if data == "pyrogram":
                await generate_session(client, query.message)

            elif data == "pyrogram_bot":
                await query.answer(
                    "The generated session will be for Pyrogram v2.",
                    show_alert=True
                )
                await generate_session(client, query.message, is_bot=True)

            elif data == "telethon":
                await generate_session(client, query.message, telethon=True)

            elif data == "telethon_bot":
                await generate_session(
                    client,
                    query.message,
                    telethon=True,
                    is_bot=True
                )

    except Exception as e:
        print(traceback.format_exc())
        await query.message.reply(f"Error: `{e}`")
