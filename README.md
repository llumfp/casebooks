# casebooks — a case-based book recommender

A **Case-Based Reasoning (CBR)** system that recommends three books to a reader
from a short description of their tastes (preferred genres, book length,
how demanding they are with ratings). It learns from the feedback of each new
user.

Project for the *Knowledge-Based Systems* course (SBC), Universitat Politècnica
de Catalunya, 2023 — team of four.

## How it works

The system follows the classic CBR cycle. Each phase is one module in
[`CBR/fases/`](CBR/fases):

| Phase | Module | What it does |
|---|---|---|
| Retrieve | `retrieve.py` | Walks a binary tree index built with recursive KMeans down to a leaf (completed with its sibling if it has too few cases) and returns the 44 most similar cases. |
| Reuse | `reuse.py` | Scores every book of the retrieved cases by its rating, weighted by similarity `1 / (distance + 1)`, and keeps the top three. |
| Revise | `revise.py` | Gets the ratings of the three books, from the user or from an XGBoost model acting as a simulated user, and updates the utility of the cases used. |
| Retain | `retain.py` | Decides whether the new case is stored, merged or discarded. |
| Maintenance | `maintenance.py` | Every 100 changes, checks retrieval time and index size; if needed, rebuilds the tree keeping only the useful cases. |

The data model (`Problem`, `Cas`) and the tree index live in
[`CBR/cases/`](CBR/cases). Domain parameters (genres, length and rating ranges)
are centralised in [`CBR/constants.py`](CBR/constants.py).

## Repository layout

```
casebooks/
├── CBR/              # the CBR library (cases/, fases/, constants, recommender)
├── app.py            # Streamlit GUI
├── us_recomender.py  # glue between the GUI and the recommender
├── data/             # books and generated user cases (CSV / dict)
├── models/           # trained recommender and XGBoost simulated user (.pkl)
├── experiments/      # scripts and notebooks used to tune the system
├── images/           # plots from the experiments
├── docs/             # assignment statement and final report
└── tests/            # pytest suite, run by GitHub Actions on every push
```

## Getting started

Requires Python 3.12 (tested).

```bash
git clone https://github.com/llumfp/casebooks.git
cd casebooks
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the GUI

```bash
streamlit run app.py
```

### Run the tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

## Data and model

- `data/genres_pages_x_books.csv` — book catalogue (genres, pages, rating).
- `data/problems4000_not_0_0_0.csv` — synthetic user cases used to build the case base.
- `data/books_dict.txt` — book id → title lookup.
- `data/problems40000.csv`, `data/problems8000.csv` — larger sets of synthetic users, used to train the XGBoost model.
- `models/recomanador.pkl` — trained recommender (case base, tree index and
  scaler). It is versioned so the GUI works right after cloning; the GUI updates
  it as users give feedback (Revise / Retain), so after using it `git status`
  shows it as modified (`git restore models/recomanador.pkl` to go back).
  To rebuild it from `data/`, run `python -m experiments.build_model`.
- `models/xgb_model.pkl` — XGBoost model that predicts ratings; used as a
  simulated user in the experiments and when a GUI user does not rate the books.

## Experiments

The scripts and notebooks in `experiments/` were used to choose the number of
cases per leaf, measure redundancy and visualise the case space. They are
exploration only: nothing in `CBR/` or `app.py` imports them. Results are in
`images/` and in the report (`docs/`).

Run the scripts from the repo root as modules, so that `CBR` can be imported
and the plots land in `images/`:

```bash
python -m experiments.casesxleaf
```

The data-preparation notebooks (`filtering.ipynb`, `model_xgb.ipynb`) document
how the data and the XGBoost model were produced; they need the raw dataset,
which is not included.

## License

Public domain ([Unlicense](LICENSE)).

