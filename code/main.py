import datetime
import os
from insta import scrapeVideos
import config
from compile import makeCompilation
num_to_month = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "July",
    8: "Aug",
    9: "Sept",
    10: "Oct",
    11: "Nov",
    12: "Dec"
} 

INTRO_VID = '' # SET AS '' IF YOU DONT HAVE ONE
OUTRO_VID = ''
TOTAL_VID_LENGTH = 14*60
MAX_CLIP_LENGTH = 50
MIN_CLIP_LENGTH = 5

now = datetime.datetime.now()
videoDirectory = "./Cars_" + num_to_month[now.month].upper() + "_" + str(now.year) + "_V" + str(now.day) + "/"
outputFile = "./" + num_to_month[now.month].upper() + "_" + str(now.year) + "_v" + str(now.day) + ".mp4"

if not os.path.exists(videoDirectory):
    os.makedirs(videoDirectory)

def run():
    print("Scraping Videos...")
    scrapeVideos(username = config.IG_USERNAME,
                 password = config.IG_PASSWORD,
                 output_folder = videoDirectory,
                  days=1)
    print("Scraped Videos!")

    print("Making Compilation...")
    makeCompilation(path = videoDirectory,
                    introName = INTRO_VID,
                    outroName = OUTRO_VID,
                    totalVidLength = TOTAL_VID_LENGTH,
                    maxClipLength = MAX_CLIP_LENGTH,
                    minClipLength = MIN_CLIP_LENGTH,
                    outputFile = outputFile)
    print("Made Compilation!")
if __name__=='__main__':
    run()