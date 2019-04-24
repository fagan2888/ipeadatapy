import pandas as pd
from .api_call import api_call

def territories():
    """Returns available Ipeadata's territories in the form of a data frame."""
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Territorios"
    return api_call(api)[['TERNOME', 'TERCODIGO', 'NIVNOME', 'TERAREA','TERCAPITAL']].rename(index=str, columns={"TERNOME": "NAME", "TERCODIGO": "ID","NIVNOME": "LEVEL","TERAREA": "AREA", "TERCAPITAL": "CAPITAL"})