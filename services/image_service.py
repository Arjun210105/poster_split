from PIL import Image


class ImageService:

    @staticmethod
    def load_image(path):
        return Image.open(path)

    @staticmethod
    def get_image_info(path):

        image = Image.open(path)

        width, height = image.size

        return {
            "image": image,
            "width": width,
            "height": height,
            "aspect_ratio": width / height
        }