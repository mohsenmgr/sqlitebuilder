import sqlite3

# List of names you want to insert into the database
names_to_insert = [
    "PC2", "PC1 / PC1_NEG", "GENC", "UFF2", "ILLC", "GENB", "UFF1", "ILLB",
    "ORD_SEZ", "FV_ABC", "ORD_FRAZ", "Q_TRACH", "PANTER_44", "Q_PANTER",
    "TESS_Q_COMP", "UFF3", "GEN_D1", "FV_D2E", "Q_MN", "PC3", "Q_GF",
    "Q_REF", "FIL_Q_COMP", "L1_NO_UPS", "L2_NO_UPS", "L3_NO_UPS", "L1_UPS",
    "L2_UPS", "L3_UPS", "L1_BOB", "L2_BOB", "L5", "L6", "Q_CAP", "L_RS",
    "Q_M-H", "FV_M-H", "C_WC", "Q_PM", "CONV_Q_COMP", "TESTA2", "C1", "C2",
    "C3", "TESTA1", "TERMOFIX", "ILL_M-H", "VERIFICA3", "VERIFICA1", "RIP1"
]

def create_table():
    # Connect to the database or create it if it doesn't exist
    conn = sqlite3.connect('sqlite_database.db')
    cursor = conn.cursor()

    # Create the 'lines' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS lines (
                        name TEXT PRIMARY KEY
                    )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_names(names):
    # Connect to the database or create it if it doesn't exist
    conn = sqlite3.connect('sqlite_database.db')
    cursor = conn.cursor()

    # Insert each name into the 'lines' table
    for name in names:
        try:
            cursor.execute("INSERT INTO lines (name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"Name '{name}' already exists in the database. Skipping...")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    insert_names(names_to_insert)
