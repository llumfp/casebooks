"""End-to-end test: one predefined reader through the whole CBR cycle.

Same calls as app.py: recomana() runs Retrieve + Reuse, revise_retain() runs
Revise (with the user's ratings), Retain, Maintain if due, and saves the model.
It works on a copy of the model in a temporary folder, so the real
models/recomanador.pkl is never modified.
"""
import hashlib
import shutil

import us_recomender
from CBR import RecommenderSystem, cargar_diccionario
from us_recomender import recomana, revise_retain

# Same format the GUI builds: order of the 10 genres (1 = favourite),
# then mean book length, books read in 10 years and how demanding (avg rating).
READER = ["1", "2", "3", "10", "4", "5", "6", "9", "7", "8", "300", "40", "3.0"]
RATINGS = [5, 3, 0]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_full_cycle(model_path, tmp_path, monkeypatch):
    original_hash = sha256(model_path)

    # Work on a copy of the model: recomana() loads it and revise_retain() saves it.
    model_copy = tmp_path / "recomanador.pkl"
    shutil.copy(model_path, model_copy)
    monkeypatch.setattr(us_recomender, "MODEL_PATH", model_copy)

    # Run from an unrelated folder: paths must not depend on the working directory.
    monkeypatch.chdir(tmp_path)
    catalogue = cargar_diccionario()

    # Retrieve + Reuse
    books, rs, newcas, casos, dicc_most_sim, cas_dists, paths = recomana(READER)

    assert len(books) == 3
    assert len(set(books)) == 3
    assert all(book in catalogue for book in books)
    assert len(casos) == rs.indexacio.casesxleaf

    # Revise (user ratings) + Retain + Maintain + save
    revise_retain(rs, newcas, casos, dicc_most_sim, cas_dists, paths, True, RATINGS)

    assert newcas.avaluacio == RATINGS
    saved = RecommenderSystem.load(model_copy)
    assert isinstance(saved, RecommenderSystem)

    # The real model is untouched.
    assert sha256(model_path) == original_hash
