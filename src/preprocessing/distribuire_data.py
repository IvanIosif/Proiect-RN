import pandas as pd
import os
from sklearn.model_selection import train_test_split

def distribute_to_folders():
    # 1. DEFINIREA CĂILOR DE INTRARE (Datele procesate anterior)
    path_proc_p = r"D:\Facultate\RN\docs\processed\Pneumonia\pneumonia_processed.csv"
    path_proc_t = r"D:\Facultate\RN\docs\processed\Tuberculoza\tuberculoza_processed.csv"

    if not os.path.exists(path_proc_p) or not os.path.exists(path_proc_t):
        print("Eroare: Nu am găsit fișierele în docs/processed. Rulează întâi preprocesarea!")
        return

    # 2. ÎNCĂRCARE DATE
    df_p = pd.read_csv(path_proc_p)
    df_t = pd.read_csv(path_proc_t)

    # 3. FUNCȚIE PENTRU SPLIT ȘI SALVARE SPECIFICĂ
    def split_and_write(df, disease_name):
        # Împărțim datele: 70% Train, 15% Validation, 15% Test
        train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
        val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

        data_map = {
            'train': train_df,
            'validation': val_df,
            'test': test_df
        }

        for stage, data in data_map.items():
            # Construim calea exactă cerută de tine: docs\stage\Disease
            # Exemplu: D:\Facultate\RN\docs\train\Pneumonia
            target_dir = os.path.join(r"D:\Facultate\RN\docs", stage, disease_name)
            os.makedirs(target_dir, exist_ok=True)
            
            save_path = os.path.join(target_dir, f"{disease_name.lower()}_{stage}.csv")
            data.to_csv(save_path, index=False)
            print(f"Salvat în: {save_path}")

    # 4. EXECUTARE DISTRIBUIRE
    print("Începe distribuirea datelor procesate...")
    split_and_write(df_p, "Pneumonia")
    split_and_write(df_t, "Tuberculoza")

    # 5. CREARE SETURI COMBINATE PENTRU MODELE (Necesar pentru Etapa 4)
    # Rețeaua Neuronală are nevoie de un singur fișier amestecat pentru a învăța
    print("\nCreăm fișierele combinate pentru antrenare în folderul data/...")
    for stage in ['train', 'validation', 'test']:
        p_file = os.path.join(r"D:\Facultate\RN\docs", stage, "Pneumonia", f"pneumonia_{stage}.csv")
        t_file = os.path.join(r"D:\Facultate\RN\docs", stage, "Tuberculoza", f"tuberculoza_{stage}.csv")
        
        # Combinăm și amestecăm (Shuffle)
        combined = pd.concat([pd.read_csv(p_file), pd.read_csv(t_file)]).sample(frac=1, random_state=42)
        
        final_data_path = os.path.join(r"D:\Facultate\RN\data", stage)
        os.makedirs(final_data_path, exist_ok=True)
        combined.to_csv(os.path.join(final_data_path, f"{stage}.csv"), index=False)
        print(f"Creat set combinat: {final_data_path}\\{stage}.csv")

if __name__ == "__main__":
    distribute_to_folders()