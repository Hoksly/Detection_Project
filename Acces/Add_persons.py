import face_recognition as fr
import os


def main(faces_folder):
    folder = os.getcwd()
    try:
        with open(folder + '/Persons.txt', 'w') as t:
            t.close()
    except:
        pass

    faces = os.listdir(faces_folder)
    file = open(folder + '/Persons.txt', 'a')

    for face in faces:
        file_name = faces_folder +'/' + face

        if '.jpg' or '.png' in face:
            name = face[0:-4] + ': '
            photo = fr.load_image_file(file_name)
            enc = fr.face_encodings(photo, fr.face_locations(photo))
            enc = enc[0]
            encode = ''
            for i in enc:
                encode += str(i) + ' '
            file.write('\n')
            file.write(name + encode)
        elif '.jpeg' in face:
            name = face[0:-5] + ': '
            enc = fr.face_encodings(file_name, fr.face_locations(file_name))[0]
            encode = ''
            for i in enc:
                encode += str(i) + ' '
            file.write('\n')
            file.write(name + encode)
    file.close()

if __name__ == '__main__':
    folder = input('Folder:')
    main(folder)