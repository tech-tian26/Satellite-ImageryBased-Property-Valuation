# 🏠 Satellite Imagery Based Property Valuation  
### Multimodal Regression using Tabular Data & Satellite Images

---

## 📌 Project Overview

This project investigates a **multimodal machine learning approach** for real estate price prediction by combining **structured tabular data** with **satellite imagery**. Traditional automated valuation models rely primarily on numerical features such as property size, quality, and location. This work evaluates whether neighborhood-level visual context, extracted from satellite images, can enhance valuation accuracy and interpretability.

Multiple modeling strategies are explored, including image-only deep learning models, strong tabular baselines, multimodal residual learning, and PCA-based feature fusion. The final predictions are generated using the **best-performing tabular model**.

---

## 🎯 Objectives

- Predict property prices using historical housing data  
- Programmatically acquire satellite images using latitude and longitude  
- Perform tabular, geospatial, and image-based exploratory analysis  
- Extract visual embeddings using convolutional neural networks (CNNs)  
- Evaluate multimodal fusion strategies  
- Ensure model interpretability using Grad-CAM and feature importance  

---

## 📂 Repository Structure

# 🏠 Satellite Imagery Based Property Valuation  
### Multimodal Regression using Tabular Data & Satellite Images

---

## 📌 Project Overview

This project investigates a **multimodal machine learning approach** for real estate price prediction by combining **structured tabular data** with **satellite imagery**. Traditional automated valuation models rely primarily on numerical features such as property size, quality, and location. This work evaluates whether neighborhood-level visual context, extracted from satellite images, can enhance valuation accuracy and interpretability.

Multiple modeling strategies are explored, including image-only deep learning models, strong tabular baselines, multimodal residual learning, and PCA-based feature fusion. The final predictions are generated using the **best-performing tabular model**.

---

## 🎯 Objectives

- Predict property prices using historical housing data  
- Programmatically acquire satellite images using latitude and longitude  
- Perform tabular, geospatial, and image-based exploratory analysis  
- Extract visual embeddings using convolutional neural networks (CNNs)  
- Evaluate multimodal fusion strategies  
- Ensure model interpretability using Grad-CAM and feature importance  

---

## 📂 Repository Structure

# 🏠 Satellite Imagery Based Property Valuation  
### Multimodal Regression using Tabular Data & Satellite Images

---

## 📌 Project Overview

This project investigates a **multimodal machine learning approach** for real estate price prediction by combining **structured tabular data** with **satellite imagery**. Traditional automated valuation models rely primarily on numerical features such as property size, quality, and location. This work evaluates whether neighborhood-level visual context, extracted from satellite images, can enhance valuation accuracy and interpretability.

Multiple modeling strategies are explored, including image-only deep learning models, strong tabular baselines, multimodal residual learning, and PCA-based feature fusion. The final predictions are generated using the **best-performing tabular model**.

---

## 🎯 Objectives

- Predict property prices using historical housing data  
- Programmatically acquire satellite images using latitude and longitude  
- Perform tabular, geospatial, and image-based exploratory analysis  
- Extract visual embeddings using convolutional neural networks (CNNs)  
- Evaluate multimodal fusion strategies  
- Ensure model interpretability using Grad-CAM and feature importance  

---

## 📂 Repository Structure

# 🏠 Satellite Imagery Based Property Valuation  
### Multimodal Regression using Tabular Data & Satellite Images

---

## 📌 Project Overview

This project investigates a **multimodal machine learning approach** for real estate price prediction by combining **structured tabular data** with **satellite imagery**. Traditional automated valuation models rely primarily on numerical features such as property size, quality, and location. This work evaluates whether neighborhood-level visual context, extracted from satellite images, can enhance valuation accuracy and interpretability.

Multiple modeling strategies are explored, including image-only deep learning models, strong tabular baselines, multimodal residual learning, and PCA-based feature fusion. The final predictions are generated using the **best-performing tabular model**.

---

## 🎯 Objectives

- Predict property prices using historical housing data  
- Programmatically acquire satellite images using latitude and longitude  
- Perform tabular, geospatial, and image-based exploratory analysis  
- Extract visual embeddings using convolutional neural networks (CNNs)  
- Evaluate multimodal fusion strategies  
- Ensure model interpretability using Grad-CAM and feature importance  

---

## 📂 Repository Structure

│
├── data_fetcher.py
├── preprocessing_training.ipynb
├── enrollno_final.csv
├── enrollno_report.pdf
└── README.md


### File Description

- **data_fetcher.py**  
  Script used to download satellite images from the Mapbox Static Images API using latitude and longitude coordinates.

- **preprocessing_training.ipynb**  
  Data cleaning, feature engineering, and exploratory data analysis (EDA) on tabular and image data.
  
  Training and evaluation of:
  - Image-only CNN (ResNet-18)  
  - Tabular models (XGBoost, Random Forest, Gradient Boosting)  
  - Multimodal residual CNN + tabular model  
  - PCA-based embedding fusion  
  Also includes Grad-CAM visualization and final evaluation.

- **enrollno_final.csv**  
  Final prediction file generated using the selected tabular model.  
  **Format:** `id, predicted_price`

- **enrollno_report.pdf**  
  Complete project report including EDA, modeling approach, results, architecture diagrams, and interpretability analysis.

---

## Satellite Image Acquisition

Satellite images were fetched using the **Mapbox Static Images API** based on property latitude and longitude.

- Image size: 224 × 224  
- Zoom level: 16  
- View type: Satellite  

Images were downloaded once and reused for all experiments due to API and compute constraints. The data acquisition script is provided for reproducibility.

---

## 🧪 Modeling Summary

###  Image-Only Model
- CNN: ResNet-18 (pretrained)
- Learns neighborhood-level visual patterns
- Demonstrates limited predictive power when used alone

###  Tabular Models
- Linear Regression, Random Forest, Gradient Boosting
- **XGBoost** achieved the best performance
- Captures nonlinear relationships among structural and locational features

###  Multimodal Residual Model
- Tabular model predicts a base price
- CNN predicts a residual correction from satellite imagery
- Improves interpretability while maintaining prediction stability

###  PCA-Based Feature Fusion
- CNN embeddings compressed using PCA
- Fused with tabular features
- Performance comparable to tabular-only models, confirming weak but complementary image signals

---

## 📊 Results (Log-Price Space)

| Model | R² Score |
|------|---------|
| Image-Only CNN | Low (~0.4–0.6) |
| Multimodal Residual Model | ~0.75 |
| PCA Fusion + XGBoost | ~0.89 |
| **Tabular XGBoost** | **~0.90** |

---

##  Explainability

- **Grad-CAM** visualizes spatial regions in satellite images influencing CNN predictions, highlighting broad neighborhood patterns such as greenery and urban density.  
- **Feature Importance** analysis for the tabular XGBoost model identifies living area, property grade, latitude, and view as key drivers of price.  
- **Predicted vs True price plots** confirm strong model calibration and generalization.

---

##  Final Model Selection

The **tabular XGBoost regressor** was selected as the final model for generating property price predictions due to its superior accuracy, robustness, and interpretability. Satellite imagery contributed valuable contextual insights but remained a complementary signal rather than a primary predictor.

---

## 🔮 Conclusion

This project demonstrates that structured tabular features are the dominant drivers of real estate valuation accuracy, while satellite imagery enhances contextual understanding and interpretability. Multimodal learning is most effective when visual information augments strong tabular models rather than replacing them.

---

## 👤 Author

**Name:** _[Gauri Bhardwaj]_  

✅ This repository is complete, organized, and ready for submission.
