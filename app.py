from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import date
import sqlite3

app = Flask(__name__)
database = 'baza.db'

def get_db_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home")
def show_main():
    return index()

@app.route("/knjige", methods=["GET", "POST"])
def books():
    conn = get_db_connection()
    data = conn.execute('''SELECT p.idPrimerka, p.idKnjige, k.naziv, k.autor, p.godinaIzdanja, p.izdavackaKuca 
                        FROM primerci AS p JOIN knjige AS k 
                        ON p.idKnjige = k.idKnjige''').fetchall()

    if request.method == "POST":
        naziv = request.form.get('nazivKnjige')
        autor = request.form.get('imeAutora')
        godina = request.form.get('godIzdanja')
        kuca = request.form.get('izdavackeKuce')

        if not naziv or not autor or not godina or not kuca:
            return render_template('knjige.html', books=data), 400

        cursor = conn.execute('SELECT MAX(idPrimerka) FROM primerci')
        last_id = cursor.fetchone()[0]
        idPrimerka = 1 if last_id is None else last_id + 1

        cursor = conn.execute('SELECT COUNT(*) FROM knjige WHERE naziv = ?', (naziv, ))
        doesBookExist = cursor.fetchone()[0]
        if doesBookExist > 0:
            cursor = conn.execute('SELECT idKnjige FROM knjige WHERE naziv = ?', (naziv, ))
            bookLastId = cursor.fetchone()[0]
        else:
            cursor = conn.execute('SELECT MAX(idKnjige) FROM knjige')
            bookLastId = cursor.fetchone()[0] + 1
            conn.execute('''INSERT INTO knjige (idKnjige, naziv, autor) values (?, ?, ?)''', 
                        (bookLastId, naziv, autor))

        conn.execute('''INSERT INTO primerci (idPrimerka, idKnjige, godinaIzdanja, izdavackaKuca) values (?, ?, ?, ?)''',
                    (idPrimerka, bookLastId, godina, kuca))
        
        conn.commit()
        conn.close()
        return redirect(url_for('books'))

    conn.close()
    return render_template('knjige.html', books=data)

@app.route("/clanovi", methods=["GET", "POST"])
def clanovi():
    conn = get_db_connection()

    if request.method == "POST":

        # Checks for membership payment update
        selected = request.form.getlist('selectedUpdateClanarina')
        if selected:
            for mId in selected:
                conn.execute(
                    '''UPDATE clanovi SET placenaClanarina = 1 WHERE idClana = ?''',
                    (mId,)
                )
            conn.commit()
            conn.close()
            return redirect(url_for('clanovi'))

        # Checks for insert
        ime = request.form.get('insertIme')
        if ime:
            prezime = request.form.get('insertPrezime')
            drzavljanstvo = request.form.get('insertNation')

            if drzavljanstvo == 'Srbija':
                JMBG = request.form.get('insertJMBG')
                JMBGequiv = None
            else:
                JMBGequiv = request.form.get('insertJMBGequiv')
                JMBG = None

            cursor = conn.execute('SELECT MAX(idClana) FROM clanovi')
            last_id = cursor.fetchone()[0]
            idClana = 1 if last_id is None else last_id + 1

            conn.execute(
                '''INSERT INTO clanovi 
                (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, placenaClanarina) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (idClana, ime, prezime, drzavljanstvo, JMBG, JMBGequiv, 0)
            )

            conn.commit()
            conn.close()
            return redirect(url_for('clanovi'))

        # Checks for delete
        action = request.form.get("action")
        if action == "delete":
            delete_id = request.form.get("deleteId")

            conn.execute(
                'DELETE FROM clanovi WHERE idClana = ?',
                (delete_id,)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('clanovi'))
    data = conn.execute('''
        SELECT idClana, 
               concat(ime, ' ', prezime) AS ime, 
               drzavljanstvo, JMBG, JMBGequiv, placenaClanarina 
        FROM clanovi
    ''').fetchall()

    conn.close()
    return render_template('clanovi.html', members=data)


@app.route("/zaposleni")
def show_slaves():
    conn = get_db_connection()
    data = conn.execute('''SELECT idZaposlenog, concat(ime, ' ', prezime) AS ime, drzavljanstvo, JMBG, JMBGequiv, datumPocetkaRada 
                        FROM zaposleni''').fetchall()
    conn.close()
    return render_template('zaposleni.html', slaves=data)

# Y'know, I'm nearing the end of this school project, and I think i've developed Stockholm Syndrome for full-stack work
# (don't know how much of this can be counted as full stack but still)
@app.route("/pozajmice", methods=["GET", "POST"])
def pozajmice():
    conn = get_db_connection()

    # This is probably the most  dogshit SQL code I've ever written
    fuck1 = conn.execute("SELECT idClana,  ime || ' ' || prezime AS imeClana FROM clanovi")
    fuck2 = conn.execute("SELECT idZaposlenog, ime || ' ' || prezime AS imeRadnika FROM zaposleni")
    fuck3 = conn.execute("SELECT idKnjige, naziv FROM knjige")
    fuck4 = [dict(row) for row in conn.execute("SELECT idPrimerka, idKnjige FROM primerci").fetchall()]

    if request.method == "POST":
        idClana = request.form.get('memberID')
        idKnjige = request.form.get('bookID')
        idZap = request.form.get('slaveID')
        idPrimerka = request.form.get('copyID')
        idPoz = request.form.get('deleteID')

        # If insert into, then all of these must be present
        if idClana and idKnjige and idZap and idPrimerka:
            datum = date.today()
            cursor = conn.execute("SELECT MAX(idPozajmice) FROM pozajmice")
            idPoz = cursor.fetchone()[0] + 1

            conn.execute("INSERT INTO pozajmice (idPozajmice, idPrimerka, idClana, idZaposlenog, datumPozajmice) values (?, ?, ?, ?, ?)",
                        (idPoz, idPrimerka, idClana, idZap, datum))
            conn.commit()
            conn.close()
            return redirect(url_for('pozajmice'))
        
        # Else it just assumes delete method
        # This is a very bad implementation, I know
        # Shut up
        elif idPoz:
            conn.execute("DELETE FROM pozajmice WHERE idPozajmice = ?", (idPoz, ))
            conn.commit()
            conn.close()
            return redirect(url_for('pozajmice'))

        
    data = conn.execute('''SELECT 
                        p.idPozajmice,
                        pr.idPrimerka,
                        k.naziv,
                        c.ime || ' ' || c.prezime AS imeClana,
                        z.ime || ' ' || z.prezime AS imeRadnika,
                        pr.godinaIzdanja,
                        pr.izdavackaKuca,
                        p.datumPozajmice
                            FROM pozajmice p
                            JOIN primerci pr ON p.idPrimerka = pr.idPrimerka
                            JOIN knjige k ON pr.idKnjige = k.idKnjige
                            JOIN clanovi c ON p.idClana = c.idClana
                            JOIN zaposleni z ON p.idZaposlenog = z.idZaposlenog''').fetchall()

    return render_template('pozajmice.html', dugovi=data, one=fuck1, two=fuck2, tre=fuck3, fou=fuck4)

def GetDbAll():
    return sqlite3.connect("baza.db")


if __name__ == "__main__":
    app.run(debug = True)

