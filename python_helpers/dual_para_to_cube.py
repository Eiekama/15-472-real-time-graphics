import numpy as np
from PIL import Image
import imageio

def hdr_to_rgba_exponent(hdr_path, exposure=1.0):
    """
    Convert Radiance HDR (.hdr) to PNG with alpha=exponent.
    
    Args:
        hdr_path: Input .hdr file
        png_path: Output .png file  
        exposure: Tone map multiplier
    """
    # Load HDR as float32 radiance (linear)
    hdr = imageio.imread(hdr_path).astype(np.float32)
    
    # Clamp and expose
    hdr = np.clip(hdr * exposure, 0, np.inf)
    
    # Convert to RGBE: mantissa * 2^(exponent+128)
    # Find max channel per pixel for shared exponent
    max_rgb = np.max(hdr, axis=2, keepdims=True) + 1e-6  # Avoid div0
    
    # Exponent: log2(max) → 8-bit shared
    exponent = np.floor(np.log2(max_rgb)) + 128
    exponent = np.clip(exponent, 0, 255).astype(np.uint8)
    
    # Mantissa: RGB / 2^(exponent-128)
    mantissa = hdr / (np.exp2(exponent.astype(np.float32) - 128) + 1e-6)
    mantissa = np.clip(mantissa * 256, 0, 255).astype(np.uint8)
    
    # Pack RGBA: RGB=mantissa, A=exponent
    rgba = np.concatenate([mantissa, exponent], axis=2)
    return rgba

def convert_to_cubemap(img):
    sz = img.shape[0] // 2
    half_sz = sz // 2

    front = img[half_sz:3*half_sz, half_sz:3*half_sz]
    back = img[half_sz:3*half_sz, -3*half_sz:-half_sz]
    left = np.concatenate((img[half_sz:3*half_sz, -half_sz:], img[half_sz:3*half_sz, 0:half_sz]), axis=1)
    right = img[half_sz:3*half_sz, 3*half_sz:5*half_sz]
    top = np.concatenate((img[0:half_sz, 2*sz:4*sz][::-1, ::-1], img[0:half_sz, 0:2*sz]), axis=0)
    top = np.array(Image.fromarray(top).resize((sz, sz)))
    bottom = np.concatenate((img[-half_sz:, 0:2*sz], img[-half_sz:, 2*sz:4*sz][::-1, ::-1]), axis=0)
    bottom = np.array(Image.fromarray(bottom).resize((sz, sz)))

    cubemap = np.concatenate((front, back, left, right, top, bottom), axis=0)
    return cubemap


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert a dual-paraboloid map to a cubemap.")
    parser.add_argument("input", help="Path to the input dual-paraboloid map")
    parser.add_argument("--output", default=None, help="Path to the output cubemap")
    args = parser.parse_args()

    img = hdr_to_rgba_exponent(args.input, 0.5)
    cubemap = convert_to_cubemap(img)
    
    if args.output is None:
        args.output = args.input.replace(".hdr", "-cube.png")

    Image.fromarray(cubemap).save(args.output)