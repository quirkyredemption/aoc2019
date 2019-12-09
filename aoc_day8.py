from operator import attrgetter
import numpy as np

class ImageLayer():
    def __init__(self, data):
        self.layer_data = data
        self.zeros = self.count_zero()
        self.output = self.layer_output()
    
    def count_zero(self):
        return self.layer_data.count(0)

    def layer_output(self):
        return self.layer_data.count(1) * self.layer_data.count(2)

def pixel_in_image(width, height):
    return width*height

def generate_layers(_input, pixels):
    layers = []
    image = [int(x) for x in str(_input)]
    layer_start = 0

    for idx in range(len(image) + 1):
        if idx % pixels == 0 and idx != 0:
            layers.append(ImageLayer(image[layer_start:idx]))
            layer_start = idx
    
    return layers

def check_corruption(_input, width, height):
    pixels = pixel_in_image(width, height)
    layers = generate_layers(_input, pixels)
    
    layer_least_zeros = min(layers, key=attrgetter("zeros"))

    return layer_least_zeros.output

def decode_pixel(pixel_layer):
    for i in range(len(pixel_layer)):
        if pixel_layer[i] == 0 or pixel_layer[i] == 1:
            return pixel_layer[i]

def decode_image(_input, width, height):
    pixels = pixel_in_image(width,height)
    layers = generate_layers(_input, pixels)
    layers_data = np.array([layer.layer_data for layer in layers])
    layer_pixels = layers_data.transpose()
    decoded_pixels = np.array([decode_pixel(layer_pixel) for layer_pixel in layer_pixels])
    decoded_pixels = decoded_pixels.reshape(height, width)
    return decoded_pixels

if __name__ == "__main__":
    input_file = open("input_day8.txt", "r").read()
    part1 = check_corruption(input_file, 25, 6)
    print(part1)
    part2 = decode_image(input_file, 25, 6)
    print(part2)
