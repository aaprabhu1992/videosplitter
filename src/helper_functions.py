
# This function has not been implemented
# The purpose of this function is to determine the frame height and width for the given number of splits
# This returns a single value of Frame Width and Frame Height
def GetFrameWidthAndHeightFromCount(number_of_splits, frame_width, frame_height):
  return frame_width, frame_height


# Takes a frame and return Individual Frames
def GetFrames(frame, number_of_splits):
  return [frame for i in range(0, number_of_splits)]