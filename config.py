import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 8367080346

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com" # shortner url 
SHORT_API = "" 
SHORT_TUT = "https://t.me/How_to_Download_7x/26"

# Bot Configuration
SESSION = "yato"
TOKEN = "8114977086:AAHrm3kjqx7qPiArD5NPqNXlKvUWAtuHTSg"
API_ID = "26047636"
API_HASH = "d8b1ed69ae1f937c5dd4d3cc8c8de440"
WORKERS = 5

DB_URI = "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Yato"

FSUBS = [[-1003182657982, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1002656509343   # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002656509343": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1002656509343": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [8367080346, 8525952693]
# Bot Settings
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": """<blockquote>ᴀʀᴀ ᴀʀᴀ {mention}</blockquote>
<blockquote> ɪ'ᴍ ᴀ ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ʜᴇʀᴇ ᴛᴏ ᴏʀɢᴀɴɪᴢᴇ, sᴀᴠᴇ, ᴀɴᴅ sʜᴀʀᴇ ʏᴏᴜʀ ꜰᴀᴠᴏʀɪᴛᴇ ꜰɪʟᴇs ᴡɪᴛʜ ʏᴏᴜʀ sᴘᴇᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ</blockquote>
<blockquote>✦ <a href="https://t.me/anime_xyz_offical">ᴀɴɪᴍᴇ xʏᴢ</a></blockquote>""",
    "FSUB": """<b><blockquote>⚠️ Hᴇʏ, {mention} ×</blockquote>
Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ {count}/{total} ᴄʜᴀɴɴᴇʟs ʏᴇᴛ. Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴘʀᴏᴠɪᴅᴇᴅ ʙᴇʟᴏᴡ, ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ.. !

<blockquote>›› ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ:  <a href="https://t.me/anime_xyz_offical">ᴀɴɪᴍᴇ xʏᴢ</a></blockquote>

❗Fᴀᴄɪɴɢ ᴘʀᴏʙʟᴇᴍs, ᴅᴍ @RioShin</b>""",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @anime_xyz_offical \n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/anime_xyz_offical'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @RioShin\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @RioShin</b></blockquote>",
    "REPLY": "<b>For More Join - @anime_xyz_offical</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://i.rj1.dev/lGdar.png",
    "FSUB_PHOTO": "https://i.rj1.dev/lGdar.png",
    "SHORT_PIC": "https://i.rj1.dev/lGdar.png",
    "SHORT": "https://i.rj1.dev/lGdar.png"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
