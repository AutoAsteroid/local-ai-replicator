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

For the LoRA to understand the context of each of your images during training, it needs a list of correlated tags.
To automatically generate `.txt` caption files for your images, we'll use ComfyUI alongside the popular **WD14 Tagger** custom node.
Because vanilla ComfyUI doesn't come with custom node managers out of the box, we will install **ComfyUI-Manager** first using a simple drag-and-drop method.

### Step 1: Install ComfyUI-Manager

1. Completely close out of  ComfyUI if it is currently running.
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

### Step 2: Install Required Custom Nodes

1. Drag and drop the provided `auto_tagger.json` file it directly into the ComfyUI browser window.
2. You may see red outlined nodes. Click the **Manager** button and **Install Missing Custom Nodes**.
4. ComfyUI Manager will find and list the missing custom nodes, such as `comfyui-wd14-tagger` and `was-ns`.
5. Click **Install All** (or **Install** next to each package).
6. After installion completes, click the red **Restart** button on the bottom left when prompted.

### Step 3: Captioning

1. In the blue node labeled **Folder Path**, paste the absolute path to your dataset. For example: `C:\Users\YourName\Documents\Dataset`. Make sure to not have any quotation marks `"` wrapped around it.
2. In the second blue node labeled **Trigger Word**, put a unique identifier that describes your dataset best. For example, `jordan_car` is better than `car` because the base model can bleed in what it already knows about `car`.
3. Near the top right **Run** button, change the **Queue/Batch Count** to match the exact number of images in your dataset folder.
4. Click **Run**. ComfyUI will generate `.txt` captions for each of your images. If you notice some words you don't like being chosen, you can add them to the `exclude_tags` parameter in `WD14 Tagger`.
5. If you notice your `Load Image Batch` picking up where it last left off rather than starting from your first file, increase the `label` parameter to reset the counter to 0.

> The workflow is set to use **`wd-v1-4-convnextv2-tagger-v2`** by default. The very first time you run the workflow, ComfyUI will automatically download this model from HuggingFace. If you'd prefer a different model, select any in the `WD14 Tagger` model dropdown.

## 4. Cleanup & Quality Control

1. Once ComfyUI finishes running through your queue, your `.txt` caption files will be ready inside ComfyUI's output directory found here:
```text
ComfyUI_windows_portable/
└── ComfyUI/
    └── output/
        └── [TRIGGER_WORD]/
            ├── 001.txt
            ├── 002.txt
            └── ...
```
2. Copy or move all the generated `.txt` files and paste them directly into your main dataset folder alongside your original image files. Every image should now have a corresponding `.txt` file with the exact same name (e.g., `001.png` and `001.txt`).
3. In every text file you should see your trigger word followed by a lot of image descriptors. You can adjust these as you'd like.

## 5. Next Step: **[Training](../02-training/README.md)**
