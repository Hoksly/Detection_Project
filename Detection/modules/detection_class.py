import face_recognition
import cv2
import os
import numpy as np


def cot(line):
    dot = line.index(':')
    Name = line[0:dot]
    encodes_line = line[(dot + 2):]
    del line
    A = list(map(float, encodes_line.split()))
    return Name, np.array(A)


def save_face_encode(file_link, encode, target_name):
    file = open(file_link, 'a')
    file.write('\n')
    sr = target_name + ': '
    for i in encode:
        sr += str(i) + ' '
    file.write(sr)
    file.close()





class Detection:

    def __init__(self):
        folder = os.getcwd()
        self.Faces_folder = folder + '/Face_folder'
        self.Files_folder = folder + '/Files_folder'
        self.encode_file = self.Files_folder + '/encodes_file.txt'
        '''
        self.folder = folder
        if len(folder) > 3:
            self.Faces_folder = folder + '/Face_folder'
            self.Files_folder = folder + '/Files_folder'
            self.encode_file = folder + self.Files_folder + '/encodes_file.txt'
        else:

            self.Faces_folder = 'Face_folder'
            self.Files_folder = 'Files_folder'
            self.encode_file = self.Files_folder + '/encodes_file.txt'
        '''

    def create_files(self):
        try:
            os.mkdir(self.Faces_folder)
            os.mkdir(self.Files_folder)

            with open(self.encode_file, 'w') as f:
                f.close()
        except:
            pass

    @staticmethod
    def cot(line):
        dot = line.index(':')
        Name = line[0:dot]
        encodes_line = line[(dot + 2):]
        del line
        A = list(map(float, encodes_line.split()))
        return Name, np.array(A)

    def get_names_and_encodes(self):
        file = open(self.encode_file, 'r')
        encodes = {}
        A = list(file.read().split('\n'))
        for line in A:
            if len(line) > 2:
                Name, encode = cot(line)
                encodes[Name] = encode
        file.close()
        return encodes

    def save_face_encode(self, encode, target_name):
        file = open(self.encode_file, 'a')
        file.write('\n')
        sr = target_name + ': '
        for i in encode:
            sr += str(i) + ' '
        file.write(sr)
        file.close()

    def save_faces_encode(self, encodes, Names_list=None):
        if Names_list is not None:
            i = 1
            while i < (len(Names_list) + 1):
                save_face_encode(self.encode_file, encodes[i], Names_list[i])
                i += 1
        else:
            i = 0
            while i < len(encodes):
                save_face_encode(self.encode_file, encodes[i], 'Unknown Pesron{0}'.format(str(i)))
                i += 1

    def save_face_image(self, image, location, name, koef=1.2):
        x1, y1, x2, y2 = location
        x1, y1, x2, y2 = int(x1 / koef), int(y1 * koef), int(x2 * koef), int(y2 / koef)
        cv2.imwrite(self.Faces_folder + '/' + name, image[x1:x2, y2:y1])









