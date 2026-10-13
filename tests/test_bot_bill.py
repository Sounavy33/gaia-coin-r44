from scripts.bot_bill import build_response_for_text, detect_language, parse_command


def test_detect_language_portuguese():
    assert detect_language('olá Bill, me ajuda com o status') == 'pt'


def test_detect_language_english():
    assert detect_language('hello Bill, please help me') == 'en'


def test_parse_command_help_and_status():
    assert parse_command('/bill help') == 'help'
    assert parse_command('@bill status') == 'status'
    assert parse_command('bill explain gaia') == 'explain'


def test_build_text_response_contains_project_name():
    text = build_response_for_text('/bill status')
    assert 'GaIA Coin R44' in text


def test_explain_response_in_portuguese():
    text = build_response_for_text('/bill explain borda')
    assert 'borda' in text.lower() or 'GaIA Coin R44' in text
