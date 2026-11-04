"""Smoke test: the package and the GUI layer can be imported."""


def test_imports():
    import CBR
    from CBR import RecommenderSystem, createRS, Cas, Problem, Indexacio
    import us_recomender

    assert callable(us_recomender.recomana)
    assert callable(us_recomender.revise_retain)
