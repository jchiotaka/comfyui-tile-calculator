import math

class TileCalculator:
    """
    Calculates tile dimensions based on image size, magnification, and tile count.
    Passes through the original image unchanged.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "tiles_per_width": ("INT", {
                    "default": 2,
                    "min": 1,
                    "max": 16,
                    "step": 1,
                    "display": "number"
                }),
                "tiles_per_height": ("INT", {
                    "default": 2,
                    "min": 1,
                    "max": 16,
                    "step": 1,
                    "display": "number"
                }),
                "upscale": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 8.0,
                    "step": 0.1,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT", "FLOAT")
    RETURN_NAMES = ("image", "tile_width", "tile_height", "upscale")
    FUNCTION = "calculate"
    CATEGORY = "image/utils"
    OUTPUT_NODE = True

    def calculate(self, image, tiles_per_width, tiles_per_height, upscale):
        _, height, width, _ = image.shape

        tile_width = math.ceil((width * upscale) / tiles_per_width)
        tile_height = math.ceil((height * upscale) / tiles_per_height)

        return {
            "ui": {"text": [f"Tile: {tile_width} x {tile_height}"]},
            "result": (image, tile_width, tile_height, upscale)
        }


NODE_CLASS_MAPPINGS = {
    "TileCalculator": TileCalculator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TileCalculator": "Tile Calculator"
}
