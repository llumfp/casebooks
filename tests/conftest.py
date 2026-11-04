"""Shared test setup.

Puts the repo root on sys.path, so the tests can `import CBR` and
`import us_recomender` however pytest is launched. No os.chdir is needed:
the code resolves its data and model paths from the package itself
(CBR/constants.py), not from the working directory.
"""
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))


@pytest.fixture
def model_path() -> Path:
    """Path of the saved recommender."""
    from CBR.constants import MODELS_DIR

    path = MODELS_DIR / "recomanador.pkl"
    if not path.is_file():
        pytest.fail(f"{path} not found")
    return path
