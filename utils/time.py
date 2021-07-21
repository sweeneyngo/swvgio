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


def getTitle():
    currentTime = getPreviousMonth().strftime("%B %Y")
    return f"vgperson's Vocaloid Highlights: {currentTime}"


def getDescription():
    return f"{getTitle()}: A compilation of known videos on Youtube from vgperson's Vocaloid Highlights for the following month. All videos listed were attempted to find versions available on Youtube, but there is no guarentee that every video is listed. To see the full list curated by vgperson, please consult here: {getSearchQuery()}."
