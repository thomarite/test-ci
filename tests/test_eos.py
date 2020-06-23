def test_find_prompt(netmiko_conn):
    assert "r03#" in netmiko_conn.find_prompt()


def test_eapi(eapi_conn):
    assert "cEOSLab" in eapi_conn.enable("show version")[0]["result"]["modelName"]
