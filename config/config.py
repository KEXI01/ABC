import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "5400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400"))
LOGGER_ID = int(getenv("LOGGER_ID", ""))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6257927828").split()))

PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-VenomMusic-01-02")
EXTRA_PLUGINS = getenv("EXTRA_PLUGINS", "False")
EXTRA_PLUGINS_REPO = getenv("EXTRA_PLUGINS_REPO", "https://github.com/venombolteop/Extra-plugins")
EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 5800))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/KEXI01/ABC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/storm_techh")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/storm_core")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/venombolteop/VenomMusic")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2d3fd5ccdd3d43dda6f17864d8eb7281")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "48d311d8910a4531ae81205e1f754d27")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "235"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "255"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
SET_CMDS = getenv("SET_CMDS", "True")

raw_sessions = getenv("STRING_SESSIONS", "")
STRING_SESSIONS = list(map(str.strip, raw_sessions.split(","))) if raw_sessions else []

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Opuslogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/Oku.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/9077cd2ba5818efef2d28.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://graph.org/file/eb1e2b58e17964083db73.jpg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "https://envs.sh/Olk.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://envs.sh/Ol4.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://envs.sh/Olr.jpg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://envs.sh/Olr.jpg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://envs.sh/Olk.jpg")
SOUNCLOUD_IMG_URL = getenv("SOUNDCLOUD_IMG_URL", "https://envs.sh/Olk.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://envs.sh/Olk.jpg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/Olk.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/Olk.jpg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/Olk.jpg")

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

def seconds_to_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

for url, label in [
    (SUPPORT_CHANNEL, "SUPPORT_CHANNEL"),
    (SUPPORT_GROUP, "SUPPORT_GROUP"),
    (UPSTREAM_REPO, "UPSTREAM_REPO"),
    (GITHUB_REPO, "GITHUB_REPO"),
    (PING_IMG_URL, "PING_IMG_URL"),
    (PLAYLIST_IMG_URL, "PLAYLIST_IMG_URL"),
    (GLOBAL_IMG_URL, "GLOBAL_IMG_URL"),
    (STATS_IMG_URL, "STATS_IMG_URL"),
    (TELEGRAM_AUDIO_URL, "TELEGRAM_AUDIO_URL"),
    (TELEGRAM_VIDEO_URL, "TELEGRAM_VIDEO_URL"),
    (STREAM_IMG_URL, "STREAM_IMG_URL"),
    (SOUNCLOUD_IMG_URL, "SOUNDCLOUD_IMG_URL"),
    (YOUTUBE_IMG_URL, "YOUTUBE_IMG_URL"),
]:
    if url and not re.match(r"(?:http|https)://", url):
        print(f"[ERROR] - Your {label} url is wrong. Please ensure that it starts with https://")
        sys.exit()
