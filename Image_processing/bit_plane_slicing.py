def bitPlaneSlicing(r, bit_plane):
    """
    Given an image, and the bit level, it extracts that particular bit level.
    
    Arguments:
      r (int): pixel_value (don't worry about it being a single pixel, we will use np.vectorize which will run it for entire image)
                in bitPlaneSlicingVec, we have to pass gray scale image
      bit_plane (int): Which bit plane to extract
                        bit_plane=8, will return the most significant bit plane
                        bit_plane=1, will return the least significant bit plane
    """
    dec = np.binary_repr(r, width = 8)
    return int(dec[8-bit_plane])

bitPlaneSlicingVec = np.vectorize(bitPlaneSlicing)

## Usage 
# highest_bit_plane = bitPlaneSlicingVec(gray_img, 8)
# lowest_bit_plane = bitPlaneSlicingVec(gray_img, 1)
