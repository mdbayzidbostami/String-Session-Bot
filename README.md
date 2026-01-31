# String Session Bot

A professional Telegram bot designed to generate Pyrogram and Telethon string sessions securely and efficiently.

## Features

- **Session Generation**: Supports Pyrogram, Telethon, and Bot Session generation.
- **Force Subscribe**: Ability to add multiple channels for mandatory subscription.
- **Broadcast System**: Send messages to all authorized users.
- **Maintenance Mode**: Toggle bot availability during updates.
- **User Management**: Ban and unban users directly through commands.
- **Easy Deployment**: Fully compatible with Koyeb, Heroku, and Railway.
- **Support**: 24/7 developer assistance via the community channel.

## Environment Variables

To deploy this bot, you need to configure the following environment variables:

| Variable | Description |
|----------|-------------|
| `API_ID` | Your Telegram API ID. Get it from [NeoCloud](https://t.me/NeoCloud_Ofc) |
| `API_HASH` | Your Telegram API HASH. Get it from [NeoCloud](https://t.me/NeoCloud_Ofc) |
| `BOT_TOKEN` | Your Bot Token from @BotFather. |
| `DB_URI` | Your MongoDB Database URI. |
| `ADMIN` | Your Telegram User ID (Numeric). |
| `PICS` | Image links for the bot's start message. |
| `LOG_CHANNEL` | Telegram ID of the channel for logs. |
| `IS_FSUB` | Set to `True` or `False` to enable/disable Force Subscribe. |
| `FSUB_EXPIRE` | Expiry time for the Force Subscribe link. |
| `AUTH_CHANNELS` | Public/Private channel IDs for FSUB. |
| `AUTH_REQ_CHANNELS` | Private Request channel IDs for FSUB. |

## Bot Commands

- `/start` - Start the bot.
- `/gen` - Initiate the string session generation process.
- `/stats` - View bot statistics and usage data.
- `/cancel` - Cancel the ongoing generation process.
- `/broadcast` - Send a message to all users (Admin only).
- `/maintenance` - Toggle maintenance mode on or off.
- `/ban` - Restrict a user from using the bot.
- `/unban` - Remove restrictions from a banned user.
- `/banned` - List all currently banned users.

## Support and Development

For updates, tutorials, and technical support, join our official channel:
- **Telegram**: [NeoCloud Official](https://t.me/NeoCloud_Ofc)
- **Developer Support**: [Contact Support](https://t.me/NeoCloud_Ofc)

## License and Terms

- This project is maintained by [NeoCloud](https://t.me/NeoCloud_Ofc).
- Copying, modifying for resale, or selling this repository is strictly prohibited.
