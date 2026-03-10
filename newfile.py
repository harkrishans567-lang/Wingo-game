import mysql.connector

print("---------------------------------")
print("        BDG WIN RESULT CHECKER")
print("---------------------------------")

db = mysql.connector.connect(
    host="your_host",
    user="your_db_user",
    password="your_password",
    database="bdg_game"
)

cursor = db.cursor()

while True:
    period = input("\nEnter Period Number (or type exit): ")

    if period.lower() == "exit":
        print("Closing checker...")
        break

    query = "SELECT number, colour FROM wingo_results WHERE period=%s"
    cursor.execute(query, (period,))
    result = cursor.fetchone()

    if result:
        print("\n------ RESULT ------")
        print("Period :", period)
        print("Number :", result[0])
        print("Colour :", result[1])
        print("--------------------")
    else:
        print("Result not found.")