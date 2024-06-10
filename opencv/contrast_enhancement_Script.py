contrastPercentage = 30

# Clip the values to [0,255] and change it back to uint8 for display
# this will increase the pixel values using contrastPercentage 
# the contrastImage will have pixel values greater then 255 and datatype would be float
contrastImage = image * (1+contrastPercentage/100) 
print("Max value - ", np.max(contrastImage)) # it will be greater then 255 
print("Dtype - ", contrastImage.dtype) # it will be float

# This will clip the values of contrastImage to 255
clippedContrastImage = np.clip(contrastImage, 0, 255)  
print("Max value after clipping - ",np.max(clippedContrastImage)) # it will show 255 

# This will conert the datatype to uint
contrastHighClippedUint8 = np.uint8(clippedContrastImage)
print("data type - ", contrastHighClippedUint8.dtype) # it will show unint8
# The final output image is in the range [0,255]


# We will repeat the same operation again, but in float datatype
# Convert the range to [0,1] and keep it in float format
contrastHighNormalized = (image * (1+contrastPercentage/100))/255
contrastHighNormalized01Clipped = np.clip(contrastHighNormalized,0,1)

# The same image as contrastHighClippedUint8 but the values are in float datatype and in range [0,1]
print("Datatype of output by this method -  ",contrastHighNormalized01Clipped.dtype)

plt.figure(figsize=[20,20])
plt.subplot(131);plt.imshow(image[...,::-1]);plt.title("original Image");
plt.subplot(132);plt.imshow(contrastHighClippedUint8[...,::-1]);plt.title("converted back to uint8");
plt.subplot(133);plt.imshow(contrastHighNormalized01Clipped[...,::-1]);plt.title("Normalized float to [0, 1]");
