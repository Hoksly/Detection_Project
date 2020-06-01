import time
import cv2
import face_recognition as fr
import numpy as np
import os


def get_names_and_encodes_from_file():
    folder = os.getcwd()
    try:
        with open(folder + '/Persons.txt', 'w') as t:
            t.close()
    except:
        pass
    file = open(folder + '/Persons.txt', 'r')
    names_and_enc = file.read().split('\n')
    if len(names_and_enc) > 100:
        d = {}

        for line in names_and_enc:
            enc = np.array(list(map(float, line[line.index(':') + 2:].split())))
            name = line[0:line.index(':')]
            d.update({name: enc})
        return d
    else:
        return {}


def get_encodes_from_dict(dic):
    return list(dic.values())


def compare(targets_encode, known_encodes_and_names):
    """

    :param known_encodes_and_names: dict
    :type targets_encode: list
    """
    enc = get_encodes_from_dict(known_encodes_and_names)

    for target_encode in targets_encode:
        res = fr.compare_faces(enc, target_encode)
        if True in res:
            n = res.index(True)
            name = list(known_encodes_and_names.keys())[n]
            return name
        else:
            return 'Unknown Person'


def main():
    known_encodes_and_names = get_names_and_encodes_from_file()

    cap = cv2.VideoCapture(0)

    name = ''
    enc = []
    while True:

        ret, frame = cap.read()
        f_l = fr.face_locations(frame)
        if len(f_l) > 0:
            new_enc = fr.face_encodings(frame, f_l)
            try:
                a = fr.compare_faces(enc, new_enc)
            except:
                a = [False]
            if True not in a:

                new_name = compare(new_enc, known_encodes_and_names)
                enc = new_enc
                if name != new_name:
                    name = new_name
                    if name != "Unknown Person":
                        print('Hello ' + name)
                    else:
                        print('Unknown Person')
                else:
                    continue
            else:
                time.sleep(3)
        
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
