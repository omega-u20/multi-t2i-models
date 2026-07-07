# AI Image Generator

A command-line interface (CLI) application that generates images from text prompts using the Hugging Face Inference API. It supports multiple state-of-the-art text-to-image models.

## Features

- **Multiple Models Supported**:
  - `flux` (`black-forest-labs/FLUX.1-schnell` via `nscale`)
  - `flux-real` (`XLabs-AI/flux-RealismLora` via `fal-ai`)
  - `krea` (`krea/Krea-2-Turbo` via `fal-ai`)
- **Interactive Interface**: Choose your model, input custom prompts, and set desired dimensions (height and width).
- **Metadata Embedding**: Prompt metadata is automatically saved inside the generated PNG images.
- **Organization**: Images are automatically saved in the `gen/` directory with structured filenames including the date, prompt snippet, selected model, and a random string suffix.

---

## Prerequisites

- **Python 3.8 or higher**
- A **Hugging Face Account** and a **Hugging Face Access Token** (with permissions to run inference).

---

## Setup Instructions

Follow these exact steps to set up and run the project:

### 1. Clone or Open the Project Directory
Ensure you are in the root directory of the project:
```bash
cd path/to/project-directory
```

### 2. Set Up a Virtual Environment (Recommended)
Creating a virtual environment helps keep dependencies isolated:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root of the project (same directory as `main.py`):
```env
HF_TOKEN=your_huggingface_access_token_here
```
> [!IMPORTANT]
> Replace `your_huggingface_access_token_here` with your actual Hugging Face Access Token. Never commit this file or expose your token publicly.

### 5. Create the Output Directory
The application saves generated images to a folder named `gen/`. Ensure it exists:
```bash
mkdir gen
```

---

## How to Run

Launch the application using Python:
```bash
python main.py
```

### Application Flow:
1. Select a model from the list by entering its corresponding number.
2. Enter your text prompt when prompted.
3. Input the dimensions as `height width` separated by a space (e.g., `1024 1024` or `512 768`).
4. The generated image will be saved under the `gen/` directory.
5. Choose whether to perform another round with the same model (`y`), switch models (`Y`), or exit the program (`n`).
