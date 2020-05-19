from modules.detection_class import Detection
import cv2
import face_recognition as fr
import os


def get_encodes_from_dict(dic):
    known_encodes = []
    for i in dic.values():
        known_encodes.append(i)
    return known_encodes


def compare(targets_encode: list, known_encodes: list):
    T = Detection()
    A = []
    l = len(known_encodes)
    for target_encode in targets_encode:
        result = fr.compare_faces(known_encodes, target_encode)
        if not True in result:
            T.save_face_encode(target_encode, 'Unknown Person{}'.format(l))
            l += 1
            A.append(True)
        else:
            A.append(False)
    if True in A:
        B = []
        for elements in enumerate(A):
            num, res = elements # num - index in list, res - bool; elements - Tuple
            if res:
                B.append(targets_encode[num])
        return True, B, A
    else:
        return False, None, None

Root = Detection()


def main():
    try:
        Root.create_files()
    except:
        pass
    #Root.create_files()

    known_encodes_and_names = Root.get_names_and_encodes()
    known_encodes = get_encodes_from_dict(known_encodes_and_names)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        f_l = fr.face_locations(frame)
        enc = fr.face_encodings(frame, f_l)

        res, l, faces = compare(enc, known_encodes)

        previous_len = len(known_encodes)
        if res:
            known_encodes.extend(l)
            for i in range(len(faces)):

                if faces[i]:
                    Root.save_face_image(frame, f_l[i], 'Unknown_Person{}.jpg'.format(i + previous_len))
                    previous_len += 1


if __name__ == '__main__':
    main()
