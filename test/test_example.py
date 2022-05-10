import demo as s

def test_replace():
    assert "Hola como estas| Esta es una prueba con|" == s.replace("Hola como estas? Esta es una prueba con.")

def test_solution():
    assert 7 == s.solution("Hola como estas? Esta es una prueba con. Esta es una mas larga mas larga..?.!.")

def test_platform():
    assert 2 == s.solution("Forget  CVs..Save time . x x")
