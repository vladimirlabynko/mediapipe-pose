import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic


def process(input, output):


  cap = cv2.VideoCapture(input)

  if (cap.isOpened() == False):
    print("Error opening the video file")
# Obtain frame size information using get() method
  image_width = int(cap.get(3))
  image_height = int(cap.get(4))
  frame_size = (image_width, image_height)
  fps = cap.get(cv2.CAP_PROP_FPS)


# Initialize video writer object
  output = cv2.VideoWriter(
    output, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)


  with mp_holistic.Holistic(
    min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
      while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("empty frame.End process")
            # If loading a video, use 'break' instead of 'continue'.
          break

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        output.write(image)
  cap.release()
  output.release()
  cv2.destroyAllWindows()


input_video = ("test.mp4")
output_video = ("output.mp4")
process(input_video,output_video)


