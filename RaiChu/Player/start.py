
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I แดแด ๐ฝ๐ค๐ฉ ๐ฟ๐ช๐ฃ๐๐ฎ๐ ๐๐ช๐จ๐๐   
สแดแด สแดษดแดสแด สส [KIGO](https://t.me/INSANE_BOTS)
Thanks to add me ๐**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Handle", url="https://t.me/Shubhanshutya"
                    ),
                    InlineKeyboardButton(
                        "๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ข๐ฌ๐ญ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "How to add me๐คท", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       " ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ๐ฟ", url="https://t.me/godzilla_chatting"
                    ),
                    InlineKeyboardButton(
                        "๐๐ฉ๐๐๐ญ๐๐ฌ", url="https://t.me/INSANE_BOTS"
                    )
                ],[
                    InlineKeyboardButton(
                        "โ ๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉโ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
