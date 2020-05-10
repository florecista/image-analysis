import face_recognition
import cv2

class recognize_target_video():
    def findTarget(self, videofile, imagefile):
        input_movie = cv2.VideoCapture(videofile)
        image = face_recognition.load_image_file(imagefile)
        face_encoding = face_recognition.face_encodings(image)[0]

        known_faces = [
            face_encoding
        ]

        frame_number = 0

        result = False

        while True:
            # Grab a single frame of video
            ret, frame = input_movie.read()
            frame_number += 1
            print('Processing frame number : ' + str(frame_number))
            # Quit when the input video file ends
            if not ret:
                break

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
                if match[0]:
                    result = True

        # All done!
        input_movie.release()
        cv2.destroyAllWindows()

        return result

def main():
    app = recognize_target_video()
    result = app.findTarget("video/Obama.mp4", "images_unknown/Obama.jpg")
    print('Target is in video : ' + str(result))

if __name__ == "__main__":
    main()