from unittest.mock import MagicMock, patch

import server


def test_listar_ofertas_de_placas_monta_query_certa():
    fake_cur = MagicMock()
    fake_cur.fetchall.return_value = [{"fornecedor": "ACME", "potencia_wp": 600}]

    with patch("server.get_cursor") as mock_get_cursor:
        mock_get_cursor.return_value.__enter__.return_value = fake_cur
        resultado = server.listar_ofertas_de_placas(potencia_minima_wp=500)

    assert resultado == [{"fornecedor": "ACME", "potencia_wp": 600}]
    fake_cur.execute.assert_called_once()
    params = fake_cur.execute.call_args[0][1]
    assert params["potencia_minima_wp"] == 500
