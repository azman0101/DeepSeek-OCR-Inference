#!/usr/bin/env python3
"""
Test script to validate DeepSeek-OCR-Inference installation and setup
"""

import sys
import importlib.util


def check_module(module_name, display_name=None):
    """Check if a module is installed"""
    if display_name is None:
        display_name = module_name
    
    spec = importlib.util.find_spec(module_name)
    if spec is not None:
        print(f"✓ {display_name} is installed")
        return True
    else:
        print(f"✗ {display_name} is NOT installed")
        return False


def check_cuda():
    """Check CUDA availability"""
    try:
        import torch
        if torch.cuda.is_available():
            print(f"✓ CUDA is available (GPU: {torch.cuda.get_device_name(0)})")
            return True
        else:
            print("⚠ CUDA is not available (CPU mode only)")
            return False
    except ImportError:
        print("✗ Cannot check CUDA (torch not installed)")
        return False


def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} is too old (need 3.8+)")
        return False


def check_disk_space():
    """Check available disk space"""
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        free_gb = free // (2**30)
        
        if free_gb >= 15:
            print(f"✓ Sufficient disk space ({free_gb} GB available)")
            return True
        else:
            print(f"⚠ Low disk space ({free_gb} GB available, 15 GB+ recommended)")
            return False
    except Exception as e:
        print(f"⚠ Could not check disk space: {e}")
        return True  # Don't fail on this


def main():
    """Run all checks"""
    print("=" * 60)
    print("DeepSeek-OCR-Inference Installation Test")
    print("=" * 60)
    
    all_passed = True
    
    # Check Python version
    print("\n1. Python Version:")
    if not check_python_version():
        all_passed = False
    
    # Check required modules
    print("\n2. Required Dependencies:")
    required_modules = [
        ("torch", "PyTorch"),
        ("transformers", "Transformers"),
        ("tokenizers", "Tokenizers"),
        ("PIL", "Pillow"),
        ("accelerate", "Accelerate"),
        ("sentencepiece", "SentencePiece"),
    ]
    
    for module_name, display_name in required_modules:
        if not check_module(module_name, display_name):
            all_passed = False
    
    # Check CUDA
    print("\n3. GPU/CUDA Support:")
    check_cuda()  # Not required, just informational
    
    # Check disk space
    print("\n4. Disk Space:")
    check_disk_space()  # Not critical
    
    # Check if inference.py exists and can be imported
    print("\n5. Project Files:")
    try:
        import inference
        print("✓ inference.py can be imported")
    except ImportError as e:
        print(f"✗ Cannot import inference.py: {e}")
        all_passed = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All critical checks passed!")
        print("You're ready to use DeepSeek-OCR-Inference!")
        print("\nNext steps:")
        print("  - Run: python inference.py --image your_image.jpg")
        print("  - Or open: DeepSeek_OCR_Colab.ipynb in Google Colab")
    else:
        print("✗ Some checks failed")
        print("\nTo install dependencies:")
        print("  pip install -r requirements.txt")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
