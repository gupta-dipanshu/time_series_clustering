import numpy as np
from glob import glob
import cv2

files = glob('../images/smoothened/*')

for i in files:
    im = cv2.imread(i)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    np.save(f'../images/numpy/{i[21:-4]}.npy', gray)
