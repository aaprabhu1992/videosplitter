# Parsing Arguments
import argparse

from splitter import splitVideo

parser = argparse.ArgumentParser()
parser.add_argument('--video', dest = 'videoLocation', help='file to be split', type=str)
parser.add_argument('--splits', dest = 'splitCount', help='file to be split', type=int)


args = parser.parse_args()
videoLocation = args.videoLocation
splitCount = args.splitCount

splitVideo(videoLocation, splitCount)



