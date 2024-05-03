from PIL import Image
import os


def resize_images(input_dir, output_dir, target_width, target_height):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        output_filepath = os.path.join(output_dir, filename)

        with Image.open(filepath) as img:
            width, height = img.size
            aspect_ratio = width / height

            if width > height:
                new_width = target_width
                new_height = int(target_width / aspect_ratio)
            else:
                new_height = target_height
                new_width = int(target_height * aspect_ratio)

            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_filepath)


if __name__ == "__main__":
    input_dir = "C:\\Users\Tamer\Desktop\emil atanasov chepareta\chernokop"
    output_dir = "C:\\Users\Tamer\Desktop\emil atanasov chepareta\chernokop-resized"

    target_width = 400
    target_height = 600

    resize_images(input_dir, output_dir, target_width, target_height)
