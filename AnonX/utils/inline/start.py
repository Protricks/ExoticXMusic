from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛤ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛤",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ ʜᴇʟᴩ ꭙ ᴄᴏᴍᴍᴀɴᴅs ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="˹sᴇᴛᴛɪɴɢs˼", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛤ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛤",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ ʜᴇʟᴩ ꭙ ᴄᴏᴍᴍᴀɴᴅs ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𓆩sᴜᴩᴩᴏʀᴛ𓆪", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="❣️ ᴏᴡɴᴇʀ ❣️", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴏᴜʀᴄᴇ ✨", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
