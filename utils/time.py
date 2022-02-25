from datetime import date, timedelta, datetime


def getTime():
    return datetime.now()


def getPreviousMonth():
    today = date.today().replace(day=1)
    t = today - timedelta(days=1)
    return t


def getSearchQuery():
    currentTime = getPreviousMonth().strftime("%Y-%m")
    return f"https://vgperson.com/vocalhighlights.php?m={currentTime}"


def getTitle(mode):
    if mode == 0:
        currentTime = getPreviousMonth().strftime("%b'%y: Stand-Outs")
    else:
        currentTime = getPreviousMonth().strftime("%b'%y: Worth Your Time")

    return f"{currentTime}"


def getDescription(unavailable, banned_countries):

    description = f"WARNING: \nCan't guarantee every video is listed!\n\n\nrestricted ➤\n"

    for u in banned_countries:
        description += f"[{u[0]}]: {u[1]}\n"

    description += f"\n\nunavailable ➤"

    for c in unavailable:
        description += f"[{c}]\n"

    description += f"\n\n\nTo see the full list curated by vgperson, please consult here: {getSearchQuery()}."
    return description
