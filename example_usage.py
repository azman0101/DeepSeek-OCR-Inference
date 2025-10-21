"""
Example usage of DeepSeek-OCR Inference

This script demonstrates different ways to use the DeepSeek-OCR model
for optical character recognition and document understanding.
"""

import os
from inference import DeepSeekOCRInference


def example_single_image():
    """Example: Process a single image"""
    print("=" * 60)
    print("Example 1: Single Image Processing")
    print("=" * 60)
    
    # Initialize the model
    ocr = DeepSeekOCRInference(
        model_name="deepseek-ai/DeepSeek-OCR",
        device=None  # Auto-detect
    )
    
    # Process an image
    image_path = "path/to/your/image.jpg"
    output_path = "output"
    
    result = ocr.infer(
        image_path=image_path,
        output_path=output_path
    )
    
    print("\nResult:")
    print(result)


def example_batch_processing():
    """Example: Process multiple images"""
    print("\n" + "=" * 60)
    print("Example 2: Batch Processing")
    print("=" * 60)
    
    # Initialize the model
    ocr = DeepSeekOCRInference()
    
    # List of images to process
    image_paths = [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg"
    ]
    
    # Process all images
    results = ocr.batch_infer(
        image_paths=image_paths,
        output_dir="batch_output"
    )
    
    # Print all results
    for i, (path, result) in enumerate(zip(image_paths, results)):
        print(f"\nResult {i+1} ({path}):")
        print(result)


def example_custom_device():
    """Example: Specify device explicitly"""
    print("\n" + "=" * 60)
    print("Example 3: Custom Device Selection")
    print("=" * 60)
    
    # Force CPU usage (useful for testing or limited GPU memory)
    ocr_cpu = DeepSeekOCRInference(device="cpu")
    
    # Or force CUDA usage
    # ocr_gpu = DeepSeekOCRInference(device="cuda")
    
    print("Model loaded on CPU")


def main():
    """Run all examples"""
    print("DeepSeek-OCR Inference Examples")
    print("=" * 60)
    print("\nNote: Update the image paths before running!\n")
    
    # Uncomment the examples you want to run:
    
    # example_single_image()
    # example_batch_processing()
    # example_custom_device()
    
    print("\n" + "=" * 60)
    print("To run these examples:")
    print("1. Update the image paths in the functions above")
    print("2. Uncomment the example functions you want to run")
    print("3. Run: python example_usage.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
