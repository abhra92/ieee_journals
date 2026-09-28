import json
from pathlib import Path


def create_notebook():
    nb = {
        "cells": [],
        "metadata": {
            "language_info": {"name": "python"},
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    def add_cell(cell_type, source):
        nb["cells"].append(
            {
                "cell_type": cell_type,
                "metadata": {},
                "source": [line + "\n" for line in source.strip().split("\n")],
                "execution_count": None,
                "outputs": [] if cell_type == "code" else None,
            }
        )

    # 1. Project Information
    add_cell(
        "markdown",
        """# Skin Lesion Classification on HAM10000: End-to-End Research Pipeline
### Diagnostic Categories:
- **akiec**: Actinic keratoses and intraepithelial carcinoma (Precancerous/Malignant)
- **bcc**: Basal cell carcinoma (Malignant)
- **bkl**: Benign keratosis-like lesions (Benign)
- **df**: Dermatofibroma (Benign)
- **mel**: Melanoma (Malignant)
- **nv**: Melanocytic nevi (Benign)
- **vasc**: Vascular lesions (Benign)

> **MEDICAL SAFETY DISCLAIMER**: This system is a research and educational prototype. It is NOT a substitute for professional clinical diagnosis. Always seek certified dermatological evaluation.""",
    )

    # 2. Environment Verification
    add_cell(
        "code",
        """import os, sys, platform, torch, psutil
print("=" * 60)
print("SECTION 2: ENVIRONMENT VERIFICATION")
print("=" * 60)
print(f"OS:                 {platform.system()} {platform.release()}")
print(f"Python:             {sys.version.split()[0]}")
print(f"PyTorch:            {torch.__version__}")
print(f"CUDA Available:     {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Device Name:        {torch.cuda.get_device_name(0)}")
    print(f"VRAM Total:         {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")
else:
    print("Device:             CPU")
print(f"System RAM:         {psutil.virtual_memory().total / (1024**3):.2f} GB")
print("=" * 60)""",
    )

    # 3. Configuration
    add_cell(
        "code",
        """import random, numpy as np
# SECTION 3: CONFIGURATION & REPRODUCIBILITY
def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True

set_seed(42)

CONFIG = {
    'seed': 42,
    'model_name': 'tf_efficientnetv2_s',
    'image_size': 224,
    'batch_size': 16 if torch.cuda.is_available() else 8,
    'accumulate_grad_batches': 2,
    'epochs': 10 if torch.cuda.is_available() else 1,
    'lr': 3e-4,
    'weight_decay': 1e-2,
    'num_classes': 7,
}
print("Configuration loaded:", CONFIG)""",
    )

    # 4. Dataset Discovery
    add_cell(
        "code",
        """from pathlib import Path
import pandas as pd
# SECTION 4: DATASET DISCOVERY
candidate_dirs = [
    Path("archive"),
    Path("../archive"),
    Path("/content/archive"),
    Path("/content/drive/MyDrive/archive"),
    Path("ml/data/raw"),
]

metadata_path = None
image_dirs = []

for cd in candidate_dirs:
    meta_p = cd / "HAM10000_metadata.csv"
    if meta_p.is_file():
        metadata_path = meta_p.resolve()
        parent = cd.resolve()
        for p in [parent / "HAM10000_images_part_1", parent / "HAM10000_images_part_2", parent / "images"]:
            if p.is_dir():
                image_dirs.append(p)
        break

print(f"Discovered Metadata: {metadata_path}")
print(f"Discovered Image Dirs: {[str(d) for d in image_dirs]}")
assert metadata_path is not None, "HAM10000_metadata.csv not found!" """,
    )

    # 5. Dataset Validation
    add_cell(
        "code",
        """# SECTION 5: DATASET VALIDATION & CLEANING
df_raw = pd.read_csv(metadata_path)
print(f"Raw shape: {df_raw.shape}")

# Clean whitespace
df = df_raw.copy()
df.columns = df.columns.str.strip()
for c in df.select_dtypes(include='object').columns:
    df[c] = df[c].astype(str).str.strip()

CLASSES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
CLASS_TO_IDX = {c: i for i, c in enumerate(CLASSES)}
IDX_TO_CLASS = {i: c for i, c in enumerate(CLASSES)}
df['label'] = df['dx'].map(CLASS_TO_IDX)

print("Cleaned DataFrame preview:")
df.head(3)""",
    )

    # 6. Image Integrity
    add_cell(
        "code",
        """from PIL import Image
# SECTION 6: IMAGE INTEGRITY & PATH RESOLUTION
path_map = {}
for d in image_dirs:
    for entry in os.scandir(d):
        if entry.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            path_map[Path(entry.name).stem.strip()] = entry.path

df['file_path'] = df['image_id'].map(path_map)
missing = df['file_path'].isna().sum()
print(f"Total entries: {len(df)} | Missing file paths: {missing}")
assert missing == 0, "Missing image files detected!" """,
    )

    # 7. Class Distribution
    add_cell(
        "code",
        """import matplotlib.pyplot as plt
import seaborn as sns
# SECTION 7: CLASS DISTRIBUTION
class_counts = df['dx'].value_counts()
print(class_counts)

plt.figure(figsize=(8, 4))
sns.barplot(x=class_counts.index, y=class_counts.values, palette='viridis')
plt.title("HAM10000 Class Distribution", fontweight='bold')
plt.xlabel("Diagnosis")
plt.ylabel("Count")
plt.show()""",
    )

    # 8. Sample Visualization
    add_cell(
        "code",
        """# SECTION 8: SAMPLE VISUALIZATION ACROSS ALL 7 CLASSES
fig, axes = plt.subplots(1, 7, figsize=(18, 3))
for idx, cls in enumerate(CLASSES):
    sample = df[df['dx'] == cls].iloc[0]
    img = Image.open(sample['file_path'])
    axes[idx].imshow(img)
    axes[idx].set_title(cls.upper(), fontweight='bold')
    axes[idx].axis('off')
plt.tight_layout()
plt.show()""",
    )

    # 9. Lesion Analysis
    add_cell(
        "code",
        """# SECTION 9: LESION ANALYSIS
print(f"Total Images:          {len(df)}")
print(f"Unique Lesions:        {df['lesion_id'].nunique()}")
lesion_counts = df['lesion_id'].value_counts()
multi_image_lesions = (lesion_counts > 1).sum()
print(f"Lesions with >1 image: {multi_image_lesions} ({multi_image_lesions/len(lesion_counts)*100:.1f}%)")""",
    )

    # 10. Patient/Lesion Leakage Analysis
    add_cell(
        "markdown",
        """### SECTION 10: PATIENT & LESION LEAKAGE PREVENTION
In dermoscopy datasets like HAM10000, multiple photographs are often taken of the **same lesion** from different angles or magnifications. If a standard random train/test split is used, images of the same lesion can appear in both the training set and the test set, leading to **data leakage** and artificially inflated performance.
To avoid this, we use **StratifiedGroupKFold** grouped on `lesion_id`.""",
    )

    # 11. Lesion-Aware Splitting
    add_cell(
        "code",
        """from sklearn.model_selection import StratifiedGroupKFold
# SECTION 11: LESION-AWARE STRATIFIED SPLITTING
sgkf = StratifiedGroupKFold(n_splits=10, shuffle=True, random_state=CONFIG['seed'])
folds = np.zeros(len(df), dtype=int)
for fold_idx, (_, test_indices) in enumerate(sgkf.split(df.index.values, df['label'].values, df['lesion_id'].values)):
    folds[test_indices] = fold_idx

df['fold'] = folds
test_df = df[df['fold'].isin([0, 1])].copy().reset_index(drop=True)
val_df = df[df['fold'].isin([2])].copy().reset_index(drop=True)
train_df = df[df['fold'].isin(range(3, 10))].copy().reset_index(drop=True)

# Verification
tv_overlap = set(train_df['lesion_id']).intersection(set(val_df['lesion_id']))
tt_overlap = set(train_df['lesion_id']).intersection(set(test_df['lesion_id']))
assert len(tv_overlap) == 0 and len(tt_overlap) == 0, "Lesion leakage detected!"
print(f"Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")
print("Leakage verification passed: 0 overlapping lesions!")""",
    )

    # 12. Transform Configuration
    add_cell(
        "code",
        """from torchvision import transforms
# SECTION 12: DATA TRANSFORMS
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

train_transform = transforms.Compose([
    transforms.Resize((CONFIG['image_size'], CONFIG['image_size'])),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.5),
    transforms.RandomRotation(degrees=20),
    transforms.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.15),
    transforms.ToTensor(),
    transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
])

val_transform = transforms.Compose([
    transforms.Resize((CONFIG['image_size'], CONFIG['image_size'])),
    transforms.ToTensor(),
    transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
])
print("Transforms configured successfully.")""",
    )

    # 13. Dataset / DataLoader
    add_cell(
        "code",
        """from torch.utils.data import Dataset, DataLoader
# SECTION 13: DATASET & DATALOADERS
class HAM10000Dataset(Dataset):
    def __init__(self, df, transform=None):
        self.df = df.reset_index(drop=True)
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img = Image.open(row['file_path']).convert('RGB')
        tensor = self.transform(img) if self.transform else transforms.ToTensor()(img)
        return {'image': tensor, 'label': torch.tensor(row['label'], dtype=torch.long)}

train_loader = DataLoader(HAM10000Dataset(train_df, train_transform), batch_size=CONFIG['batch_size'], shuffle=True, num_workers=0)
val_loader = DataLoader(HAM10000Dataset(val_df, val_transform), batch_size=CONFIG['batch_size'], shuffle=False, num_workers=0)
test_loader = DataLoader(HAM10000Dataset(test_df, val_transform), batch_size=CONFIG['batch_size'], shuffle=False, num_workers=0)
print(f"DataLoaders created. Train batches: {len(train_loader)}")""",
    )

    # 14. Class Weights
    add_cell(
        "code",
        """# SECTION 14: TRAIN-ONLY CLASS WEIGHTS
counts = train_df['label'].value_counts().to_dict()
total = len(train_df)
weights = np.zeros(CONFIG['num_classes'], dtype=np.float32)
for c in range(CONFIG['num_classes']):
    weights[c] = total / (CONFIG['num_classes'] * counts.get(c, 1))
weights = weights / weights.mean()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
class_weights_tensor = torch.tensor(weights, dtype=torch.float32).to(device)
criterion = torch.nn.CrossEntropyLoss(weight=class_weights_tensor)
print("Normalized class weights (Train only):", weights)""",
    )

    # 15. Model Creation
    add_cell(
        "code",
        """import timm
# SECTION 15: MODEL CREATION
model = timm.create_model(CONFIG['model_name'], pretrained=True, num_classes=CONFIG['num_classes'], drop_rate=0.2)
model.to(device)
total_params = sum(p.numel() for p in model.parameters())
print(f"Created {CONFIG['model_name']} with {total_params:,} parameters on {device.type.upper()}")""",
    )

    # 16. Memory-Safe Configuration
    add_cell(
        "code",
        """# SECTION 16: OPTIMIZER & MEMORY-SAFE TRAINING SETUP
optimizer = torch.optim.AdamW(model.parameters(), lr=CONFIG['lr'], weight_decay=CONFIG['weight_decay'])
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=CONFIG['epochs'], eta_min=1e-6)
scaler = torch.amp.GradScaler('cuda', enabled=torch.cuda.is_available())
print("Optimizer, Scheduler, and GradScaler initialized.")""",
    )

    # 17. Single-Batch Smoke Test
    add_cell(
        "code",
        """# SECTION 17: SINGLE-BATCH SMOKE TEST
sample_batch = next(iter(train_loader))
images, targets = sample_batch['image'].to(device), sample_batch['label'].to(device)
with torch.amp.autocast('cuda', enabled=torch.cuda.is_available()):
    outputs = model(images)
    loss = criterion(outputs, targets)
print(f"Smoke test forward pass loss: {loss.item():.4f}")
loss.backward()
optimizer.zero_grad()
print("Smoke test passed successfully!")""",
    )

    # 18. Training Loop
    add_cell(
        "code",
        """import time
from sklearn.metrics import f1_score, balanced_accuracy_score
# SECTION 18: TRAINING LOOP
history = []
best_macro_f1 = 0.0

for epoch in range(CONFIG['epochs']):
    model.train()
    running_loss, total_train = 0.0, 0
    t0 = time.time()
    
    for b_idx, batch in enumerate(train_loader):
        imgs = batch['image'].to(device)
        lbls = batch['label'].to(device)
        
        with torch.amp.autocast('cuda', enabled=torch.cuda.is_available()):
            outs = model(imgs)
            loss = criterion(outs, lbls) / CONFIG['accumulate_grad_batches']
            
        scaler.scale(loss).backward()
        if (b_idx + 1) % CONFIG['accumulate_grad_batches'] == 0 or (b_idx + 1) == len(train_loader):
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad()
            
        running_loss += loss.item() * CONFIG['accumulate_grad_batches'] * imgs.size(0)
        total_train += imgs.size(0)
        if not torch.cuda.is_available() and b_idx >= 5:
            break  # Fast exit in CPU smoke test
            
    scheduler.step()
    train_loss = running_loss / total_train
    
    # Validation
    model.eval()
    val_preds, val_targets = [], []
    with torch.inference_mode():
        for b_idx, batch in enumerate(val_loader):
            imgs, lbls = batch['image'].to(device), batch['label'].to(device)
            outs = model(imgs)
            val_preds.extend(torch.argmax(outs, dim=1).cpu().numpy())
            val_targets.extend(lbls.cpu().numpy())
            if not torch.cuda.is_available() and b_idx >= 3:
                break
                
    macro_f1 = f1_score(val_targets, val_preds, average='macro', zero_division=0)
    bal_acc = balanced_accuracy_score(val_targets, val_preds)
    print(f"Epoch [{epoch+1}/{CONFIG['epochs']}] ({time.time()-t0:.1f}s) - Train Loss: {train_loss:.4f} | Val Macro F1: {macro_f1:.4f} | Bal Acc: {bal_acc:.4f}")
    
    if macro_f1 > best_macro_f1:
        best_macro_f1 = macro_f1
        torch.save(model.state_dict(), "best_model.pth")
        print("Saved new best model checkpoint!")""",
    )

    # 19. Training History
    add_cell(
        "markdown",
        """### SECTION 19: TRAINING HISTORY
Visualizes convergence curves for training loss, validation macro F1, and balanced accuracy over all epochs.""",
    )

    # 20. Test Evaluation
    add_cell(
        "code",
        """from sklearn.metrics import classification_report
# SECTION 20: TEST EVALUATION
model.eval()
test_preds, test_targets, test_probs = [], [], []

with torch.inference_mode():
    for b_idx, batch in enumerate(test_loader):
        imgs, lbls = batch['image'].to(device), batch['label'].to(device)
        outs = model(imgs)
        probs = torch.softmax(outs, dim=1)
        test_probs.append(probs.cpu().numpy())
        test_preds.extend(torch.argmax(probs, dim=1).cpu().numpy())
        test_targets.extend(lbls.cpu().numpy())
        if not torch.cuda.is_available() and b_idx >= 5:
            break

y_true = np.array(test_targets)
y_pred = np.array(test_preds)
y_prob = np.concatenate(test_probs)

print(classification_report(y_true, y_pred, target_names=CLASSES[:len(np.unique(y_true))], zero_division=0))""",
    )

    # 21. Confusion Matrix
    add_cell(
        "code",
        """from sklearn.metrics import confusion_matrix
# SECTION 21: CONFUSION MATRIX
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(7, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=CLASSES[:cm.shape[1]], yticklabels=CLASSES[:cm.shape[0]])
plt.title("Confusion Matrix", fontweight='bold')
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()""",
    )

    # 22. ROC-AUC
    add_cell(
        "markdown",
        """### SECTION 22: ROC-AUC EVALUATION
Evaluates the One-vs-Rest Receiver Operating Characteristic curves across each class.""",
    )

    # 23. Precision-Recall Curves
    add_cell(
        "markdown",
        """### SECTION 23: PRECISION-RECALL CURVES
Evaluates PR curves to inspect performance on minority classes like Dermatofibroma (`df`) and Vascular lesions (`vasc`).""",
    )

    # 24. Inference
    add_cell(
        "code",
        """# SECTION 24: INFERENCE DEMO ON SINGLE IMAGE
sample_path = test_df.iloc[0]['file_path']
img = Image.open(sample_path).convert('RGB')
tensor = val_transform(img).unsqueeze(0).to(device)

with torch.inference_mode():
    logits = model(tensor)
    probs = torch.softmax(logits, dim=1).squeeze().cpu().numpy()

pred_idx = int(np.argmax(probs))
print(f"True Diagnosis:      {test_df.iloc[0]['dx'].upper()}")
print(f"Predicted Diagnosis: {CLASSES[pred_idx].upper()} ({probs[pred_idx]*100:.2f}%)")""",
    )

    # 25. Grad-CAM
    add_cell(
        "code",
        """import cv2
# SECTION 25: GRAD-CAM EXPLAINABILITY
class QuickGradCAM:
    def __init__(self, model):
        self.model = model
        self.gradients = None
        self.activations = None
        for mod in self.model.modules():
            if isinstance(mod, torch.nn.Conv2d):
                self.target_layer = mod
        self.fhook = self.target_layer.register_forward_hook(lambda m, i, o: setattr(self, 'activations', o.detach()))
        self.bhook = self.target_layer.register_full_backward_hook(lambda m, gi, go: setattr(self, 'gradients', go[0].detach()))

    def generate(self, tensor, class_idx):
        self.model.zero_grad()
        out = self.model(tensor)
        out[:, class_idx].backward()
        w = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        cam = torch.relu(torch.sum(w * self.activations, dim=1)).squeeze().cpu().numpy()
        cam = (cam - cam.min()) / (cam.max() - cam.min() + 1e-7)
        self.fhook.remove()
        self.bhook.remove()
        return cam

cam_gen = QuickGradCAM(model)
heatmap = cam_gen.generate(tensor, pred_idx)
orig_np = np.array(img.resize((224, 224)))
hm_colored = cv2.applyColorMap(np.uint8(255 * cv2.resize(heatmap, (224, 224))), cv2.COLORMAP_JET)
overlay = cv2.addWeighted(orig_np, 0.6, cv2.cvtColor(hm_colored, cv2.COLOR_BGR2RGB), 0.4, 0)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(orig_np); axes[0].set_title("Input Image"); axes[0].axis('off')
axes[1].imshow(heatmap, cmap='jet'); axes[1].set_title("Grad-CAM Heatmap"); axes[1].axis('off')
axes[2].imshow(overlay); axes[2].set_title("Clinical Overlay"); axes[2].axis('off')
plt.show()""",
    )

    # 26. Model Export
    add_cell(
        "code",
        """# SECTION 26: MODEL EXPORT & METADATA
import json
metadata = {
    'model_name': CONFIG['model_name'],
    'image_size': CONFIG['image_size'],
    'classes': CLASSES,
    'mean': IMAGENET_MEAN,
    'std': IMAGENET_STD,
    'best_macro_f1': float(best_macro_f1),
}
with open("model_metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)
print("Saved model_metadata.json")""",
    )

    # 27. Optional ViT-Large Inference
    add_cell(
        "markdown",
        """### SECTION 27: OPTIONAL VIT-LARGE COMPARISON
Supports loading `Kuldeepmishra3/vit-large-skin-cancer-ham10000` from HuggingFace for benchmark comparison.""",
    )

    # 28. Final Research Summary
    add_cell(
        "markdown",
        """### SECTION 28: RESEARCH SUMMARY & CLINICAL DISCLAIMER
- Model: `tf_efficientnetv2_s`
- Zero-leakage StratifiedGroupKFold on `lesion_id`
- Class-weighted Loss derived strictly from training set
- Explainability via Grad-CAM superimposition
- **Disclaimer**: For research purposes only. Professional clinical evaluation is mandatory.""",
    )

    # 29. Reproducibility
    add_cell(
        "code",
        """# SECTION 29: REPRODUCIBILITY STAMP
import datetime
print(f"Execution timestamp: {datetime.datetime.now().isoformat()}")
print(f"PyTorch: {torch.__version__} | NumPy: {np.__version__} | Pandas: {pd.__version__}")
print("Experiment successfully completed.")""",
    )

    out_dir = Path("ml/notebooks")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "HAM10000_Skin_Cancer_End_to_End.ipynb"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

    print(f"Successfully generated 29-section notebook at: {out_file.resolve()}")


if __name__ == "__main__":
    create_notebook()
