# Zoom maintains this much padding
WIDTH_PERCENTAGE = 9.00
HEIGHT_PERCENTAGE = 6.25


# Algorithm for the screen.(11 videos)
# Find the Smallest Square greater than equal to total videos. (16)
# Square root of this number (4)is the grrid size.
# Start filling from TOP till it fill each row. (First two rows)
# If it does not fit a particular row use centered justifcation to find the coordinates (Last 3 will be at the centers of the previous rows)


# This function has not been implemented
# The purpose of this function is to determine the frame height and width for the given number of splits
# This returns a single value of Frame Width and Frame Height
def GetFrameWidthAndHeightFromCount(number_of_splits, frame_width, frame_height):
    if number_of_splits == 3:
        return int((50 - WIDTH_PERCENTAGE) * frame_width/100), int((50 - HEIGHT_PERCENTAGE) * frame_height/100)
    if number_of_splits == 4:
        return int((50 - WIDTH_PERCENTAGE) * frame_width/100), int((50 - HEIGHT_PERCENTAGE) * frame_height/100)
    print("Data has not been defined for {} splits".format(str(number_of_splits)))
    return frame_width, frame_height


# Takes a frame and return Individual Frames
def GetFrames(frame, number_of_splits):
    (image_frame_height, image_frame_width, channels) = frame.shape
    frame_width, frame_height = GetFrameWidthAndHeightFromCount(number_of_splits, image_frame_width, image_frame_height)
    if number_of_splits == 3:
        split_coordinates = []
        start_height = int(HEIGHT_PERCENTAGE * image_frame_height / 100)
        start_width = int(WIDTH_PERCENTAGE * image_frame_width/ 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        start_height = int(HEIGHT_PERCENTAGE * image_frame_height/ 100)
        start_width = int(50 * image_frame_width/ 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        start_height = int(50 * image_frame_height / 100)
        start_width = int((25 + WIDTH_PERCENTAGE/2) * image_frame_width / 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        return split_coordinates
    if number_of_splits == 4:
        split_coordinates = []
        start_height = int(HEIGHT_PERCENTAGE * image_frame_height / 100)
        start_width = int(WIDTH_PERCENTAGE * image_frame_width/ 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        start_height = int(HEIGHT_PERCENTAGE * image_frame_height/ 100)
        start_width = int(50 * image_frame_width/ 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        start_height = int(50 * image_frame_height / 100)
        start_width = int(WIDTH_PERCENTAGE * image_frame_width/ 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        start_height = int(50 * image_frame_height / 100)
        start_width = int(50 * image_frame_width/ 100)
        split_coordinates.append(frame[start_height: start_height + frame_height, start_width : start_width + frame_width, :])
        return split_coordinates
    print("Data has not been defined for {} splits".format(str(number_of_splits)))
    return [frame for i in range(0, number_of_splits)]
