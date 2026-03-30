import sqlite3

connAll = sqlite3.connect("baza.db")

# sqlite3 can eat shit and die
try:
    # iz nekog razloga sqlite MI NE DOZVOLJAVA da sve tabele lepo kreiram u 
    # jednu connAll.execute() komandu
    # bemti kuj ga izmisli
    connAll.execute('''
        CREATE TABLE IF NOT EXISTS clanovi (
        idClana INTEGER PRIMARY KEY,
        ime TEXT NOT NULL,
        prezime TEXT NOT NULL,
        drzavljanstvo TEXT NOT NULL,
        JMBG INTEGER,
        JMBGequiv INTEGER,
        placenaClanarina BOOLEAN NOT NULL
        )
    ''')

    connAll.execute('''
        CREATE TABLE IF NOT EXISTS zaposleni(
            idZaposlenog INTEGER PRIMARY KEY,
            ime TEXT NOT NULL,
            prezime TEXT NOT NULL,
            drzavljanstvo TEXT NOT NULL,
            JMBG INTEGER,
            JMBGequiv INTEGER,
            datumPocetkaRada DateTime NOT NULL
        )
    ''')
    
    connAll.execute('''
        CREATE TABLE IF NOT EXISTS primerci(
            idPrimerka INTEGER PRIMARY KEY,
            idKnjige INTEGER REFERENCES knjige(idKnjige),
            godinaIzdanja INTEGER NOT NULL,
            izdavackaKuca TEXT NOT NULL
        )
    ''')

    connAll.execute('''
        CREATE TABLE IF NOT EXISTS pozajmice(
            idPozajmice INTEGER NOT NULL,
            idPrimerka INTEGER references primerci(idPrimerka),
            idClana INTEGER references clanovi(idClana),
            idZaposlenog INTEGER references zaposleni(idZaposlenog),
            datumPozajmice DateTime NOT NULL
        )
    ''')


    connAll.commit()
    # S obzirom da kolone ima BRDA, odlučio sam da sve INSERT OR INGORE INTO
    # komande smestim u poseban fajl, zbog lakšeg snalaženja           
    print("Database created successfully.")

except sqlite3.Error as e:
    print(f"An SQLite error occurred: {e}")
    # Rollback changes if an error occurs
    if connAll:
        connAll.rollback() 
