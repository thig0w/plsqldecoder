from src.plsqldecoder.api.decoder.business import decode


def test_db_connection():
    assert decode() == "Senhafacil#16"
