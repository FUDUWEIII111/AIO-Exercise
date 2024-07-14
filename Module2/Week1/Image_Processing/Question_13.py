import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def average_method(img):
    gray_img = np.mean(img, axis=2)
    return gray_img

def show_img(img, gray_img):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(gray_img, cmap='gray')
    axes[1].set_title('Gray Image')
    axes[1].axis('off')

    plt.show()

def main():
    img = mpimg.imread('D:\AIO\AIO-Exercise\AIO-Exercise\Module2\Week1\Image_Processing\dog.jpeg')
    gray_img = average_method(img)
    print(gray_img[0, 0])

    show_img(img, gray_img)

if __name__ == '__main__':
    main()
    