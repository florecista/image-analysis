import face_recognition
import os
import re

try:
    source_image = face_recognition.load_image_file("images_known/COL-Flagg.jpg")
    source_face_encoding = face_recognition.face_encodings(source_image)[0]

    known_faces = [
        source_face_encoding
    ]

    filelist = os.listdir('images_unknown')
    sorted_filelist = sorted(filelist)
    pattern = re.compile(r'[.](jpg|jpeg|png)$', re.IGNORECASE)
    for image_file in sorted_filelist[:]:
        if re.search(pattern, image_file):
            unknown_image = face_recognition.load_image_file('images_unknown/' + image_file)
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
            if results[0] == True:
                print(image_file + " is a match")
            else:
                print(image_file + " does not match")

except IndexError:
    print("I wasn't able to locate any faces in at least one of the images_unknown. Check the image files. Aborting...")
    quit()
