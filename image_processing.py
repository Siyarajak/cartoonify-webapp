import cv2
import numpy as np

def cartoonify_image_steps(image, blur_ksize=5, bilateral_d=9):
    steps = []

    # Step 1: Original
    steps.append(image)

    # Step 2: Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    steps.append(gray)

    # Step 3: Smooth grayscale
    gray_blur = cv2.medianBlur(gray, blur_ksize)
    steps.append(gray_blur)

    # Step 4: Edge detection
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,
                                  9, 9)
    steps.append(edges)

    # Step 5: Bilateral filter
    color = cv2.bilateralFilter(image, bilateral_d, 300, 300)
    steps.append(color)

    # Step 6: Cartoon image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    steps.append(cartoon)

    return steps
