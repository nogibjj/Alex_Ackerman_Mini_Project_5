"""
Transforms and loads data to local SQLite3 database with custom schema
"""

import sqlite3
import csv


# Alex_Ackerman_Mini_Project_5/mylib/ks-projects-201801.csv
def load(
    dataset="../Alex_Ackerman_Mini_Project_5/Data/ks-projects-201801.csv",
):
    # Open the CSV file
    payload = csv.reader(open(dataset, newline="", encoding="utf-8"), delimiter=",")
    # print(*payload)
    conn = sqlite3.connect("../Alex_Ackerman_Mini_Project_5/Data/kickstarter.db")
    c = conn.cursor()

    # ['999987933', 'BioDefense Education Kit', 'Technology', 'Technology', 'USD', '2016-02-13', '15000.00', '2016-01-13 18:13:53', '200.00', 'failed', '6', 'US', '200.00', '200.00', '15000.00']
    # Create a new table based on the provided schema
    c.execute("DROP TABLE IF EXISTS kickstarter")
    c.execute(
        """
        CREATE TABLE kickstarter (
            ID INTEGER,
            name TEXT,
            category TEXT,
            main_category TEXT,
            currency TEXT,
            deadline TEXT,
            goal FLOAT,
            launched TEXT,
            pledged FLOAT,
            state TEXT,
            backers INTEGER,
            country TEXT,
            usd_pledged FLOAT,
            usd_pledged_real FLOAT,
            usd_goal_real FLOAT
        )
        """
    )

    # Insert the data into the table
    c.executemany(
        """
        INSERT INTO kickstarter
        (ID, name, category, main_category, currency, deadline, goal, launched, pledged,
         state, backers, country, usd_pledged, usd_pledged_real, usd_goal_real)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        payload,
    )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    return "../Alex_Ackerman_Mini_Project_5/Data/kickstarter.db"


if __name__ == "__main__":
    load()
