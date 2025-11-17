# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 14:21:38 2025

@author: Thomas S Ball

"""

import numpy as np

def get_areas(
        res: tuple, # Angular resolution
        bounds: dict = {
            "top" : 90,
            "bottom" : -90, 
            "left" : -180,
            "right" : 180
            },
        R: float = 6371.0, # earth radius in km
        ) -> np.array:
    
    R * np.sin(np.deg2rad(res[0]))
    latitudes = np.linspace(bounds["bottom"],
                            bounds["top"], 
                            int(round((bounds["top"] - bounds["bottom"]) / abs(res[1]), 0))
                            )
    verts = R * (np.sin(np.deg2rad(abs(latitudes))) \
                     - np.sin(np.deg2rad(abs(latitudes) - abs(res[1])
                                         )))
    areas = verts * R * np.sin(np.deg2rad(res[0]))
    return areas

def get_pixel_area(res, coords, bounds, R):
    areas = get_areas(res, bounds, R)
    lat, lon = coords
    lat_index = int(round((lat - bounds["bottom"]) / abs(res[1]), 0))
    area = areas[lat_index]
    if R == 6371:
        print(f"{area} km squared at {coords}")
    return area
    
if __name__ == "__main__":
    R = 6371 # km
    res = (0.083333333333333,-0.083333333333333)
    bounds = {"top" : 90,
              "bottom" : -90, 
              "left" : -180,
              "right" : 180
              }
    
    # KNEPP
    # coords = (50.978141, -0.358317)
    coords = (10.720675, -85.013805)
    get_pixel_area(res, coords, bounds, R)