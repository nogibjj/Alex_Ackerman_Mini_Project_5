import sqlite3


# Function to insert a new project into the kickstarter table
def queryCreate():
    conn = sqlite3.connect("kickstarter.db")
    cursor = conn.cursor()
    # Insert execution (example project details provided)
    cursor.execute(
        """
        INSERT INTO kickstarter (name, category, main_category, currency, deadline, goal, launched, pledged, state, backers, country, usd_pledged, usd_pledged_real, usd_goal_real)
        VALUES ('Sample Project', 'Technology', 'Tech', 'USD', '2024-12-31', 10000, '2024-01-01', 5000, 'live', 100, 'US', 5000, 5000, 10000)
        """
    )
    conn.commit()
    conn.close()
    return "Create Success"


# Function to read data from the kickstarter table
def queryRead():
    conn = sqlite3.connect("kickstarter.db")
    cursor = conn.cursor()
    # Read execution
    cursor.execute("SELECT * FROM kickstarter LIMIT 10")
    # rows = cursor.fetchall()
    conn.close()
    # return rows
    return "Read Success"


# Function to update an entry in the kickstarter table
def queryUpdate():
    conn = sqlite3.connect("kickstarter.db")
    cursor = conn.cursor()
    # Update execution (updating an example project)
    cursor.execute("UPDATE kickstarter SET pledged = 6000 WHERE ID = 1")
    conn.commit()
    conn.close()
    return "Update Success"


# Function to delete an entry from the kickstarter table
def queryDelete():
    conn = sqlite3.connect("kickstarter.db")
    cursor = conn.cursor()
    # Delete execution
    cursor.execute("DELETE FROM kickstarter WHERE ID = 1")
    conn.commit()
    conn.close()
    return "Delete Success"


# Main program execution
if __name__ == "__main__":
    print(queryCreate())
    print(queryRead())
    print(queryUpdate())
    print(queryDelete())


# """
# Query the database
# """
# import sqlite3


# def querycreate():
#     conn = sqlite3.connect("kickstarter.db")
#     cursor = conn.cursor()
#     # create execution
#     cursor.execute(
#         "INSERT INTO rainfall (Date,POONDI,CHOLAVARAM,REDHILLS,CHEMBARAMBAKKAM) VALUES(31-12-2003,1,1,1,1)"
#     )
#     conn.close()
#     return "Create Success"


# def queryRead():
#     conn = sqlite3.connect("rainfall.db")
#     cursor = conn.cursor()
#     # read execution
#     cursor.execute("SELECT * FROM rainfall LIMIT 10")
#     conn.close()
#     return "Read Success"


# def queryUpdate():
#     conn = sqlite3.connect("rainfall.db")
#     cursor = conn.cursor()
#     # update execution
#     cursor.execute("UPDATE rainfall SET POONDI = 1 WHERE id = 1 ")
#     conn.close()
#     return "Update Success"


# def queryDelete():
#     conn = sqlite3.connect("rainfall.db")
#     cursor = conn.cursor()
#     # delete execution
#     cursor.execute("DELETE FROM rainfall WHERE id = 3")
#     conn.close()
#     return "Delete Success"


# if __name__ == "__main__":
#     querycreate()
#     queryRead()
#     queryUpdate()
#     queryDelete()
