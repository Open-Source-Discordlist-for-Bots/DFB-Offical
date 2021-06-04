onstarted = "[OnStarted]:"
onjoined = "[OnJoined]:"
onleft = "[OnLeft]:"
onerror = "[OnError]:"
onmessagedeleted = "[OnMessageDeleted]:"
botonoffline = "[BotOnOffline]:"

def onStarted():
    print(f"{onstarted} Bot started")

def onMemberJoined(member):
    print(f"{onjoined} {member} joined, and was given the online role")

def onMemberLeft(member):
    print(f"{onleft} {member} has left the server")

def onError(error):
    print(f"{onerror} {error}")

def onMessageDeleted(message):
    print(f"{onmessagedeleted} Message deleted in {message.channel.name}")

def botOnOffline(after, before):
    print(f"{botonoffline} {before.name} is offline!")

