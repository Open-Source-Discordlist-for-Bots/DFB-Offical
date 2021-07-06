import psutil
import platform

def get_ram_usage():
    """
    Obtains the absolute number of RAM bytes currently in use by the system.
    :returns: System RAM usage in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

developer = [775017772358434817, 703944517048598568, 705557092802625576]

class Emote:
    dfbEmote = "<:DFB:792539859419267142>"
    dfbLoading = "<a:WindowsLoading:797892629420572772>"
    dfbLoading2 = "<a:loading:808810373947195392>"
    cpu = "<:CPU:850775065305284608>"
    ram = "<:RAM:850774967330144286>"
    python = "<:python:796191053211631656>"
    pyCompiler = "<:pyCompiler:853294245455593502>"
    info = "<:dj_info:853295815338754119>"
    github = "<:Github:850774618934738974>"
    server = "<:server:862018984382693386>"


class Bot:
    Id = "847100391387824158"
    Version = "1.56-pre-1a"
    Repo = "https://github.com/Discordlist-for-Bots/dfbOfficalRewrite"
    Owner = "703944517048598568"
    OwnerMention = "<@703944517048598568>"


class Server:
    Backup = "https://discord.new/9rPgS6CncCFA"
    Invite = "https://discord.gg/9Hq7wqsmJy"


class Messages:
    OnStarted = "[OnStarted]: Bot started"
    OnMessageDeleted = "[OnMessageDeleted]: "
    BotOnOffline = "[BotOnOffline]: "
    OnToken = "[OnToken]: Someone tried to get the Bot Token!"


class Info:
    PyVer = platform.python_version()
    Cpu = f'{psutil.cpu_percent(4)} %'
    Ram = f"{psutil.virtual_memory()[2]} %"
    OS = f"{platform.system()} {platform.release()}"


class Colors:
    dfbColor = 0x5865F2
    procColor = 0xE4B400
    nprocColor = 0x277ECD
    certColor = 0x00FF00
    approveColor = 0x00FF00

class console:
    def print(args):
        print(args)