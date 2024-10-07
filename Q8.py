# Function to invert the colors of an RGB image
def invert_colors(image):
    # Iterate over each pixel (row)
    for i in range(len(image)):
        # Iterate over each pixel (column)
        for j in range(len(image[i])):
            # Get the current pixel's RGB values
            red, green, blue = image[i][j]
            # Invert the RGB values (255 - current value)
            image[i][j] = [255 - red, 255 - green, 255 - blue]
    return image

# Example 3x3 RGB image (each pixel has [R, G, B] values)
image = [
    [[100, 150, 200], [50, 100, 150], [0, 50, 100]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
    [[200, 100, 50], [150, 50, 0], [100, 50, 0]]
]

# Print original image
print("Original Image:")
for row in image:
    print(row)

# Invert the colors
inverted_image = invert_colors(image)

# Print inverted image
print("\nInverted Image:")
for row in inverted_image:
    print(row)
