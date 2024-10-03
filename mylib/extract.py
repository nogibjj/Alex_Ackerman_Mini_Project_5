"""
Extract a dataset from URL
"""

import requests
import os

# from pathlib import Path

# csv_path = Path("data/ks-projects-201801.csv")

# if test_fig_file_path.exists():
#     test_fig_file_path.unlink()


def extract(
    url="https://github.com/bharatk101/kickstarter_eda/raw/refs/heads/master/ks-projects-201801.csv",
    filepath="ks-projects-201801.csv",
):
    if os.path.exists(
        "Data"
        # )
        #     "/Users/alexackerman/Library/CloudStorage/OneDrive-Personal/MIDS/Data Engineering/Alex_Ackerman_Mini_Project_5/mylib"
    ):
        os.chdir("Data")
    else:
        os.mkdir("Data")
        os.chdir("Data")

    with requests.get(url, timeout=100) as r:
        with open(filepath, "wb") as f:
            f.write(r.content)
    print(filepath)

    return filepath

    # extract()


if __name__ == "__main__":
    # if os.path.exists(
    #     "/Users/alexackerman/Library/CloudStorage/OneDrive-Personal/MIDS/Data Engineering/Alex_Ackerman_Mini_Project_5/mylib"
    # ):
    #     os.chdir(
    #         "/Users/alexackerman/Library/CloudStorage/OneDrive-Personal/MIDS/Data Engineering/Alex_Ackerman_Mini_Project_5/mylib"
    #     )
    # else:
    #     print("Directory does not exist.")

    extract()
