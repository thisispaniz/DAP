# DAP

Code for my B.Sc. thesis (Health Informatics, TH Deggendorf): automated scoring of
children's Draw-a-Person (DAP) drawings.

## Data

The drawings are **not included in this repository**. The dataset has no open
license, so it is used for research only and not redistributed here.

1. Download *Draw-a-Person hand-drawn sketches* (Rakhmanov, 2021) from Kaggle:
   https://www.kaggle.com/datasets/lachin007/drawaperson-handdrawn-sketches-by-children
2. Unzip it so the age-group folders sit directly under `data/raw/`:

   ```
   data/raw/4/  data/raw/5/  ...  data/raw/11/
   ```

3. Check the copy:

   ```
   python src/audit_dataset.py
   ```

The dataset contains about 1000 drawings by primary-school children (ages 4–11),
sorted into 8 mental-age classes by professionals.

## Setup (Windows)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Citation

If you use the dataset, cite its author:

Rakhmanov, O., Agwu, N. N., & Adeshina, S. (2020). Experimentation on hand drawn
sketches by children to classify Draw-a-Person test images in psychology.
*Proceedings of the 33rd International FLAIRS Conference*. AAAI Press.

Rakhmanov, O. (2021). *Draw-a-Person hand-drawn sketches* [Data set]. Kaggle.
https://www.kaggle.com/datasets/lachin007/drawaperson-handdrawn-sketches-by-children
