from translation import *
from pyrogram import Client, filters
from plugins.groups import group_send_handler
from plugins.database import collection
from pymongo import TEXT
from config import START_MSG, HOWTO, OWNER_USERNAME, GROUP, BOT_USERNAME, FILEBOT, START_PIC
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    collection.create_index([("title" , TEXT),("caption", TEXT)],name="movie_index")
    if len(m.command) == 1:
        return await m.reply_photo(f"{START_PIC}",
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('β€ Donation Link', url='https://upier.vercel.app/pay/tgnvs@axisbank')
                    ], 
                    [
                        InlineKeyboardButton("πΌππππ π²ππππππ", url="https://t.me/nvsmovielink"),
                        InlineKeyboardButton("Ι’Κα΄α΄α΄", url=f'https://t.me/{GROUP}')
                    ]
                ]
            )
        )
    else:
        return await group_send_handler(c,m)
