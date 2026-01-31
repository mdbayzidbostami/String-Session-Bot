from telethon import TelegramClient
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ask_ques = "Choose the string session type you want:"
buttons_ques = [
    [
        InlineKeyboardButton("Telethon", callback_data="telethon"),
        InlineKeyboardButton("Pyrogram", callback_data="pyrogram")
    ],
    [
        InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot"),
        InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot")
    ],
    [
        InlineKeyboardButton("Close", callback_data="close")
    ]
]

gen_button = [[
    InlineKeyboardButton(
        text="Generate String Session",
        callback_data="generate"
    )
]]

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["gen"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    ty = "TELETHON" if telethon else "PYROGRAM"
    if is_bot:
        ty += " BOT"

    await msg.reply(f"Trying to start {ty} string session generator...")

    user_id = msg.chat.id

    api_id_msg = await bot.ask(
        user_id,
        "Send your API_ID to continue.",
        filters=filters.text
    )

    if await cancelled(api_id_msg):
        return

    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply(
            "API_ID must be an integer. Please start again.",
            reply_markup=InlineKeyboardMarkup(gen_button)
        )
        return

    api_hash_msg = await bot.ask(
        user_id,
        "Now send your API_HASH.",
        filters=filters.text
    )

    if await cancelled(api_hash_msg):
        return

    api_hash = api_hash_msg.text

    if not is_bot:
        t = (
            "Send your phone number with country code.\n"
            "Example: +8801XXXXXXXXX"
        )
    else:
        t = (
            "Send your bot token.\n"
            "Example: 123456789:ABCdefGhIjKlMnOpQrStUvWx"
        )

    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)

    if await cancelled(phone_number_msg):
        return

    phone_number = phone_number_msg.text

    if not is_bot:
        await msg.reply("Sending OTP to your number...")
    else:
        await msg.reply("Logging in using bot token...")

    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(
            name="bot",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=phone_number,
            in_memory=True
        )
    else:
        client = Client(
            name="user",
            api_id=api_id,
            api_hash=api_hash,
            in_memory=True
        )

    await client.connect()

    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply(
            "API_ID and API_HASH are invalid. Please try again.",
            reply_markup=InlineKeyboardMarkup(gen_button)
        )
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply(
            "The phone number you sent is invalid.",
            reply_markup=InlineKeyboardMarkup(gen_button)
        )
        return

    try:
        if not is_bot:
            phone_code_msg = await bot.ask(
                user_id,
                "Send the OTP you received.\nExample: 1 2 3 4 5",
                filters=filters.text,
                timeout=600
            )
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply(
            "Time limit exceeded. Please start again.",
            reply_markup=InlineKeyboardMarkup(gen_button)
        )
        return

    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply(
                "The OTP you sent is wrong.",
                reply_markup=InlineKeyboardMarkup(gen_button)
            )
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply(
                "The OTP has expired.",
                reply_markup=InlineKeyboardMarkup(gen_button)
            )
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(
                    user_id,
                    "Enter your 2-step verification password.",
                    filters=filters.text,
                    timeout=300
                )
            except TimeoutError:
                await msg.reply(
                    "Time limit exceeded.",
                    reply_markup=InlineKeyboardMarkup(gen_button)
                )
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply(
                    "Wrong password.",
                    reply_markup=InlineKeyboardMarkup(gen_button)
                )
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)

    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()

    text = (
        f"This is your {ty} string session:\n\n"
        f"`{string_session}`\n\n"
        f"By: @NeoCloud_Ofc\n\n"
        f"Note: Do not share this string with anyone. "
        f"Anyone with this string can access your account."
    )

    if not is_bot:
        await client.send_message("me", text)
    else:
        await bot.send_message(msg.chat.id, text)

    await client.disconnect()

    await bot.send_message(
        msg.chat.id,
        f"Successfully generated your {ty} string session.\n"
        f"Please check your Saved Messages.\n\n"
        f"String Generator Bot by @NeoCloud_Ofc"
    )


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply(
            "String generation cancelled.",
            reply_markup=InlineKeyboardMarkup(gen_button)
        )
        return True
    return False
