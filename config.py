from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "19748416"))
API_HASH = getenv("API_HASH", "153a3aac0c31290d7ba83e53868cf19f")
BOT_TOKEN = getenv("BOT_TOKEN", "5225942879:AAGJNic5JZdQhkW2TaPEehMmjL910dRPlKQ")
SESSION_NAME = getenv("SESSION_NAME", "AgAllCk94Fyiwc1WkL58CTRhDb_uelZE41eviPybqchJ_SPC7OgYfgHx3CdUhqWd1lqyxkKm4sK3DVNRfOOBUSIje13-y9L52_EIgS8Nf-xozQf3Tk0EdUzmvOQElmMiB-DFpFazmKeFKF6BrHJEaxRVd380c8xm_xSO_PZxDmUnvzwYE-iHQn7btET8P8_HoaNEsQd5Ram7BLHwMEEhxu4nam8TO5MX1DxhZVIfhahzFVq6FhqFRE4adz-qdO5_z17-WeCOvyQhDK2_bH-A9_SfhGVqQxvIuYnohZPga0vxvPGD3U1ERim52du4gkYSOFGWFDlw9JQ8TcivB-dtbwmBAAAAATK0zRoA")

# mandatory vars
BOT_NAME = getenv("BOT_NAME", "SEMO")
OWNER_USERNAME = getenv("OWNER_USERNAME", "T_O_T_A1")
ALIVE_NAME = getenv("ALIVE_NAME", "AHMED")
BOT_USERNAME = getenv("BOT_USERNAME", "Sggdyvc_bot")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "T_O_T_A1")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "T_S_T1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SSE_MO")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("mongodb+srv://shikhar:shikhar@cluster0.6xzlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", '').split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5183920797").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5183920797").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/72b949b8ea801e787b8ed.jpg")
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/5f2e911c64cf25f99c591.jpg")
