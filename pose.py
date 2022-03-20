import cv2
import mediapipe as mp
import argparse
import sys

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic



def process_video(args):
    cap = cv2.VideoCapture(args.input)
    if (cap.isOpened() == False):
        print("Error opening the video file")
    # Obtain frame size information using get() method
    image_width = int(cap.get(3))
    image_height = int(cap.get(4))
    frame_size = (image_width,image_height)
    fps = cap.get(cv2.CAP_PROP_FPS)


    # Initialize video writer object
    output = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while (cap.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool 
    # and the second is frame

            ret, frame = cap.read()

        
            if ret == True:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
      
        # Make detection
                results = holistic.process(image)
    
        # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Render detections
                try:
                    landmarks = results.pose_landmarks.landmark
                    mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Draw left hand connections
                    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             )
    # Draw right hand connections 
                    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             )
                except:
                    pass
                
                output.write(image)

            else:
                break
                
        sys.stdout.write(" \nDone!\n")
# Release the video capture object
        cap.release()
        output.release()
        cv2.destroyAllWindows()
        

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Mediapipe video processing')
    parser.add_argument('-i', "--input", dest='input', help='full path to input video that will be processed')
    parser.add_argument('-o', "--output", dest='output', help='full path for saving processed video output')
    args = parser.parse_args()

    if args.input is None or args.output is None:
        sys.exit("Please provide path to input and output video files! See --help")


    process_video(args)
