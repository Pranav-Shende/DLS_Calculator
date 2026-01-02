import pandas as pd
odi_df = pd.read_csv("dls_odi.csv").set_index("Overs_Available")
t20_df = pd.read_csv("dls_t20.csv").set_index("Overs_Available")
def get_resource(overs_left, wickets_lost, fmt):
    fmt = fmt.lower()
    table = odi_df if fmt == "odi" else t20_df
    try:
        return float(table.loc[overs_left, str(wickets_lost)])
    except KeyError:
        raise ValueError("Invalid overs/wickets combination")