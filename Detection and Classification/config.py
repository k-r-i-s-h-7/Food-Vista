"""
Configuration file for Food Classification Models
Adjust hyperparameters here instead of in notebooks
"""

# ============================================
# Dataset Configuration
# ============================================
DATASET_LOCATION = "./food-1"  # Path to dataset folder
BATCH_SIZE = 32
IMG_SIZE = 224

# ============================================
# Training Configuration
# ============================================
LEARNING_RATE = 1e-4
WEIGHT_DECAY = 1e-4
EPOCHS = 10
DEVICE = "cuda"  # or "cpu" if no GPU

# ============================================
# Model Configuration
# ============================================
DROPOUT_RATE = 0.5

# PyTorch Models
RESNET18_LR = 1e-4
MOBILENETV2_LR = 3e-4

# TensorFlow Models
RESNET50_TF_LR = 3e-4
RESNET50_TF_EPOCHS = 20

# ============================================
# Data Augmentation
# ============================================
AUGMENTATION_ENABLED = True
AUGMENTATION_CONFIG = {
    "random_crop_scale": (0.8, 1.0),
    "random_flip": True,
    "random_rotation": 20,
    "color_jitter": 0.3,
    "perspective_distortion": 0.2,
}
