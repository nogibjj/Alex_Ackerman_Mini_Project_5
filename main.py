"""
Main cli or app entry point
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import queryCreate, queryRead, queryUpdate, queryDelete

# Extract
extract()

# Transform and Load
load()

# Query
queryCreate()
queryRead()
queryUpdate()
queryDelete()


def main_result():
    results = {
        "extract_to": extract(),
        "transform_db": load(),
        "create": queryCreate(),
        "read": queryRead(),
        "update": queryUpdate(),
        "delete": queryDelete(),
    }

    return results


main_result()
