#### Also need to install onxruntime! ###
# pip install onnxruntime
# pip install rembg
# pip install Pillow
from rembg import remove
from PIL import Image


# Removes the background from an image and saves the result
def remove_background(input_path, output_path):
    # Validate input and output paths
    if (
        not input_path
        or input_path == ""
        or output_path == ""
        or not input_path.endswith((".png", ".jpg", ".jpeg"))
        or not output_path
    ):
        print("Ensure file types are png, jpg, or jpeg and paths are valid")
        exit(1)

    # Opens and removes the background from the image
    with Image.open(input_path) as img:
        result = remove(img)
        result.save(output_path)
        print(f"Background removed and saved as {output_path}")


# Example
if __name__ == "__main__":
    input_path = "./myBeautifulImage.png"  # path to the input image (include file extension name)
    output_path = "./../Example.png"  # path to save the Image (including the file extension name)

    # Call the function
    remove_background(input_path, output_path)
