import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

#lighness method to convert the image to gray scale
def luminosity_method(img):
    gray_img = img[:,:,0]*0.21 + img[:,:,1]*0.72 + img[:,:,2]*0.07
    return gray_img

#function to show the original and gray image
def show_image(img, gray_img):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Create a figure and axes
    axes[0].imshow(img)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(gray_img, cmap='gray')
    axes[1].set_title('Gray Image')
    axes[1].axis('off')
    plt.show()

#main function
def main():
    img = mpimg.imread('D:\AIO\AIO-Exercise\AIO-Exercise\Module2\Week1\Image_Processing\dog.jpeg') #path to the image
    gray_img = luminosity_method(img)
    print(gray_img[0, 0])
    show_image(img, gray_img)

if __name__ == '__main__':
    main()
