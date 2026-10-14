# Step 01: Dataset Curation & Preprocessing

Before training a high-quality SDXL LoRA, the most critical factor is the quality and consistency of your image dataset. Garbage in means garbage out. Spending a few minutes cleaning your images here will save you hours of troubleshooting later.

---

## 1. What Makes a Good Dataset?

- **Strict Subject Focus:** Every image should feature your specific subject clearly. Avoid crowded backgrounds, multiple competing people, or busy environments that confuse the model during training.
- **Diverse Angles and Lighting:** Include a healthy mix of close-up portraits, medium shots, different facial expressions, and varied natural or studio lighting. This prevents the model from hard-coding a single lighting condition or pose.
- **Avoid Heavy Filters:** Stay away from heavily compressed images, severe JPEGs artifacts, extreme social media filters, or heavy watermarks, as these artifacts will bleed into your generated output.
- **Resolution Matters:** Aim for clean, high-resolution source images (at least 1024x1024 pixels is ideal for SDXL). Don't worry if your raw photos are different sizes or scattered across messy subfolders.

---

## 2. Cleanup & Renaming (`preprocess.py`)

Instead of manually sorting, deleting duplicates, and renaming files, you should use the automated `preprocess.py` script. 
It will recursively crawl your input folder for images, find the highest resolution of identical photos, and sequentially rename them into your provided output directory.

1. Download and double click **`preprocess.py`**. A command window will open.
2. When prompted, drag and drop or type out your image folder path directly into the window and press Enter.
3. Do this again for a new, empty folder where you want your cleaned dataset saved.
4. The script will automatically process your photos getting us closer to ready for training!

You can also run the script directly in terminal.
The `-t` or `--threshold` setting controls how strict the duplicate checker is. 6 catches near-visual duplicates and burst shots while 0 catches exact file-hash duplicates.

```text
python preprocess.py -i "C:\input_path" -o "C:\output_path" -t 6
```

## 3. Setting Up the Auto-Tagger in ComfyUI

For the LoRA to understand the context of each of your images during training, it needs a description of tags, otherwise known as a caption.
To automatically generate `.txt` caption files for your images, we'll use ComfyUI alongside the popular **WD14 Tagger** custom node.
Because vanilla ComfyUI doesn't come with custom node managers out of the box, we will install **ComfyUI-Manager** first using a simple drag-and-drop method.

### Step 1: Install ComfyUI-Manager

1. Completely close ComfyUI if it is currently running.
2. Go to the official [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) GitHub Repository.
3. Click the green **`<> Code`** button at the top right, then select **Download ZIP**.
4. Extract the downloaded ZIP file. You will get a folder named `ComfyUI-Manager-main`.
5. Rename that extracted folder so it is strictly named: `ComfyUI-Manager`
6. Move that folder directly into your ComfyUI custom nodes directory, located here:
```text
ComfyUI_windows_portable/
└── ComfyUI/
    └── custom_nodes/
        └── ComfyUI-Manager/
```
7. Launch ComfyUI. You will now see a new **Manager** button on your floating menu panel!

### Step 2: Install the WD14 Tagger Node

1. Open ComfyUI and click the blue **Manager** button on the top right-hand menu.
2. Click on **Custom Nodes Manager** (or *Install via Manager*).
3. Type `WD14` into the search bar.
4. Locate **ComfyUI-WD14-Tagger** and click **Install**.
5. After installing, click the Red **Restart** button on the bottom left when prompted.
