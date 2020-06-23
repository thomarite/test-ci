def test_ssh(netmiko_conn):
    assert "r03#" in netmiko_conn.find_prompt()


def test_eapi(eapi_conn):
    assert "cEOSLab" in eapi_conn.enable("show version")[0]["result"]["modelName"]


def test_json(json_conn):
    assert "cEOSLab" in json_conn.runCmds(1, ["show version"], "json")[0]["modelName"]
