import os
import argparse
from PIL import Image, ImageOps


def get_args():
    """Get commmand line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument(
        "--output", help="Path to the output image", default="", type=str
    )
    args = parser.parse_args()
    return vars(args)


def get_img(input_path):
    """Open the image file and return img object if successful"""
    im = Image.open(input_path)
    im = ImageOps.exif_transpose(im)
    return im


def resize_img(img):
    """Resize the img and return the resized image"""
    width, height = img.size
    total_pixels = width * height
    print(f"Width is {width}, Height is {height}")
    print(f"Total pixels: {total_pixels}")
    img = img.resize((512, 512), Image.ANTIALIAS)
    return img


def save_img(img, output_path):
    """Save the image, treduce quality and get file size"""
    img.save(output_path, optimize=True, quality=10)


def make_output_path(args):
    """Check output path"""
    input_name = os.path.splitext(args["input"])[0]
    return f"{input_name}-rescaled.png"


def main():
    args = get_args()
    if args["output"]:
        output_path = args["output"]
    else:
        output_path = make_output_path(args)
    init_image = get_img(args["input"])
    resized_img = resize_img(init_image)
    save_img(resized_img, output_path)


if __name__ == "__main__":
    main()
