from datetime import datetime

def getSearchQuery():
    current_time = datetime.now().strftime("%Y-%m")
    return f'https:\//vgperson.com/vocalhighlights.php?m={current_time}'

def getTitle():
    current_time = datetime.now().strftime("%B %Y")
    return f'vgperson\'s Vocaloid Highlights: {current_time}'

def getDescription():
    current_time = datetime.now().strftime("%B %Y")
    return f'{getTitle()}: A compilation of known videos on Youtube from vgperson\'s Vocaloid Highlights for the following month. All videos listed were attempted to find versions available on Youtube, but there is no guarentee that every video is listed. To see the full list curated by vgperson, please consult here: {getSearchQuery()}.'
