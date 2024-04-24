from PIL import Image
import os


def convert_images_format(input_dir: str, output_dir: str, convert_to: str) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    for filename in files:
        with Image.open(os.path.join(input_dir, filename)) as img:
            output_filename = os.path.splitext(filename)[0] + f".{convert_to}"
            output_path = os.path.join(output_dir, output_filename)

            img.save(output_path, convert_to.upper())


if __name__ == "__main__":
    input_directory = "C:\\Users\Tamer\Desktop\emil atanasov chepareta\karagioz"
    output_directory = "C:\\Users\Tamer\Desktop\emil atanasov chepareta\karagioz-webp"

    convert_images_format(input_directory, output_directory, "webp")