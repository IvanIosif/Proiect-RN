import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

def process_to_specific_folders():
    # 1. CĂI DE INTRARE (RAW)
    path_raw_p = r"D:\Facultate\RN\docs\raw\Pneumonie\cases.csv"
    path_raw_t = r"D:\Facultate\RN\docs\raw\Tuberculoza\cases.csv"
    
    # 2. CĂI DE IEȘIRE (PROCESSED) - Exact unde ai cerut
    path_proc_p = r"D:\Facultate\RN\docs\processed\Pneumonia"
    path_proc_t = r"D:\Facultate\RN\docs\processed\Tuberculoza"
    
    # Cale pentru scaler (necesar pentru UI/Streamlit ulterior)
    path_config = r"D:\Facultate\RN\config"

    # Creăm folderele de ieșire dacă nu există
    os.makedirs(path_proc_p, exist_ok=True)
    os.makedirs(path_proc_t, exist_ok=True)
    os.makedirs(path_config, exist_ok=True)

    # 3. VERIFICARE ȘI ÎNCĂRCARE DATE
    if not os.path.exists(path_raw_p) or not os.path.exists(path_raw_t):
        print("❌ Eroare: Nu am găsit fișierele brute (RAW) în locațiile specificate.")
        return

    df_p = pd.read_csv(path_raw_p)
    df_t = pd.read_csv(path_raw_t)

    # 4. NORMALIZARE STANDARD (Min-Max Scaling)
    # Mapăm valorile din intervalul [1, 5] în intervalul [0, 1]
    # 1 -> 0.0 | 2 -> 0.25 | 3 -> 0.5 | 4 -> 0.75 | 5 -> 1.0
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit(np.array([[1]*20, [5]*20])) 

    def normalize_df(df, label):
        # Separăm simptomele de diagnostic
        X = df.drop('Diagnosis', axis=1)
        # Aplicăm transformarea matematică
        X_scaled = scaler.transform(X)
        # Reconstruim DataFrame-ul
        new_df = pd.DataFrame(X_scaled, columns=X.columns)
        new_df['Diagnosis'] = label
        return new_df

    # Procesăm ambele categorii
    df_p_norm = normalize_df(df_p, 0)
    df_t_norm = normalize_df(df_t, 1)

    # 5. SALVARE FINALĂ
    # Salvăm rezultatele în folderele cerute
    file_p_final = os.path.join(path_proc_p, "pneumonia_processed.csv")
    file_t_final = os.path.join(path_proc_t, "tuberculoza_processed.csv")
    
    df_p_norm.to_csv(file_p_final, index=False)
    df_t_norm.to_csv(file_t_final, index=False)
    
    # Salvăm scaler-ul pentru a păstra consistența datelor în viitor
    joblib.dump(scaler, os.path.join(path_config, "scaler.pkl"))

    print(f"✅ Succes! Datele normalizate au fost salvate în:")
    print(f"   -> {path_proc_p}")
    print(f"   -> {path_proc_t}")

if __name__ == "__main__":
    process_to_specific_folders()