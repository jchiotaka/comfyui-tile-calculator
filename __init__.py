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
                "zoom": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 8.0,
                    "step": 0.1,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT")
    RETURN_NAMES = ("image", "tile_width", "tile_height")
    FUNCTION = "calculate"
    CATEGORY = "image/utils"

    def calculate(self, image, tiles_per_width, tiles_per_height, zoom):
        # Image tensor shape: [B, H, W, C]
        _, height, width, _ = image.shape
        
        tile_width = math.ceil((width * zoom) / tiles_per_width)
        tile_height = math.ceil((height * zoom) / tiles_per_height)
        
        return (image, tile_width, tile_height)


NODE_CLASS_MAPPINGS = {
    "TileCalculator": TileCalculator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TileCalculator": "Tile Calculator"
}
