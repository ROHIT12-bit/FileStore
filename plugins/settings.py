from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.pyromod import ListenerTimeout
from config import OWNER_ID

#===============================================================#

def safe_get(dct, key, default="ᴇᴍᴘᴛʏ"):
    """Helper to safely get a value from dict or fallback."""
    return dct.get(key, default)

#===============================================================#

@Client.on_callback_query(filters.regex("^settings$"))
async def settings(client, query):
    total_fsub = len(getattr(client, "fsub_dict", {}))
    request_enabled = sum(1 for data in getattr(client, "fsub_dict", {}).values() if data[2])
    timer_enabled = sum(1 for data in getattr(client, "fsub_dict", {}).values() if data[3] > 0)
    
    total_db_channels = len(getattr(client, 'db_channels', {}))
    primary_db = getattr(client, 'primary_db_channel', 'Not set')
    
    msg = (
        f"<blockquote>✦ sᴇᴛᴛɪɴɢs ᴏғ @{client.username}</blockquote>\n"
        f"›› **ꜰꜱᴜʙ ᴄʜᴀɴɴᴇʟs:** `{total_fsub}` "
        f"(ʀᴇǫᴜᴇsᴛ: {request_enabled}, ᴛɪᴍᴇʀ: {timer_enabled})\n"
        f"›› **ᴅʙ ᴄʜᴀɴɴᴇʟs:** `{total_db_channels}` (ᴘʀɪᴍᴀʀʏ: `{primary_db}`)\n"
        f"›› **ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ:** `{getattr(client, 'auto_del', 0)}`\n"
        f"›› **ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ:** `{'✓ ᴛʀᴜᴇ' if getattr(client, 'protect', False) else '✗ ꜰᴀʟsᴇ'}`\n"
        f"›› **ᴅɪsᴀʙʟᴇ ʙᴜᴛᴛᴏɴ:** `{'✓ ᴛʀᴜᴇ' if getattr(client, 'disable_btn', False) else '✗ ꜰᴀʟsᴇ'}`\n"
        f"›› **ʀᴇᴘʟʏ ᴛᴇxᴛ:** `{getattr(client, 'reply_text', 'ɴᴏɴᴇ')}`\n"
        f"›› **ᴀᴅᴍɪɴs:** `{len(getattr(client, 'admins', []))}`\n"
        f"›› **sʜᴏʀᴛɴᴇʀ ᴜʀʟ:** `{getattr(client, 'short_url', 'ɴᴏᴛ sᴇᴛ')}`\n"
        f"›› **ᴛᴜᴛᴏʀɪᴀʟ ʟɪɴᴋ:** `{getattr(client, 'tutorial_link', 'ɴᴏᴛ sᴇᴛ')}`\n"
        f"›› **sᴛᴀʀᴛ ᴍᴇssᴀɢᴇ:**\n<pre>{safe_get(client.messages, 'START')}</pre>\n"
        f"›› **sᴛᴀʀᴛ ɪᴍᴀɢᴇ:** `{bool(safe_get(client.messages, 'START_PHOTO', ''))}`\n"
        f"›› **ꜰᴏʀᴄᴇ sᴜʙ ᴍᴇssᴀɢᴇ:**\n<pre>{safe_get(client.messages, 'FSUB')}</pre>\n"
        f"›› **ꜰᴏʀᴄᴇ sᴜʙ ɪᴍᴀɢᴇ:** `{bool(safe_get(client.messages, 'FSUB_PHOTO', ''))}`\n"
        f"›› **ᴀʙᴏᴜᴛ ᴍᴇssᴀɢᴇ:**\n<pre>{safe_get(client.messages, 'ABOUT')}</pre>\n"
        f"›› **ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ:**\n<pre>{getattr(client, 'reply_text', '')}</pre>"
    )
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton('ꜰꜱᴜʙ ᴄʜᴀɴɴᴇʟꜱ', 'fsub'), InlineKeyboardButton('ᴅʙ ᴄʜᴀɴɴᴇʟꜱ', 'db_channels')],
        [InlineKeyboardButton('ᴀᴅᴍɪɴꜱ', 'admins'), InlineKeyboardButton('ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ', 'auto_del')],
        [InlineKeyboardButton('ʜᴏᴍᴇ', 'home'), InlineKeyboardButton('›› ɴᴇxᴛ', 'settings_page_2')]
    ])
    
    await query.message.edit_text(msg, reply_markup=reply_markup)

