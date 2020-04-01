from xspectre.utils.image import ExistingImage, ArrayImage
# TODO: replace this file with a settings file


def hk_model_reshape(
        original_image_filename, output_filename, image_hdu=1,  x_scale=-1/0.925, y_scale=-1/0.93,
        x_translation=269, y_translation=161, rotation_angle=1
):
    image = ExistingImage(original_image_filename, image_hdu)
    image.scale_and_translate(x_translation, y_translation, x_scale, y_scale, 0)
    image.rotate(rotation_angle)
    ArrayImage(image.image).save(output_filename)


def yj_model_reshape(
        original_image_filename, output_filename, image_hdu=1,  x_scale=-1/0.96, y_scale=-1/0.95,
        x_translation=113, y_translation=-108, rotation_angle=-1.5
):
    image = ExistingImage(original_image_filename, image_hdu)
    image.scale_and_translate(x_translation, y_translation, x_scale, y_scale, 0)
    image.rotate(rotation_angle)
    ArrayImage(image.image).save(output_filename)
