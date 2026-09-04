from PIL import Image, ImageOps


def prepare_photo(source_path, destination_path):
    with Image.open(source_path) as image:
        image = ImageOps.exif_transpose(image)
        image = image.convert('RGB')

        image.thumbnail(
            (1280, 800),
            Image.Resampling.LANCZOS,
        )

        image.save(
            destination_path,
            'JPEG',
            quality=88,
            optimize=True,
        )