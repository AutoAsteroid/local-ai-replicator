# This helper script helps prepare a dataset by:
#
# - Finding duplicate images and purging lower-quality versions 
# - Sequentially renaming images into a separate output folder

import argparse
import os
import shutil
import sys
from PIL import Image, ImageOps
import imagehash

SIMILARITY_THRESHOLD = 6                # Hamming distance: 0 = exact match, 1-6 = near duplicates
HASH_FUNC = imagehash.phash             # Perceptual hash algorithm
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff')

# Command line argument parsing if run without interactive prompts
def parse_args():
    parser = argparse.ArgumentParser(
        description="Find duplicates, purge lower-quality versions, and sequentially rename images into a separate output folder."
    )
    parser.add_argument(
        "-i", "--input",
        dest="image_dir",
        default=None,
        help="Path to the input dataset directory"
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_dir",
        default=None,
        help="Path to the separate output directory"
    )
    parser.add_argument(
        "-t", "--threshold",
        type=int,
        default=SIMILARITY_THRESHOLD,
        help=f"Similarity threshold for duplicates (default: {SIMILARITY_THRESHOLD})"
    )
    return parser.parse_args()

# Helper function to extract image information from our dataset
def get_image_info(filepath):
    """Returns image dimensions, file size, and perceptual hash."""
    try:
        file_size = os.path.getsize(filepath)
        with Image.open(filepath) as img:
            img_exif = ImageOps.exif_transpose(img)
            w, h = img_exif.size
            pixel_count = w * h
            h_val = HASH_FUNC(img_exif)
            return {
                'path': filepath,
                'hash': h_val,
                'pixels': pixel_count,
                'size': file_size,
                'dimensions': f"{w}x{h}"
            }
    except Exception as e:
        print(f"Skipping unreadable image {filepath}: {e}")
        return None

# Function to walk through and scan a directory to gather image metadata
def scan_directory(directory):
    """Recursively scans folder and gathers image metadata and perceptual hashes."""
    images_data = []
    print(f"Scanning '{directory}' recursively for images...")
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                filepath = os.path.join(root, file)
                info = get_image_info(filepath)
                if info:
                    images_data.append(info)
                    
    return images_data

# Function to group near-duplicate images based on perceptual hash distance
def group_duplicates(images_data, threshold=SIMILARITY_THRESHOLD):
    """Groups near-duplicate images based on hash distance."""
    visited = set()
    duplicate_groups = []
    unique_images = []

    for i in range(len(images_data)):
        img_a = images_data[i]
        if img_a['path'] in visited:
            continue

        group = [img_a]

        for j in range(i + 1, len(images_data)):
            img_b = images_data[j]
            if img_b['path'] in visited:
                continue

            distance = img_a['hash'] - img_b['hash']
            if distance <= threshold:
                group.append(img_b)
                visited.add(img_b['path'])

        visited.add(img_a['path'])

        if len(group) > 1:
            duplicate_groups.append(group)
        else:
            unique_images.append(img_a)

    return duplicate_groups, unique_images

# Helper function to greedily select the "best" image from any given group of duplicates
def select_best_image(group):
    """Sorts group by pixel count (descending), then file size (descending)."""
    sorted_group = sorted(group, key=lambda x: (x['pixels'], x['size']), reverse=True)
    return sorted_group[0], sorted_group[1:]


# Prepare the dataset by scanning, deduplicating, and renaming images into a separate output folder
def main():
    args = parse_args()
    image_dir = args.image_dir
    output_dir = args.output_dir

    # Handle interactive prompts if command line arguments were not provided
    if not image_dir:
        image_dir = input("Enter the input dataset folder path: ").strip().strip('"').strip("'")

    while not output_dir or os.path.abspath(output_dir) == os.path.abspath(image_dir):
        output_dir = input("Enter a different output folder path: ").strip().strip('"').strip("'")

    if not os.path.exists(image_dir):
        print(f"Error: Input directory '{image_dir}' does not exist.")
        sys.exit(1)

    # Scan the input directory for images and gather metadata
    images_data = scan_directory(image_dir)
    if not images_data:
        print("No valid images found in the specified directory or subfolders.")
        sys.exit(0)

    print(f"Successfully processed {len(images_data)} total images.")

    # Group duplicates and identify unique images based on perceptual hash similarity
    duplicate_groups, unique_images = group_duplicates(images_data, threshold=args.threshold)

    to_keep = []
    purged_count = 0

    for img in unique_images:
        to_keep.append(img)

    # Handle duplicate groups by selecting the best image and purging lower-quality versions
    if duplicate_groups:
        print(f"Successfully found {len(duplicate_groups)} duplicate image groups.")

        for idx, group in enumerate(duplicate_groups, 1):
            best, duplicates = select_best_image(group)
            to_keep.append(best)
            purged_count += len(duplicates)

            print(f"\nGroup {idx} of {len(duplicate_groups)}")
            print(f"   KEEP:    {os.path.basename(best['path'])} ({best['dimensions']}, {best['size'] / 1024:.1f} KB)")
            for dup in duplicates:
                print(f"   DISCARD: {os.path.basename(dup['path'])} ({dup['dimensions']}, {dup['size'] / 1024:.1f} KB)")

    # Sort the final list of images to keep by modification date for sequential renaming
    to_keep.sort(key=lambda x: os.path.getmtime(x['path']))
    os.makedirs(output_dir, exist_ok=True)

    print(f"\nKeeping {len(to_keep)} images and purging {purged_count} duplicates.")

    for index, img in enumerate(to_keep, start=1):
        ext = os.path.splitext(img['path'])[1]
        new_image_name = f"{index:03d}{ext}"
        dest_path = os.path.join(output_dir, new_image_name)

        # Make sure we don't overwrite any existing files in the output directory
        counter = 1
        base_name, file_ext = os.path.splitext(new_image_name)
        while os.path.exists(dest_path):
            dest_path = os.path.join(output_dir, f"{base_name}_{counter}{file_ext}")
            counter += 1

        shutil.copy2(img['path'], dest_path)

    print(f"Successfully processed and renamed dataset at: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    main()
    