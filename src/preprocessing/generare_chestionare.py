import pandas as pd
import numpy as np
import os

def generate_raw_inconsistent():
    np.random.seed(42)
    # Definim toate căile necesare, inclusiv RAW pentru procesare ulterioară
    path_raw = r"D:\Facultate\RN\docs\raw"
    path_p = os.path.join(path_raw, "Pneumonie")
    path_t = os.path.join(path_raw, "Tuberculoza")
    
    os.makedirs(path_p, exist_ok=True)
    os.makedirs(path_t, exist_ok=True)

    num_samples = 4000
    cols = [f"Q{i}" for i in range(1, 21)]

    def create_noisy_data(label):
        data = []
        for _ in range(num_samples):
            # GENERĂM HAOS: 
            # În loc de șabloane fixe, generăm valori random (1-5) pentru TOATE întrebările.
            # Aceasta creează o variabilitate uriașă între pacienții cu aceeași boală.
            row = np.random.randint(1, 6, 20)
            
            # Introducem o corelație foarte slabă (doar 10-15% influență) 
            # pentru ca modelul să nu rămână blocat fix la 50% (noroc pur), 
            # ci să încerce să învețe ceva ce nu îi reușește complet.
            if label == 0: # Pneumonie
                # Modificăm doar 3 coloane să tindă spre valori mici (1-3)
                indices_to_mod = [5, 10, 14]
                for idx in indices_to_mod:
                    if np.random.rand() > 0.4: # 60% șansă să fie "specific"
                        row[idx] = np.random.randint(1, 3)
            else: # TBC
                # Modificăm doar 3 coloane să tindă spre valori mari (4-5)
                indices_to_mod = [5, 10, 14]
                for idx in indices_to_mod:
                    if np.random.rand() > 0.4:
                        row[idx] = np.random.randint(4, 6)
            
            data.append(np.append(row, [label]))
        return data

    # Salvăm fișierele
    data_p = create_noisy_data(0)
    pd.DataFrame(data_p, columns=cols + ["Diagnosis"]).to_csv(os.path.join(path_p, "cases.csv"), index=False)

    data_t = create_noisy_data(1)
    pd.DataFrame(data_t, columns=cols + ["Diagnosis"]).to_csv(os.path.join(path_t, "cases.csv"), index=False)

    print("--- Faza 1 Gata ---")
    print("Date HAOTICE salvate. Pacienții nu mai seamănă între ei.")
    print(f"Locație: {path_raw}")

if __name__ == "__main__":
    generate_raw_inconsistent()