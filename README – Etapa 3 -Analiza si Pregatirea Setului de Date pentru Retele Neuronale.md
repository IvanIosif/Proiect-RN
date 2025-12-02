# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Ivan Iosif Sebastian  
**Data:** 20.11.2025 

---

## Introducere

Proiectul presupune dezvolarea unui Sistem cu Inteligenta Artifiiala bazat pe Retele Neuronale, capabil sa identifice boli pornind de la imagii medicale (radiografii) si text.
  Sistemul utilizeaza o retea neuronala convolutionala pentru analiza imaginilor si un model de procesare a limbajului natural, pentru interpretarea simptomelor descries in limbaj comun.
  Scopul sau este de oferi un diagnostic probabil si un grad de incredere asociat fiecarei predictii, sprijinind astfel medicii si pacientii in procesul de identificare timpurie a afectiunilor.
  Acest proiect combina metodele de invatare profunda si metodele de clasificare, astfel integrandu-se in domeniul Sistemelor de Inteligenta Artificiala. Aplicatia astfel va avea capacitatile de intelegere, analiza si invatare din date complexe 
  Proiectul isi propune sa contriibuie la dezvoltarea diagnosticarilor cat mai precise  din domeniul medical, capabil sa reduca timpul de diagnosticare, sa creasca acuratetea si sa ofere sprijin specialistilor din sanatate

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** dataset public https://data.mendeley.com/datasets/9d55cttn5h/1
* **Modul de achiziție:**  Fișier extern Source link: https://data.mendeley.com/public-files/datasets/9d55cttn5h/files/de09b715-f8cb-457f-95dd-ced33e18b634/file_downloaded
* **Perioada / condițiile colectării:** Date colectate din spitale, pentru clasificarea pneumoniei.

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** Număr total imagini: 1100 Pneumonie, 1250 Normale
* **Număr de caracteristici (features):** Tipuri de date: imagini grayscale / RGB
* **Tipuri de date: Imagini
* **Format fișiere:** JPG

### 2.3 Descrierea fiecărei caracteristici

Pentru acest dataset nu există features tabulare. Singurele caracteristici sunt pixelii imaginilor, care sunt matrice de valori între 0–255 (sau 0–1 după normalizare).

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

Distribuția claselor: 2 tipuri de clase, cele cu Pneumonie si Normale

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă** 0
* **Detectarea valorilor inconsistente sau eronate** toate imaginile sunt in regula
* **Identificarea caracteristicilor redundante sau puternic corelate** imagini blurate / alb-negru / expunere slabă

dimensiuni neuniforme

### 3.3 Probleme identificate

* Distribuția claselor este aproape echilibrată (1100 vs 1250)
* Variabilitate în dimensiunea imaginilor, a fost necesara redimensionarea imagninilor
* Contrast diferit, a fost necesara clasa CLAHE pentru contrastarea cat mai uniforma a culorilor din imagini

---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* **Eliminare duplicatelor** nu există,
* 
### 4.2 Transformarea caracteristicilor

* **Normalizare:** efectuat
* **Redimensionare:** efectuat

### 4.3 Structurarea seturilor de date

**Împărțire recomandată:**
* 70–80% – train
* 10–15% – validation
* 10–15% – test

**Principii respectate:**
* Stratificare pentru clasificare
* Fără scurgere de informație (data leakage)
* Statistici calculate DOAR pe train și aplicate pe celelalte seturi

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train/val/test în foldere dedicate
* Parametrii de preprocesare în `config/preprocessing_config.*` (opțional)

---

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & transformate
* `data/train/`, `data/validation/`, `data/test/` – seturi finale
* `src/preprocessing/` – codul de preprocesare
* `data/README.md` – descrierea dataset-ului

---

##  6. Stare Etapă (de completat de student)

- [ ] Structură repository configurată
- [ ] Dataset analizat (EDA realizată)
- [ ] Date preprocesate
- [ ] Seturi train/val/test generate
- [ ] Documentație actualizată în README + `data/README.md`

---
