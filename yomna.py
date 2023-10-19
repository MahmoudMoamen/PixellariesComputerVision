from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import wget



#image_url="https://networkcameratech.com/wp-content/uploads/2016/10/HIKVISION-DS-2CD2142FWD-I_2016-Nov-09_21_59_05.png"
#image_filename = wget.download(image_url)
#image2_url="https://networkcameratech.com/wp-content/uploads/2016/10/HIKVISION-DS-2CD2142FWD-I_2016-Nov-09_21_52_01.png"
#image2_filename = wget.download(image2_url)
#image3_url="https://networkcameratech.com/wp-content/uploads/2016/10/AXISP3364_2016-Oct-27_03_50_22.png"
#image3_filename = wget.download(image3_url)
#image_test= "https://images.squarespace-cdn.com/content/v1/5eb9df33b77a9729b4d3b5f9/2f4bbcfd-87c2-4253-a62e-971770630976/ghost+1.png"
#image_test_filename = wget.download(image_test)

im= Image.open("HIKVISION-DS-2CD2142FWD-I_2016-Nov-09_21_59_05.png").convert("L")
im2= Image.open("HIKVISION-DS-2CD2142FWD-I_2016-Nov-09_21_52_01.png").convert("L")
im3= Image.open("AXISP3364_2016-Oct-27_03_50_22.png").convert("L")
imtest= Image.open("ghost+1.png").convert("L")



pixel_intensity = [0]*256 
cumulative_intensity = [0]*256


#plot the histogram
for pixel in imtest.getdata():
   
    intensity = pixel
    
    
    pixel_intensity[intensity] += 1

#plt.plot(range(256), pixel_intensity, color='blue')
#plt.show()


cumulative_sum = 0
for i in range(256):
    cumulative_sum += pixel_intensity[i]
    cumulative_intensity[i] = cumulative_sum




#plt.plot(range(256), cumulative_intensity, color='red')
#plt.show()



    # Open the image

im1_array = np.array(im)
im2_array = np.array(im2)
im3_array = np.array(im3)
imtest_array = np.array(imtest)
def contrast_stretching(im_array, a, b, c, d):
    for i in range(im_array.shape[0]):
        for j in range(im_array.shape[1]):
            if im_array[i][j] > d:
                im_array[i][j] = b
            elif im_array[i][j] < c:
                im_array[i][j] = a
            else:
                im_array[i][j] = (im_array[i][j] - c)*(b-a)/(d-c) + a
    return im_array
imtest_array = contrast_stretching(im2_array, 0, 255, 10, 90)


#convert imtest_array to image
imtest2 = Image.fromarray(imtest_array)
pixel_intensity = [0]*256
for pixel in imtest.getdata():
   
    intensity = pixel
    
    
    pixel_intensity[intensity] += 1
cumulative_intensity = [0]*256
cumulative_sum = 0
for i in range(256):
    cumulative_sum += pixel_intensity[i]
    cumulative_intensity[i] = cumulative_sum
#plt.plot(range(256), pixel_intensity, color='green')
#plt.show()
#plt.plot(range(256), cumulative_intensity, color='black')
#plt.show()

imtest2.show()