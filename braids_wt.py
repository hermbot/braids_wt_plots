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
import os

RESOURCE_FILE = 'resources.cc'
TARGET_DIR = 'C:\\Users\\mHermes\\Desktop\\test_images\\'
X_AXIS = np.arange(129)

# The closest I could get to "the" MI colors
TEAL = ((58 / 255), (158 / 255), (163 / 255))
MAGENTA = ((210 / 255), (64 / 255), (99 / 255))

# These lists come from digital_oscillator.cc. In the source code they are
# set up to be lists of either 8 or 16 waveforms. In many cases there are
# some values that are repeated to fill out the values. I have removed duplicates.
# "Organ" and "Digital" both start with sine waves that are repeated from "Waves".

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


wave_list = [male, female, choir, space_voice, tampura, shamus, swept_string, bowed, cello,
            vibes, slap, piano, organ, waves, digital, drone1, drone2, metallic, fantasy, bell]

wave_names = ['Male', 'Female', 'Choir', 'Space Voice', 'Tampura', 'Shamus', 'Swept String',
             'Bowed', 'Cello', 'Vibes', 'Slap', 'Piano', 'Organ', 'Waves', 'Digital', 'Drone 1',
             'Drone 2', 'Metallic', 'Fantasy', 'Bell']


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
    return np.fromstring(data, dtype=np.int16, sep=',')


#TODO move this somewhere more appropriate
wt_waves = clean(read_values(RESOURCE_FILE, 'wt_waves'))

def get_wave(address, table, no_samples=129):
    start = address * no_samples
    return table[start:start + no_samples]


def crossfade(wave1, wave2, pct_wave1):
    """pct_wave1 needs to be a decimal value between 0 and 0.99."""
    return (wave1 * pct_wave1) + (wave2 * (1 - pct_wave1))


def plot_waves_overlay(wave_set):
    """Overlays each wave in a set."""
    for i in wave_set:
        plt.plot(X_AXIS, get_wave(i, wt_waves))

    f = plt.gca()
    f.axes.get_xaxis().set_visible(False)
    f.axes.get_yaxis().set_visible(False)
    plt.title('Waves')
    plt.xlim(0, 129)
    plt.ylim(0, 256)
    plt.savefig('overlay.png')
    plt.show()


def plot_allwaves(wave_set):
    """Plots each wave in an individual file."""
    suffix = 0
    for i in wave_set:
        plt.plot(X_AXIS, get_wave(i, wt_waves))
        f = plt.gca()
        f.axes.get_xaxis().set_visible(False)
        f.axes.get_yaxis().set_visible(False)
        plt.title('Waves')
        plt.xlim(0, 129)
        plt.ylim(0, 256)
        plt.savefig(TARGET_DIR + 'overlay' + str(suffix) + '.png')
        plt.close()
        suffix += 1


def plot_interp_waves(wave_set, subdivisions):
    """Plots each wave in an individual file.

    This is one of the functions you would call in main() to create
    output. repeats is the number of times to repeat the frames of
    animation for each of the "base" waves. subdivisions is the
    number of frames to create between each base wave.

    """
    suffix = 0
    crossfade_amount = np.linspace(1, 0, subdivisions)
    repeats = 5

    for i in wave_set:
        wave_to_plot = get_wave(i, wt_waves)

        # Here we add extra frames for the animation at each defined wave shape
        for j in range(0, repeats + 1):
            single_plot(wave_to_plot, suffix)
            suffix += 1

        # These are the cross-faded wave shapes
        for k in crossfade_amount:
            single_plot(crossfade(get_wave(i, wt_waves), get_wave(i + 1, wt_waves), k), suffix)
            suffix += 1


def animate_all_waves():
    """Creates subdirectories for all waves and animates them."""
    for i in range(1, len(wave_list) + 1):
        wave_to_plot = wave_list[i]
        wave_name = wave_names[i]


def single_plot(series1, suffix):
    plt.plot(X_AXIS, series1, color=TEAL)
    f = plt.gca()
    f.axes.get_xaxis().set_visible(False)
    f.axes.get_yaxis().set_visible(False)
    plt.xlim(0, 129)
    plt.ylim(0, 256)
    plt.title('Cello', fontsize=16, fontname='Consolas')
    plt.savefig(TARGET_DIR + 'overlay' + str(suffix) + '.png')
    plt.close()


def main():
    plot_interp_waves(piano, 20)


if __name__ == '__main__':
    main()
