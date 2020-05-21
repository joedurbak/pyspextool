import os

from pandas import to_datetime

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


def lmi_to_rimas(lmi_file, rimas_header, save_dir, bias_image, c_indices=[0, 0]):
    rimas_format = "rimas.{0:04d}.{1}.C{2}.fits"
    lmi_image = ExistingImage(lmi_file)
    lmi_image.image = lmi_image.image[516:516+2048, 516:516+2048] - bias_image
    lmi_header = lmi_image.header.copy()
    rimas_header['OBSMODE'] = 'PHOTO'
    rimas_header['OBJNAME'] = str(lmi_header['OBJNAME'])
    rimas_header['OBJECT'] = str(lmi_header['OBJECT'])
    rimas_header['OBSTYPE'] = str(lmi_header['OBSTYPE'])
    rimas_header['IMAGETYP'] = str(lmi_header['IMAGETYP'])
    rimas_header['OBSERVER'] = str(lmi_header['OBSERVER'])
    rimas_header['OBSAFFIL'] = str(lmi_header['OBSAFFIL'])
    lmi_dt_str = lmi_header['DATE-OBS']
    rimas_header['DATEOBS'] = lmi_dt_to_rimas_dt(lmi_dt_str)
    rimas_header['UTCSTART'] = lmi_t_to_rimas_dt(lmi_header['UTCSTART'], lmi_dt_str)  # TODO: fix datetime format
    rimas_header['UT'] = lmi_t_to_rimas_dt(lmi_header['UT'], lmi_dt_str)  # TODO: setup RIMAS to fill this in
    rimas_header['UTC'] = lmi_t_to_rimas_dt(lmi_header['UT'], lmi_dt_str)  # TODO: setup RIMAS to fill this in
    rimas_header['UTCEND'] = lmi_t_to_rimas_dt(lmi_header['UTCEND'], lmi_dt_str)  # TODO: setup RIMAS to fill this in
    rimas_header['EXPTIME'] = str(lmi_header['EXPTIME'])  # TODO: setup RIMAS to fill this in, also need to check units
    rimas_header['TELRA'] = str(lmi_header['TELRA'])
    rimas_header['TELDEC'] = str(lmi_header['TELDEC'])
    rimas_header['OBSRA'] = str(lmi_header['OBSRA'])
    rimas_header['OBSDEC'] = str(lmi_header['OBSDEC'])
    rimas_header['RA'] = str(lmi_header['RA'])
    rimas_header['DEC'] = str(lmi_header['DEC'])
    rimas_header['RAOFF'] = 'TBD'  # TODO: figure out how to fill this in
    rimas_header['DECOFF'] = 'TBD'  # TODO: figure out how to fill this in
    rimas_header['ST'] = str(lmi_header['ST'])  # TODO: setup RIMAS to fill this in
    rimas_header['AIRMASS'] = str(lmi_header['AIRMASS'])
    rimas_header['FILTER2'] = 'open'  # TODO: encourage ethan to use this for a composite filter for FILTER0 and FILTER1
    rimas_header['SLITWID'] = 'open'  # TODO: encourage ethan to use this for a composite filter for FILTER0 and FILTER1
    rimas_header['CRVAL1'] = str(lmi_header['CRVAL1'])
    rimas_header['CRVAL2'] = str(lmi_header['CRVAL2'])
    rimas_header['TELFOCUS'] = str(lmi_header['TELFOCUS'])
    rimas_header['HA'] = str(lmi_header['HA'])
    rimas_header['ZA'] = str(lmi_header['ZA'])
    rimas_header['PARANGLE'] = str(lmi_header['PARANGLE'])
    rimas_header['INSTCVR'] = str(lmi_header['INSTCVR'])
    rimas_header['TCSHLTH'] = str(lmi_header['TCS_HLTH'])
    rimas_header['ROTANGLE'] = str(lmi_header['ROTANGLE'])
    rimas_header['M1CVR'] = str(lmi_header['M1CVR'])
    rimas_header['TCS_STAT'] = str(lmi_header['TCS_STAT'])
    rimas_header['TELALT'] = str(lmi_header['TELALT'])
    rimas_header['TELAZ'] = str(lmi_header['TELAZ'])
    rimas_header['COMAZDIF'] = str(lmi_header['DOMAZDIF'])  # TODO: fix RIMAS instrument header typo
    rimas_header['DOMOCCUL'] = str(lmi_header['DOMOCCUL'])
    rimas_header['GUIMODE'] = str(lmi_header['GUIMODE'])
    rimas_header['IPA'] = str(lmi_header['IPA'])
    rimas_header['PRESSURE'] = str(lmi_header['PRESSURE'])
    rimas_header['TEMPAMB'] = str(lmi_header['TEMPAMB'])
    rimas_header['TEMPDEW'] = str(lmi_header['TEMPDEW'])
    rimas_header['HUMIDITY'] = str(lmi_header['HUMIDITY'])
    rimas_header['WINDDIR'] = str(lmi_header['WINDDIR'])
    rimas_header['WINDVEL'] = str(lmi_header['WINDVEL'])
    rimas_header['OBSALT'] = str(lmi_header['OBSALT'])
    rimas_header['CD1_1'] = str(lmi_header['CD1_1'])
    rimas_header['CD2_2'] = str(lmi_header['CD2_2'])
    rimas_header['CD1_2'] = str(lmi_header['CD1_2'])
    rimas_header['CD2_1'] = str(lmi_header['CD2_1'])
    # GAIN
    rimas_header['CRPIX1'] = str(1024)
    rimas_header['CRPIX2'] = str(1024)
    rimas_header['RDNOISE'] = str(lmi_header['RDNOISE'])
    rimas_header['SATURATE'] = str(65000)  # TODO: Figure out the correct number for RIMAS

    lmi_filter = str(lmi_header['FILTER1'])
    if lmi_filter.strip() == 'SDSS-G':
        rimas_header['FILTER0'] = 'Y'
        rimas_header['FILTER1'] = 'H'
        rimas_header['CAMERA'] = '0'
        rimas_header['DETECTOR'] = 'C0'
        i = c_indices[0]
        rimas_format = rimas_format.format(i, 'YJ', 0)
        c_indices[0] += 1
    elif lmi_filter.strip() == 'SDSS-R':
        rimas_header['FILTER0'] = 'J'
        rimas_header['FILTER1'] = 'K'
        rimas_header['CAMERA'] = '0'
        rimas_header['DETECTOR'] = 'C0'
        i = c_indices[0]
        rimas_format = rimas_format.format(i, 'YJ', 0)
        c_indices[0] += 1
    elif lmi_filter.strip() == 'SDSS-I':
        rimas_header['FILTER0'] = 'Y'
        rimas_header['FILTER1'] = 'H'
        rimas_header['CAMERA'] = '1'
        rimas_header['DETECTOR'] = 'C1'
        i = c_indices[1]
        rimas_format = rimas_format.format(i, 'HK', 1)
        c_indices[1] += 1
    elif lmi_filter.strip() == 'SDSS-Z':
        rimas_header['FILTER0'] = 'J'
        rimas_header['FILTER1'] = 'K'
        rimas_header['CAMERA'] = '1'
        rimas_header['DETECTOR'] = 'C1'
        i = c_indices[1]
        rimas_format = rimas_format.format(i, 'HK', 1)
        c_indices[1] += 1

    else:
        return c_indices

    lmi_image.header = rimas_header
    print(rimas_format)
    lmi_image.save(os.path.join(save_dir, rimas_format))

    return c_indices


