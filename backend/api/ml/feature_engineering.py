def extract_features(data: dict):
    return [[
        data.get("engine_temp", 0),
        data.get("vibration", 0),
        data.get("oil_pressure", 0)
    ]]
