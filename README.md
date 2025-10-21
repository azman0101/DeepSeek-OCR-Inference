# DeepSeek-OCR Inference

A comprehensive implementation for running inference with [DeepSeek-OCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR), a state-of-the-art vision-language model for optical character recognition and document understanding.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/azman0101/DeepSeek-OCR-Inference/blob/main/DeepSeek_OCR_Colab.ipynb)

## Features

- 🚀 **Easy-to-use inference scripts** for DeepSeek-OCR
- 📓 **Google Colab notebook** for quick experimentation
- 🎯 **Single and batch processing** support
- 🔧 **Flexible device management** (CPU/GPU)
- 📦 **Minimal dependencies** with clear setup instructions

## Model Overview

DeepSeek-OCR is a sophisticated vision-language model designed for:
- Optical Character Recognition (OCR)
- Document understanding and layout analysis
- Multi-scale feature extraction
- Adaptive resolution processing

The model utilizes dual vision encoders (SAM ViT-B and CLIP-L) with the innovative "Contexts Optical Compression" approach for efficient processing.

## Quick Start

**⚡ New to this?** Check out our [Quick Start Guide](QUICK_START.md) for the fastest way to get started!

### Option 1: Google Colab (Recommended for Beginners)

The easiest way to get started is using Google Colab:

1. Click the "Open in Colab" badge above
2. Select Runtime → Change runtime type → GPU (T4 or better)
3. Run the cells sequentially
4. Upload your image and get results!

### Option 2: Local Installation

#### Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended, but CPU works too)
- 10GB+ free disk space for the model

#### Installation

```bash
# Clone the repository
git clone https://github.com/azman0101/DeepSeek-OCR-Inference.git
cd DeepSeek-OCR-Inference

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Process a single image:

```bash
python inference.py --image path/to/your/image.jpg --output output_directory
```

With custom model or device:

```bash
python inference.py \
  --image path/to/your/image.jpg \
  --output output_directory \
  --device cuda \
  --model deepseek-ai/DeepSeek-OCR
```

### Python API

```python
from inference import DeepSeekOCRInference

# Initialize the model
ocr = DeepSeekOCRInference(
    model_name="deepseek-ai/DeepSeek-OCR",
    device=None  # Auto-detect GPU/CPU
)

# Process a single image
result = ocr.infer(
    image_path="path/to/image.jpg",
    output_path="output"
)
print(result)

# Batch processing
image_paths = ["img1.jpg", "img2.jpg", "img3.jpg"]
results = ocr.batch_infer(
    image_paths=image_paths,
    output_dir="batch_output"
)
```

See [example_usage.py](example_usage.py) for more examples.

## Project Structure

```
DeepSeek-OCR-Inference/
├── inference.py              # Main inference script
├── example_usage.py          # Usage examples
├── DeepSeek_OCR_Colab.ipynb # Google Colab notebook
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── .gitignore               # Git ignore rules
```

## Requirements

The main dependencies are:

- `torch>=2.6.0` - PyTorch deep learning framework
- `transformers>=4.48.0` - HuggingFace Transformers
- `tokenizers>=0.15.0` - Fast tokenizers
- `Pillow>=10.2.0` - Image processing
- `accelerate>=0.25.0` - Model acceleration
- `sentencepiece>=0.1.99` - Tokenization
- `protobuf>=4.25.8` - Protocol buffers

See [requirements.txt](requirements.txt) for the complete list.

## System Requirements

### Minimum Requirements
- **RAM**: 8GB
- **Disk Space**: 15GB
- **GPU**: Not required but highly recommended

### Recommended Requirements
- **RAM**: 16GB+
- **GPU**: NVIDIA GPU with 12GB+ VRAM (e.g., T4, V100, A100)
- **Disk Space**: 20GB+

## Performance Tips

1. **Use GPU**: GPU inference is 10-100x faster than CPU
2. **Batch Processing**: Process multiple images together for better efficiency
3. **Image Quality**: Higher resolution images typically produce better results
4. **Memory Management**: If you encounter OOM errors:
   - Use CPU instead of GPU
   - Process images one at a time
   - Reduce image resolution

## Troubleshooting

### Out of Memory (OOM) Error

```python
# Try using CPU instead
ocr = DeepSeekOCRInference(device="cpu")

# Or use float32 instead of float16
```

### Model Download Issues

If the model download is interrupted:

```bash
# Clear the cache and try again
rm -rf ~/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-OCR
```

### CUDA Not Available

If you have a NVIDIA GPU but CUDA is not detected:

```bash
# Reinstall PyTorch with CUDA support
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

## Examples

### Example 1: Simple OCR

```python
from inference import DeepSeekOCRInference

ocr = DeepSeekOCRInference()
result = ocr.infer("document.jpg")
print(result)
```

### Example 2: Document Analysis

```python
ocr = DeepSeekOCRInference()
result = ocr.infer(
    image_path="invoice.png",
    output_path="output"  # Saves additional analysis files
)
```

### Example 3: Batch Processing Multiple Documents

```python
ocr = DeepSeekOCRInference()
documents = ["doc1.jpg", "doc2.jpg", "doc3.jpg"]
results = ocr.batch_infer(documents, output_dir="processed")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for educational and research purposes. Please refer to the [DeepSeek-OCR model page](https://huggingface.co/deepseek-ai/DeepSeek-OCR) for model-specific licensing information.

## Citation

If you use DeepSeek-OCR in your research, please cite the original work:

```bibtex
@misc{deepseek-ocr,
  title={DeepSeek-OCR: Advanced OCR and Document Understanding},
  author={DeepSeek-AI},
  year={2024},
  howpublished={\url{https://huggingface.co/deepseek-ai/DeepSeek-OCR}}
}
```

## Resources

- [DeepSeek-OCR Model Card](https://huggingface.co/deepseek-ai/DeepSeek-OCR)
- [HuggingFace Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Google Colab Guide](https://colab.research.google.com/)

## Support

For issues and questions:
- Open an issue on [GitHub](https://github.com/azman0101/DeepSeek-OCR-Inference/issues)
- Check the [HuggingFace model page](https://huggingface.co/deepseek-ai/DeepSeek-OCR)

## Acknowledgments

- DeepSeek-AI team for developing the DeepSeek-OCR model
- HuggingFace for the Transformers library
- The open-source community

---

Made with ❤️ for the OCR and document understanding community