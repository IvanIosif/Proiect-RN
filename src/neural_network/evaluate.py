import pandas as pd
import numpy as np
import os
import json
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import f1_score, confusion_matrix

# --- 1. CONFIGURARE CĂI ---
PATH_BASE = r"D:\Facultate\RN"
PATH_DATA = os.path.join(PATH_BASE, "data", "test")
PATH_MODELS = os.path.join(PATH_BASE, "models")
# Locația unde se salvează totul (Metrici + Matrice)
PATH_SAVE_FINAL = os.path.join(PATH_BASE, "results", "train_model_etapa 5")

# Creăm folderul dacă nu există
os.makedirs(PATH_SAVE_FINAL, exist_ok=True)

def run_evaluation():
    # --- 2. ÎNCĂRCARE DATE TEST ---
    p_path = os.path.join(PATH_DATA, "pneumonie", "pneumonie_test.csv")
    t_path = os.path.join(PATH_DATA, "tuberculoza", "tuberculoza_test.csv")
    
    if not os.path.exists(p_path) or not os.path.exists(t_path):
        print("❌ Datele de test nu au fost găsite!")
        return

    df_p = pd.read_csv(p_path)
    df_t = pd.read_csv(t_path)
    df_test = pd.concat([df_p, df_t], ignore_index=True)
    
    X_test = df_test.drop('Diagnosis', axis=1).values.astype('float32')
    y_test = df_test['Diagnosis'].values.astype('float32')

    # --- 3. ÎNCĂRCARE MODEL (.keras) ---
    model_path = os.path.join(PATH_MODELS, "trained_model.keras")
    if not os.path.exists(model_path):
        print(f"❌ Modelul nu a fost găsit la {model_path}")
        return

    model = tf.keras.models.load_model(model_path)

    # --- 4. CALCUL METRICI ---
    y_pred_prob = model.predict(X_test, verbose=0)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()

    acc = np.mean(y_pred == y_test)
    f1 = f1_score(y_test, y_pred, average='macro')

    # OUTPUT AȘTEPTAT ÎN CONSOLĂ
    print(f"\n# Output așteptat:")
    print(f"# Test Accuracy: {acc:.4f}")
    print(f"# Test F1-score (macro): {f1:.4f}")

    # --- 5. SALVARE LIVRABILE ÎN FOLDERUL ETAPA 5 ---
    
    # A. Salvare JSON
    metrics = {
        "test_accuracy": round(float(acc), 4),
        "f1_macro": round(float(f1), 4)
    }
    json_path = os.path.join(PATH_SAVE_FINAL, "test_metrics.json")
    with open(json_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"# ✓ Metrics saved to {json_path}")

    # B. Salvare Confusion Matrix (Tot în folderul de rezultate)
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Pneumonie', 'TBC'], 
                yticklabels=['Pneumonie', 'TBC'])
    plt.title('Confusion Matrix - Etapa 5')
    plt.xlabel('Predicție')
    plt.ylabel('Realitate')
    
    cm_path = os.path.join(PATH_SAVE_FINAL, "confusion_matrix.png")
    plt.savefig(cm_path)
    plt.close()
    print(f"# ✓ Confusion matrix saved to {cm_path}")

if __name__ == "__main__":
    run_evaluation()