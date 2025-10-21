"""
DeepSeek-OCR Inference Script
Provides a simple interface for running OCR inference using the DeepSeek-OCR model.
"""

import os
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image


class DeepSeekOCRInference:
    """Main class for DeepSeek-OCR inference."""
    
    def __init__(self, model_name="deepseek-ai/DeepSeek-OCR", device=None):
        """
        Initialize the DeepSeek-OCR model.
        
        Args:
            model_name (str): HuggingFace model identifier
            device (str): Device to run the model on ('cuda', 'cpu', or None for auto)
        """
        self.model_name = model_name
        
        # Auto-detect device if not specified
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        print(f"Loading model '{model_name}' on device '{self.device}'...")
        
        # Load tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )
        
        # Move model to device and set to eval mode
        self.model.to(self.device)
        self.model.eval()
        
        print("Model loaded successfully!")
    
    def infer(self, image_path, output_path=None, prompt=None):
        """
        Run inference on an image.
        
        Args:
            image_path (str): Path to the input image
            output_path (str): Optional path to save the output
            prompt (str): Optional custom prompt for the model
            
        Returns:
            str: The OCR result
        """
        # Verify image exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
        
        print(f"Processing image: {image_path}")
        
        # Run inference using the model's infer method
        try:
            result = self.model.infer(
                self.tokenizer,
                image_file=image_path,
                output_path=output_path
            )
            
            print("Inference completed successfully!")
            return result
            
        except Exception as e:
            print(f"Error during inference: {e}")
            raise
    
    def batch_infer(self, image_paths, output_dir=None):
        """
        Run inference on multiple images.
        
        Args:
            image_paths (list): List of paths to input images
            output_dir (str): Optional directory to save outputs
            
        Returns:
            list: List of OCR results
        """
        results = []
        
        for i, image_path in enumerate(image_paths):
            print(f"\nProcessing image {i+1}/{len(image_paths)}")
            
            output_path = None
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                basename = os.path.basename(image_path)
                output_path = os.path.join(output_dir, f"output_{basename}")
            
            result = self.infer(image_path, output_path)
            results.append(result)
        
        return results


def main():
    """Main function for CLI usage."""
    parser = argparse.ArgumentParser(
        description="DeepSeek-OCR Inference Tool"
    )
    parser.add_argument(
        "--image",
        type=str,
        required=True,
        help="Path to the input image"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Path to save the output (optional)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="deepseek-ai/DeepSeek-OCR",
        help="HuggingFace model identifier"
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        choices=["cuda", "cpu"],
        help="Device to run inference on (default: auto-detect)"
    )
    
    args = parser.parse_args()
    
    # Initialize inference
    ocr = DeepSeekOCRInference(
        model_name=args.model,
        device=args.device
    )
    
    # Run inference
    result = ocr.infer(
        image_path=args.image,
        output_path=args.output
    )
    
    # Print result
    print("\n" + "="*50)
    print("OCR RESULT:")
    print("="*50)
    print(result)
    print("="*50)


if __name__ == "__main__":
    main()
