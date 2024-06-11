import cv2

#Configurables
source = "bts1.jpeg"
destination = 'newImage.png' 
#percent by which image is resized
scale_percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)

#calculate the 50 percent of original dimension
N_width = int(image.shape[1] * scale_percent/100)
N_height = int(image.shape[0] * scale_percent/100)

# resize image
output = cv2.resize(image, (N_width,N_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)