#===============================================================#

@Client.on_callback_query(filters.regex("^settings_page_2$"))
async def settings_page_2(client, query):
    total_fsub = len(getattr(client, "fsub_dict", {}))
    request_enabled = sum(1 for data in getattr(client, "fsub_dict", {}).values() if data[2])
    timer_enabled = sum(1 for data in getattr(client, "fsub_dict", {}).values() if data[3] > 0)
    
    total_db_channels = len(getattr(client, 'db_channels', {}))
    primary_db = getattr(client, 'primary_db_channel', 'Not set')
    
    msg = (
        f"<blockquote>✦ sᴇᴛᴛɪɴɢs ᴏғ @{client.username}</blockquote>\n"
        f"›› **ꜰsᴜʙ ᴄʜᴀɴɴᴇʟs:** `{total_fsub}` "
        f"(ʀᴇǫᴜᴇsᴛ: {request_enabled}, ᴛɪᴍᴇʀ: {timer_enabled})\n"
        f"›› **ᴅʙ ᴄʜᴀɴɴᴇʟs:** `{total_db_channels}` (ᴘʀɪᴍᴀʀʏ: `{primary_db}`)\n"
        f"›› **ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ:** `{getattr(client, 'auto_del', 0)}`\n"
        f"›› **ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ:** `{'✓ ᴛʀᴜᴇ' if getattr(client, 'protect', False) else '✗ ꜰᴀʟsᴇ'}`\n"
        f"›› **ᴅɪsᴀʙʟᴇ ʙᴜᴛᴛᴏɴ:** `{'✓ ᴛʀᴜᴇ' if getattr(client, 'disable_btn', False) else '✗ ꜰᴀʟsᴇ'}`\n"
        f"›› **ʀᴇᴘʟʏ ᴛᴇxᴛ:** `{getattr(client, 'reply_text', 'ɴᴏɴᴇ')}`\n"
        f"›› **ᴀᴅᴍɪɴs:** `{len(getattr(client, 'admins', []))}`\n"
        f"›› **sʜᴏʀᴛɴᴇʀ ᴜʀʟ:** `{getattr(client, 'short_url', 'ɴᴏᴛ sᴇᴛ')}`\n"
        f"›› **ᴛᴜᴛᴏʀɪᴀʟ ʟɪɴᴋ:** `{getattr(client, 'tutorial_link', 'ɴᴏᴛ sᴇᴛ')}`\n"
        f"›› **sᴛᴀʀᴛ ᴍᴇssᴀɢᴇ:**\n<pre>{safe_get(client.messages, 'START')}</pre>\n"
        f"›› **sᴛᴀʀᴛ ɪᴍᴀɢᴇ:** `{bool(safe_get(client.messages, 'START_PHOTO', ''))}`\n"
        f"›› **ꜰᴏʀᴄᴇ sᴜʙ ᴍᴇssᴀɢᴇ:**\n<pre>{safe_get(client.messages, 'FSUB')}</pre>\n"
        f"›› **ꜰᴏʀᴄᴇ sᴜʙ ɪᴍᴀɢᴇ:** `{bool(safe_get(client.messages, 'FSUB_PHOTO', ''))}`\n"
        f"›› **ᴀʙᴏᴜᴛ ᴍᴇssᴀɢᴇ:**\n<pre>{safe_get(client.messages, 'ABOUT')}</pre>\n"
        f"›› **ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ:**\n<pre>{getattr(client, 'reply_text', '')}</pre>"
    )
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton('ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ', 'protect'), InlineKeyboardButton('ᴘʜᴏᴛᴏs', 'photos')],
        [InlineKeyboardButton('ᴛᴇxᴛs', 'texts'), InlineKeyboardButton('sʜᴏʀᴛɴᴇʀ', 'shortner')],
        [InlineKeyboardButton('‹ ᴘʀᴇᴠ', 'settings'), InlineKeyboardButton('ʜᴏᴍᴇ', 'home')]
    ])
    
    await query.message.edit_text(msg, reply_markup=reply_markup)
