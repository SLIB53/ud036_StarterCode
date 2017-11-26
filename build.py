"""
Project build script.

Generates files in 'build' folder.
"""

__author__ = "Akil Krishnan"

import os
import shutil
import data.entertainment_center
import lib.fresh_tomatoes


# Build target directories

BUILD_DIR_NAME = "build"
RESOURCES_DIR_NAME = "resources"
IMAGES_DIR_NAME = "images"

BUILD_DIR_PATH = BUILD_DIR_NAME
RESOURCES_DIR_PATH = "/".join([BUILD_DIR_NAME, RESOURCES_DIR_NAME])
IMAGES_DIR_PATH = "/".join([BUILD_DIR_NAME, RESOURCES_DIR_NAME, IMAGES_DIR_NAME])


def main():
    """
    Generates HTML files, and outputs to build folder. Existing build files
    and folder are overwritten.
    """

    # Init build folder

    print("Checking 'build' directory...")

    if not os.path.isdir(BUILD_DIR_PATH):
        os.mkdir(BUILD_DIR_PATH)

    # Build resources

    print("Checking resources directory...")

    if os.path.isdir(RESOURCES_DIR_PATH):
        print("Resources directory exists. Performing cleanup.")
        shutil.rmtree(RESOURCES_DIR_PATH, ignore_errors=True)

    print("Building resources...")

    shutil.copytree("resources/images", IMAGES_DIR_PATH)

    # Build static page

    print("Building static page...")

    os.chdir(BUILD_DIR_PATH)
    lib.fresh_tomatoes.open_movies_page(data.entertainment_center.MOVIES)

    print("Build complete!")


if __name__ == "__main__":
    main()
