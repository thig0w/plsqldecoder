# -*- coding: utf-8 -*-
def test_decoder_endpoint(client):
    response = client.get(
        "/api/v1/decoder/28734699435745114553445143494439451343314421345532093267"
    )
    assert response.status_code == 200
    assert response.json() == {"pass": "Senhafacil#16"}
