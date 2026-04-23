"""
adversarial_example_generator.py
---------------------------------
Generates adversarial examples using the Fast Gradient Sign Method (FGSM).

Educational purposes only. Only use on models you own or have permission to test.

Usage:
    python adversarial_example_generator.py --help
    python adversarial_example_generator.py --epsilon 0.03 --image path/to/image.png

Requirements:
    pip install torch torchvision pillow numpy matplotlib
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="FGSM Adversarial Example Generator (educational demo)"
    )
    parser.add_argument(
        "--epsilon",
        type=float,
        default=0.03,
        help="Perturbation magnitude (default: 0.03)",
    )
    parser.add_argument(
        "--image",
        type=str,
        default=None,
        help="Path to input image. If omitted, a random tensor is used.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="adversarial_output.png",
        help="Path to save the adversarial image (default: adversarial_output.png)",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display original and adversarial images side-by-side",
    )
    return parser.parse_args()


def fgsm_attack(image, epsilon, gradient):
    """Apply the FGSM perturbation to an image tensor."""
    sign_gradient = gradient.sign()
    perturbed = image + epsilon * sign_gradient
    # Clamp pixel values to valid range [0, 1]
    perturbed = perturbed.clamp(0, 1)
    return perturbed


def run(args):
    try:
        import torch
        import torchvision.models as models
        import torchvision.transforms as transforms
        from PIL import Image
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("Install requirements with: pip install torch torchvision pillow numpy matplotlib")
        sys.exit(1)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] Using device: {device}")

    # --- Load pre-trained model ---
    print("[*] Loading pre-trained ResNet-18 model...")
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    model.eval().to(device)

    # --- Prepare input image ---
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    if args.image:
        print(f"[*] Loading image: {args.image}")
        img = Image.open(args.image).convert("RGB")
        input_tensor = transform(img).unsqueeze(0).to(device)
    else:
        print("[*] No image provided — using random tensor as demo input.")
        input_tensor = torch.rand(1, 3, 224, 224).to(device)

    input_tensor.requires_grad = True

    # --- Forward pass ---
    output = model(input_tensor)
    original_pred = output.argmax(dim=1).item()
    print(f"[*] Original prediction class index: {original_pred}")

    # --- Compute loss (target = original prediction) ---
    criterion = torch.nn.CrossEntropyLoss()
    target = torch.tensor([original_pred]).to(device)
    loss = criterion(output, target)

    # --- Backward pass ---
    model.zero_grad()
    loss.backward()

    # --- Generate adversarial example ---
    gradient = input_tensor.grad.data
    adversarial = fgsm_attack(input_tensor, args.epsilon, gradient)

    # --- Evaluate adversarial example ---
    with torch.no_grad():
        adv_output = model(adversarial)
    adversarial_pred = adv_output.argmax(dim=1).item()
    print(f"[*] Adversarial prediction class index: {adversarial_pred}")

    if original_pred != adversarial_pred:
        print(f"[+] Attack successful! Prediction changed: {original_pred} → {adversarial_pred}")
    else:
        print(f"[-] Attack unsuccessful — prediction unchanged at {original_pred}. Try increasing --epsilon.")

    # --- Save output ---
    adv_np = adversarial.squeeze().detach().cpu().numpy().transpose(1, 2, 0)
    adv_img = Image.fromarray((adv_np * 255).astype(np.uint8))
    adv_img.save(args.output)
    print(f"[*] Adversarial image saved to: {args.output}")

    # --- Optional display ---
    if args.show:
        orig_np = input_tensor.squeeze().detach().cpu().numpy().transpose(1, 2, 0)
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))
        axes[0].imshow(orig_np)
        axes[0].set_title(f"Original (class {original_pred})")
        axes[0].axis("off")
        axes[1].imshow(adv_np)
        axes[1].set_title(f"Adversarial (class {adversarial_pred})")
        axes[1].axis("off")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    args = parse_args()
    run(args)
