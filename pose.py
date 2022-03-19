import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

input_video=("test.mp4")
output_video=("output.mp4")

cap = cv2.VideoCapture(input_video)

if (cap.isOpened() == False):
        print("Error opening the video file")
    # Obtain frame size information using get() method
image_width = int(cap.get(3))
image_height = int(cap.get(4))
frame_size = (image_width,image_height)
fps = cap.get(cv2.CAP_PROP_FPS)


    # Initialize video writer object
output = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)


with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    output.write(image)


cap.release()
output.release()
cv2.destroyAllWindows()