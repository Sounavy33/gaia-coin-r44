from scripts.transcription_pipeline import reduce_text, translate_stub


def test_reduce_text_simple():
    text = 'Olá. Isto é uma frase. Outra frase importante.'
    out = reduce_text(text, 2)
    assert 'Olá' in out or len(out) > 0


def test_translate_stub():
    t = 'Olá mundo'
    tr = translate_stub(t, 'en')
    assert tr.startswith('[en]')
