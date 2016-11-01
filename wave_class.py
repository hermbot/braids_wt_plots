import numpy as np
import pylab as plt
import seaborn as sns

RESOURCE_FILE = 'resources.cc'
TARGET_DIR = 'C:\\Users\\mHermes\\Desktop\\test_images\\'
TEAL = (0.094, 0.455, 0.443)
MAGENTA = (0.702, 0.09, 0.282)
X_AXIS = np.arange(129)

# These lists come from digital_oscillator.cc. In the source code they are
# set up to be lists of either 8 or 16 waveforms, in many cases there are
# some values that are repeated to fill out the values. Curiously, table
# 16, Organ, has what might be a typo where the first value is 176
# which is out of order with the rest of the table. I removed it from this
# list. 176 was also at the beginning of digital.

male =          ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'Male')
female =        ([16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 'Female')
choir =         ([32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], 'Choir')
space_voice =   ([48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], 'Space Voice')
tampura =       ([64, 65, 66, 67, 68, 68, 69, 70, 71, 72, 73, 74, 75, 76], 'Tampura')
shamus =        ([77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], 'Shamus')
swept_string =  ([93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
                107, 108], 'Swept String')
bowed =         ([109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                121, 122, 123, 124], 'Bowed')
cello =         ([125, 126, 127, 128, 129, 130, 131, 132], 'Cello')
vibes =         ([133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
                145], 'Vibes')
slap =          ([146, 147, 148, 149, 150, 151, 152, 153], 'Slap')
piano =         ([154, 155, 156], 'Piano')
organ =         ([157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
                169, 170, 171], 'Organ')
waves =         ([172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183,
                184, 185, 186, 187], 'Waves')
digital =       ([188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199,
                200, 201, 202], 'Digital')
drone1 =        ([203, 204, 205, 212, 206, 207, 208, 209, 210, 211, 212], 'Drone 1')
drone2 =        ([213, 214, 215, 216, 217, 218, 219], 'Drone 2')
metallic =      ([220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231,
                232, 233, 234, 235], 'Metallic')
fantasy =       ([236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
                248, 249, 250, 251], 'Fantasy')
bell =          ([252, 253, 254, 255], 'Bell')

class WaveTable(object):
    def __init__(self, table_definition):
        self.table = table_definition[0]
        self.name = table_definition[1]