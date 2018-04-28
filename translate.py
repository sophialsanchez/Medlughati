# Translation function made by Fares Al Ghazy for NYAUD 2018 hackathon

from textblob import TextBlob as TB


# take a string and translate it
def translate(text, originallanguage, newlanguage):
    return TB("String").translate(from_lang=originallanguage, to=newlanguage)