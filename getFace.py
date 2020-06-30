import dlib             # pip install cmake, pip install dlib
from PIL import Image   # pip install Image
from skimage import io  # pip install scikit-image scipy matplotlib
import matplotlib.pyplot as plt # pip install plt
import glob
import os

if __name__ == "__main__":
    print("this is main")

class GetFace:
    from_path = 'img/'
    to_path = 'formed_img/'

    def __init__(self, keyWord, from_path=None, to_path=None):
        self.keyWord = keyWord
        if from_path != None:
            self.from_path = from_path
        if to_path != None:
            self.to_path = to_path

        if not os.path.exists(self.to_path):
            os.makedirs(self.to_path)

        self.files = self.from_path + self.keyWord + "*" + ".jpg"

    def detect_faces(self, image):
        face_detector = dlib.get_frontal_face_detector()

        detected_faces = face_detector(image, 1)
        face_frames = [(x.left(), x.top(),
                        x.right(), x.bottom()) for x in detected_faces]

        return face_frames

    def cropAndSaveFace(self, detected_faces, image, image_path):
        for n, face_rect in enumerate(detected_faces):
            face = Image.fromarray(image).crop(face_rect)
            plt.subplot(1, len(detected_faces), n+1)
            plt.axis('off')
            plt.imshow(face)
            tempFilePath = "formed_img/formed_"+image_path
            plt.savefig(tempFilePath, bbox_inches='tight')

    def run(self):
        for image_path in glob.glob(self.files):
            image = io.imread(image_path)
            detected_faces = self.detect_faces(image)
            self.cropAndSaveFace(detected_faces, image, image_path[len(self.from_path):])