def lmi_dt_to_rimas_dt(lmi_dt):
    dt = to_datetime(lmi_dt)
    rimas_dt = dt.strftime("%Y%m%d-%H%M%S%f")
    rimas_dt = rimas_dt[:len(rimas_dt)-3]
    return rimas_dt


def lmi_t_to_rimas_dt(lmi_t, lmi_dt):
    dt_str = "".join((lmi_dt[0:11], lmi_t))
    return lmi_dt_to_rimas_dt(dt_str)


if __name__ == '__main__':
    lmi_dir = r'G:\My Drive\Shared LMI data\DCT Run 200228b\DCT Run 200228b'
    lmi_dir_ls = [os.path.join(lmi_dir, name) for name in os.listdir(lmi_dir) if name.endswith('.fits')]
    lmi_dir_ls.sort()
    c_indices = [0, 0]
    out_dir = r'G:\My Drive\RIMAS Photometry Data\converted_lmi'
    bias = ExistingImage(lmi_dir_ls[57]).image[516:516+2048, 516:516+2048]
    input_header = ExistingImage(r'G:\My Drive\RIMAS spectra\spectra_upload_2019_10_18\20191018T144058C0-Char_run_YH_Thermal_1.1V\20191018T144058C0-0007.fits').header.copy()
    for image_file in lmi_dir_ls:
        c_indices = lmi_to_rimas(image_file, input_header, out_dir, bias, c_indices)
