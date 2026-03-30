import sqlite3

connAll = sqlite3.connect("baza.db")

try:
    # Insert Knjige
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (1, "Hamlet", "Šekspir, Viljem"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (2, "Faust", "Gete, Johan Volfgang"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (3, "Čekajući Godoa", "Beket, Semjuel"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (4, "Ime Ruže", "Eko, Umberto"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (5, "Majstor i Margarita", "Bulgakov, Mihail"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (6, "Bašta Sljezove Boje", "Ćopić, Branko"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (7, "Prokleta Avlija", "Andrić, Ivo"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (8, "Stranac", "Kami, Alber"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (9, "Mit o Sizifu", "Kami, Alber"))
    connAll.execute("INSERT OR IGNORE INTO knjige (idKnjige, naziv, autor) VALUES (?, ?, ?)", 
                    (10, "Zločin i Kazna", "Dostojevski, Fjodor"))

    print("Book list successfully inserted.")

    # Clanovi
    connAll.execute("INSERT OR IGNORE INTO clanovi (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, placenaClanarina) values (?, ?, ?, ?, ?, ?, ?)", 
                    (1, "Ivan", "Stefanović", "Srbija", 1506985782541, None, 1))
    connAll.execute("INSERT OR IGNORE INTO clanovi (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, placenaClanarina) values (?, ?, ?, ?, ?, ?, ?)", 
                    (2, "Igor", "Gavrilović", "Srbija", 2104001771235, None, 0))
    connAll.execute("INSERT OR IGNORE INTO clanovi (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, placenaClanarina) values (?, ?, ?, ?, ?, ?, ?)", 
                    (3, "Milena", "Tomić", "Srbija", 1111011746785, None, 1))
    connAll.execute("INSERT OR IGNORE INTO clanovi (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, placenaClanarina) values (?, ?, ?, ?, ?, ?, ?)", 
                    (4, "Mario", "Bianchi", "Italija", None, 784561, 0))
    connAll.execute("INSERT OR IGNORE INTO clanovi (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, placenaClanarina) values (?, ?, ?, ?, ?, ?, ?)", 
                    (5, "Miona", "Ilov", "Srbija", 2903004489840, None, 1))

    print("Members successfully inserted.")

    # Zaposleni
    connAll.execute("INSERT OR IGNORE INTO zaposleni (idZaposlenog, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, datumPocetkaRada) values (?, ?, ?, ?, ?, ?, ?)",
                    (1, "Dimitrije", "Marjanović", "Srbija", 1506006751575, None, "2024-05-22"))
    connAll.execute("INSERT OR IGNORE INTO zaposleni (idZaposlenog, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, datumPocetkaRada) values (?, ?, ?, ?, ?, ?, ?)",
                    (2, "Stevan", "Mitrović", "Srbija", 1010007755575, None, "2024-12-02"))

    print("Staff successfully inserted.")
    
    # Primerci
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (1, 1, 2009, "Laguna"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (2, 1, 2009, "Laguna"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (3, 2, 2019, "Vulkan"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (4, 4, 2007, "Zavod"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (5, 5, 2018, "Narodna knjiga"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (6, 4, 1999, "Laguna"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (7, 2, 1989, "Narodna knjiga"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (8, 6, 2014, "Laguna"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (9, 7, 2014, "Vulkan"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (10, 7, 2009, "Laguna"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (11, 5, 2025, "Vulkan"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (12, 8, 2025, "Vulkan"))         
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (13, 9, 2025, "Laguna"))
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (14, 9, 1989, "Zavod"))                
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (15, 10, 1988, "Zavod"))             
    connAll.execute("INSERT OR IGNORE INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)",
                    (16, 10, 1975, "Nepoznat"))

    print("Books successfully inserted.")

    # I, najzad, pozajmice
    connAll.execute("INSERT OR IGNORE INTO pozajmice (idPozajmice, idPrimerka, idClana, idZaposlenog, datumPozajmice) values (?, ?, ?, ?, ?)",
                    (1, 6, 3, 1, "2026-03-24"))
    connAll.execute("INSERT OR IGNORE INTO pozajmice (idPozajmice, idPrimerka, idClana, idZaposlenog, datumPozajmice) values (?, ?, ?, ?, ?)",
                    (2, 6, 4, 2, "2026-03-24"))
    connAll.execute("INSERT OR IGNORE INTO pozajmice (idPozajmice, idPrimerka, idClana, idZaposlenog, datumPozajmice) values (?, ?, ?, ?, ?)",
                    (3, 2, 5, 1, "2026-03-24"))

    print("Borrowed books successfully inserted.")
    connAll.commit()

except sqlite3.Error as e:
    print(f"An SQLite error occurred: {e}")
    # Rollback changes if an error occurs
    if connAll:
        connAll.rollback()
                    