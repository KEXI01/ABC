from Opus.core.bot import AyuBot
from Opus.core.dir import dirr
from Opus.core.git import git
from Opus.core.userbot import Userbot
from Opus.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()
sudo()

app = AyuBot()

userbot = Userbot()

from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}
