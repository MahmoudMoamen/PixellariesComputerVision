from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open(r"C:\Users\yaraa\OneDrive\Desktop\semester 9\Computer Vision\img2 - Copy.png")
width, height = img.size

# histogram and cumulative histogram

intensity_counts = [0] * 256  # initialize a list of 256 zeros
cumulative_counts = [0] * 256  # initialize a list of 256 zeros
color_percentage = [0] * 256    # initialize a list of 256 zeros
total_pixels = width * height

for y in range(height):
    for x in range(width):
        intensity = img.getpixel((x, y))
        intensity_counts[intensity] += 1

cumulative_counts[0] = intensity_counts[0]
color_percentage[0] = intensity_counts[0] / total_pixels
for i in range(1, 256):
    cumulative_counts[i] = cumulative_counts[i-1] + intensity_counts[i]
    color_percentage[i] = ((cumulative_counts[i-1] + intensity_counts[i]) / total_pixels)*100

plt.subplot(1, 3, 1)
plt.bar(range(256), intensity_counts)
plt.title('Histogram')

plt.subplot(1, 3, 2)
plt.bar(range(256), cumulative_counts)
plt.title('Cumulative Histogram')

plt.subplot(1, 3, 3)
plt.bar(range(256), color_percentage)
plt.title('Color Percentage cumulative histogram')

plt.show()



# color covering percentage

def color_covering_percentage(percentage):
    x1 = 0
    x2 = 0
    for x in range(256):
        if color_percentage[x] >= percentage:
            x1 = x
            break
    for x in range(256-1,0,-1):
        if color_percentage[x] <= 100-percentage:
            x2 = x
            break
    return x1, x2

p = 10
print(p)
x1, x2 = color_covering_percentage(p)
print(x1)
print(x2)


# histogram equalization


def histogram_equalization(image, min_intensity, max_intensity):
    width, height = image.size
    
    # histogram and cumulative histogram
    intensity_counts = [0] * 256  # initialize a list of 256 zeros
    cumulative_counts = [0] * 256  # initialize a list of 256 zeros
    color_percentage = [0] * 256    # initialize a list of 256 zeros
    total_pixels = width * height

    for y in range(height):
        for x in range(width):
            intensity = image.getpixel((x, y))
            intensity_counts[intensity] += 1

    cumulative_counts[0] = intensity_counts[0]
    color_percentage[0] = intensity_counts[0] / total_pixels
    for i in range(1, 256):
        cumulative_counts[i] = cumulative_counts[i-1] + intensity_counts[i]
        color_percentage[i] = ((cumulative_counts[i-1] + intensity_counts[i]) / total_pixels)*100

    # color covering percentage
    x1, x2 = color_covering_percentage(min_intensity)

    # histogram equalization
    new_image = []
    for y in range(height):
        for x in range(width):
            intensity = image.getpixel((x, y))
            new_intensity = (cumulative_counts[intensity] - cumulative_counts[x1]) * 255 / (cumulative_counts[x2] - cumulative_counts[x1])
            new_image.append(new_intensity)
    final_image = Image.new('L', (width, height))
    final_image.putdata(new_image)

    return final_image


plt.show()

# greyscale transformation
def greyscale_transformation(img, x1, y1, x2, y2):
    width, height = img.size
    new_image = []
    for y in range(height):
        for x in range(width):
            intensity = img.getpixel((x, y))
            if intensity <= x1:
                new_intensity = (intensity * y1) / x1
            elif intensity > x1 and intensity <= x2:
                new_intensity = (((y2 - y1) / (x2 - x1)) * (intensity - x1)) + y1
            else:
                new_intensity = (((255 - y2) / (255 - x2)) * (intensity - x2)) + y2
            new_image.append(new_intensity)
    final_image = Image.new('L', (width, height))
    final_image.putdata(new_image)
    return final_image
