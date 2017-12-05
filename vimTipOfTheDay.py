#!/usr/bin/env python3

import requests
import socket
import html2text
import random
import re

minTipNumber = 1
maxTipNumber = 1678

def getVimTipOfTheDay():
    doesNotExist = True

    while doesNotExist:
        response = requests.get('''http://vim.wikia.com/wiki/VimTip{0}?useskin=monobook&printable=yes'''.format(random.randint(minTipNumber, maxTipNumber+1)))
        myParser = html2text.HTML2Text()
        myParser.ignore_links = True
        myParser.ignore_images = True
        myParser.unicode_snob = True
        cuteText = myParser.handle(response.text)
        matches = re.findall('has been removed', cuteText)
        matches2 = re.findall('does not exist', cuteText)
        if len(matches) or len(matches2):
            doesNotExist = True
        else:
            doesNotExist = False
    preCuteTip = cuteText.split('##  Comments')[0].split('* * *')[1]
    return preCuteTip


if __name__ == '__main__':
    theTip = getVimTipOfTheDay()

    print(theTip)
