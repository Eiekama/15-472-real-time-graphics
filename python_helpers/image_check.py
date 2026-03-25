import cv2
import numpy as np
import argparse

def rgbe_to_rgb(image):
    rgb = (image[...,:3].astype(np.float32)+0.5) / 256.0
    exp = image[...,3].astype(np.float32) - 128.0
    rgb = rgb * np.power(2.0, exp[..., np.newaxis])
    return rgb

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("img1", help="path to first image")
    parser.add_argument("img2", help="path to second image")
    args = parser.parse_args()

    img1 = cv2.imread(args.img1, cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread(args.img2, cv2.IMREAD_UNCHANGED)

    img1 = rgbe_to_rgb(img1)
    img2 = rgbe_to_rgb(img2)

    one_m_two = cv2.subtract(img1, img2)
    two_m_one = cv2.subtract(img2, img1)
    cv2.imshow("image1", one_m_two)
    cv2.imshow("image2", two_m_one)
    cv2.waitKey(0)
    cv2.destroyAllWindows()