import os

API_ID = os.environ.get('API_ID', '') 
API_HASH = os.environ.get('API_HASH', '') 
BOT_TOKEN = os.environ.get('BOT_TOKEN', '') 
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

ADMINS = list(int(i) for i in os.environ.get("ADMINS", "").split(" ")) if os.environ.get("ADMINS") else []
 
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

MONGODB = os.environ.get('MONGODB', '')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'linkfindbot') 
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'nvslinkbot')
UPDATE_CHANNEL =  os.environ.get('UPDATE_CHANNEL', 'tgnvs')
USERNAME = UPDATE_CHANNEL
RESULTS_COUNT = int(os.environ.get('RESULT_COUNTS', 3))
AUTO_DELETE = os.environ.get('AUTO_DELETE', 'True')
AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME', 300))
START_MSG = os.environ.get('START_MSG', '<b>Hey!,\nI am Link Search Bot.\n🤖I Can Search 🔍 What You Want❗\nMade With ❤ By @tgnvs</b>')
GROUP = os.environ.get('GROUP', 'nvshdmovielink')
FILEBOT = os.environ.get('FILEBOT', 'None')
BOT_USERNAME = os.environ.get('BOT_USERNAME', 'nvslinkbot')
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', 'tgnvs')
HOWTO = os.environ.get('HOWTO', 'https://t.me/tgnvs/8')
START_PIC = os.environ.get('START_PIC', 'https://graph.org/file/ff2999e57bf1ae1f99e7e.jpg')

#  Replit Config
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = True if REPLIT_APP_NAME and REPLIT_USERNAME else False 
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))


