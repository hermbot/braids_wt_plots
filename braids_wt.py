'''
Wavetables

- 33 waveforms distributed over 20 wavetables, with quantized wavetable selector, and smooth interpolation
within a wavetable.

WTBL

WTBL is a classic implementation of wavetable synthesis. TIMBRE sweeps the
wavetable, and COLOR selects one of the 20 wavetables to play with. The
waveforms are interpolated when traveling through a wavetable, but not when
switching from one table to another.

'''


import numpy as np
import pylab as plt
import seaborn as sns

RESOURCE_FILE = 'resources.cc'
TARGET_DIR = 'C:\\Users\\mHermes\\Desktop\\Lunch\\braids_wt\\Images'
TEAL = [24, 116, 113]
MAGENTA = [179, 23, 72]
X = np.arange(129)


# These lists come from digital_oscillator.cc. In the source code they are
# set up to be lists of either 8 or 16 waveforms, in many cases there are
# some values that are repeated to fill out the values. Curiously, table
# 16, Organ, has what might be a typo where the first value is 176
# which is out of order with the rest of the table. I removed it from this
# list. 176 was also at the beginning of digital.

male =          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
female =        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
choir =         [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
space_voice =   [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
tampura =       [64, 65, 66, 67, 68, 68, 69, 70, 71, 72, 73, 74, 75, 76]
shamus =        [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]
swept_string =  [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
                107, 108]
bowed =         [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                121, 122, 123, 124]
cello =         [125, 126, 127, 128, 129, 130, 131, 132]
vibes =         [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
                145]
slap =          [146, 147, 148, 149, 150, 151, 152, 153]
piano =         [154, 155, 156]
organ =         [157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
                169, 170, 171]
waves =         [172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183,
                184, 185, 186, 187]
digital =       [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199,
                200, 201, 202]
drone1 =        [203, 204, 205, 212, 206, 207, 208, 209, 210, 211, 212]
drone2 =        [213, 214, 215, 216, 217, 218, 219]
metallic =      [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231,
                232, 233, 234, 235]
fantasy =       [236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
                248, 249, 250, 251]
bell =          [252, 253, 254, 255]

all_waves = {'Male': male, 'Female': female, 'Choir': choir, 'Space Voice':
            space_voice, 'Tampura': tampura, 'Shamus': shamus, 'Swept String':
            swept_string, 'Bowed': bowed, 'Cello': cello, 'Vibes': vibes,
            'Slap': slap, 'Piano': piano, 'Organ': organ, 'Waves': waves,
            'Digital': digital, 'Drone 1': drone1, 'Drone 2': drone2,
            'Metallic': metallic, 'Fantasy': fantasy, 'Bell': bell}

def read_values(file_name, var_name):
    """Opens a source code file and returns the block of text between the
    declaration of a variable and the closing brace. Used for grabbing
    wavetable data and indices from Braids source code. Requires knowledge
    of variable names beforehand.

    "If" statments are set up such that the declaration line and the
    closing brace line are omitted and the routine will stop when
    successful rather than continuing to read to the end of the file.
    """
    append_flag = False
    text_lines = ""

    searchfile = open(file_name, "r")
    for line in searchfile:
        if var_name in line:
            append_flag = True
        if append_flag and ('}' in line):
            break
        if append_flag and (var_name not in line):
            text_lines += line

    searchfile.close()
    return text_lines


def clean(data):
    """Remove all newline characters and spaces and convert to numpy array."""
    data = ''.join(data.split())
    array_form = np.fromstring(data, dtype=np.int16, sep=',')
    return array_form


def get_wave(address, table, no_samples=129):
    # no_samples is set to 129 as a default for Braids wavetables.
    start = address * no_samples
    return table[start:start + no_samples]


def crossfade(wave1, wave2, pct_wave1):
    """Returns a wave between the two arguments based on value of pct_wave1.
    pct_wave1 needs to be a decimal value between 0 and 0.99.
    """
    return (wave1 * pct_wave1) + (wave2 * (1 - pct_wave1))


def create_images(image_list, target_dir):
    pass


wt_waves = clean(read_values(RESOURCE_FILE, 'wt_waves'))
# wt_code = clean(read_values(RESOURCE_FILE, 'wt_code'))
# wt_map = clean(read_values(RESOURCE_FILE, 'wt_map'))

def old_main():
    a = get_wave(237, wt_waves)
    b = get_wave(238, wt_waves)

    a1 = (a * 0.8) + (b * 0.2)
    a2 = (a * 0.6) + (b * 0.4)
    a4 = (a * 0.4) + (b * 0.6)
    a5 = (a * 0.2) + (b * 0.8)
    plt.plot(X, a)
    plt.plot(X, a1)
    plt.plot(X, a2)
    plt.plot(X, a4)
    plt.plot(X, a5)
    plt.plot(X, b)
    plt.show()


def main():
    for i in waves:
        plt.plot(X, get_wave(i, wt_waves))

    plt.show()

if __name__ == '__main__':
    main()




'''data = np.genfromtxt(data_file, delimiter=',')
print(data.size)

wave_samples = 128
number_of_waves = np.arange(129)
wave_index = number_of_waves * wave_samples


for i in range(1, 2):
    plt.axis('off')
    plt.title(i)
    plt.plot(data[wave_index[i]:wave_index[i] + 255])
    plt.show()'''