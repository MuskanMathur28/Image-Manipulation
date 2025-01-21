 import cv2
from google.colab.patches import cv2_imshow  # Import for showing images in Colab
from google.colab import files  # For uploading files in Colab

# Step 1: Upload the image
uploaded = files.upload()

# Load the image (assuming only one file is uploaded)
image = cv2.imread(list(uploaded.keys())[0])

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found")
    exit()

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Resize the image (Example: Resize to 500x500)
resized_image = cv2.resize(image, (500, 500))

# Step 4: Crop the image (Example: Crop a region of interest)
# Crop the region (x1, y1, width, height)
cropped_image = image[50:300, 100:400]

# Step 5: Rotate the image (Example: Rotate by 45 degrees)
# Get the center of the image for rotation
height, width = image.shape[:2]
center = (width // 2, height // 2)

# Create a rotation matrix (rotate by 45 degrees)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)

# Apply the rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Step 6: Display the images
print("Original Image:")
cv2_imshow(image)

print("Grayscale Image:")
cv2_imshow(gray_image)

print("Resized Image:")
cv2_imshow(resized_image)

print("Cropped Image:")
cv2_imshow(cropped_image)

print("Rotated Image:")
cv2_imshow(rotated_image)
