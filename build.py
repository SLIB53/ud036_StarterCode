"""
Project build script.

Generates files in 'build' folder.
"""

__author__ = "Akil Krishnan"

import os
import lib.fresh_tomatoes
import data.entertainment_center

def main():
    """
    Generates HTML files, and outputs to build folder. Existing build files
    and folder are overwritten.
    """
    try:
        os.mkdir("build")
    finally:
        os.chdir("build")
        lib.fresh_tomatoes.open_movies_page(data.entertainment_center.MOVIES)

if __name__ == "__main__":
    main()
