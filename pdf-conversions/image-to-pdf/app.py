import os

from PIL import Image


def images_to_pdf(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all .png files in the input folder
    # image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".jpg")]
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]

    if not image_files:
        print("No PNG files found in the input folder.")
        return

    for image_file in image_files:
        # Open the image
        img = Image.open(os.path.join(input_folder, image_file))

        # Ensure the image is in RGB mode (PDFs do not support palettes)
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Create the output PDF file name
        output_pdf_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}.pdf")

        # Save the image as a PDF
        img.save(output_pdf_path, "PDF")
        print(f"Converted: {image_file} -> {output_pdf_path}")

if __name__ == "__main__":
    input_folder = "input"  # Specify the input folder
    output_folder = "output"  # Specify the output folder

    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
    else:
        images_to_pdf(input_folder, output_folder)
        print("Done")
