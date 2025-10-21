# Quick Start Guide

This guide will help you get started with DeepSeek-OCR inference in minutes.

## Choose Your Method

### Method 1: Google Colab (Easiest - No Setup Required)

1. Click here: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/azman0101/DeepSeek-OCR-Inference/blob/main/DeepSeek_OCR_Colab.ipynb)

2. Change runtime to GPU:
   - Click `Runtime` → `Change runtime type`
   - Select `T4 GPU` or better
   - Click `Save`

3. Run all cells in order (Runtime → Run all)

4. Upload your image when prompted

5. View your OCR results!

**Pros:** 
- No installation needed
- Free GPU access
- Works immediately

**Cons:**
- Requires internet connection
- Session timeout after inactivity

---

### Method 2: Local Installation

#### Prerequisites
- Python 3.8+
- 10GB+ free disk space
- (Optional) NVIDIA GPU with CUDA support

#### Quick Install

```bash
# Clone the repository
git clone https://github.com/azman0101/DeepSeek-OCR-Inference.git
cd DeepSeek-OCR-Inference

# Install dependencies
pip install -r requirements.txt
```

#### Basic Usage

**Command Line:**
```bash
python inference.py --image your_image.jpg --output output_dir
```

**Python Script:**
```python
from inference import DeepSeekOCRInference

# Initialize
ocr = DeepSeekOCRInference()

# Process image
result = ocr.infer("your_image.jpg", "output_dir")
print(result)
```

---

### Method 3: GitHub Models (Future)

Coming soon! GitHub Models integration will allow you to use the model through GitHub's infrastructure.

---

## What You Can Do

✅ Extract text from images  
✅ Understand document layouts  
✅ Process multiple images in batch  
✅ Save results in various formats  

## Supported Image Formats

- JPG/JPEG
- PNG
- BMP
- TIFF
- And more...

## Tips for Best Results

1. **Use high-resolution images** - Better quality = better results
2. **Ensure good lighting** - Clear, well-lit images work best
3. **GPU recommended** - 10-100x faster than CPU
4. **Batch process** - More efficient for multiple images

## Getting Help

- 📖 [Full Documentation](README.md)
- 💻 [View Code](https://github.com/azman0101/DeepSeek-OCR-Inference)
- 🐛 [Report Issues](https://github.com/azman0101/DeepSeek-OCR-Inference/issues)
- 🤗 [Model Page](https://huggingface.co/deepseek-ai/DeepSeek-OCR)

---

**Ready to start?** Choose Method 1 (Google Colab) for the fastest way to try it out!
