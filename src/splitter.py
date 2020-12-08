# Video Editing Functions
import cv2
import numpy as np
import os

from helper_functions import GetFrameWidthAndHeightFromCount, GetFrames

def splitVideo(video_location, number_of_splits = 1):
  filename, file_extension = os.path.splitext(video_location)
  print(file_extension)
  video_reader = cv2.VideoCapture(video_location)
  if (video_reader.isOpened() == False):
    print("Error opening the video file {}".format(video_location))
    return
  frame_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
  frame_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
  frames_per_second = int(video_reader.get(cv2.CAP_PROP_FPS))
  frame_width, frame_height = GetFrameWidthAndHeightFromCount(number_of_splits, frame_width, frame_height)
  video_writers = [cv2.VideoWriter('output_{}{}'.format(str(i), file_extension),cv2.VideoWriter_fourcc(*'mp4v'), frames_per_second, (frame_width,frame_height)) for i in range(0, number_of_splits)]
  print("Splitting Started")
  while(video_reader.isOpened()):
   ret, frame = video_reader.read()
   if ret == True:
     frames = GetFrames(frame, number_of_splits)
     for i in range(0, number_of_splits):
       video_writers[i].write(frames[i])
   else:
     break
  video_reader.release()
  for video_writer in video_writers:
    video_writer.release()
  print("Splitting Completed")