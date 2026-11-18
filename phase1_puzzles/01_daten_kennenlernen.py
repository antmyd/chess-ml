"""
Phase 1 · Schritt 1: Die Daten kennenlernen
===========================================
Ziel: Du verstehst, was in den Daten steckt, BEVOR du irgendein Modell baust.
(Data-Science-Prozess Schritt 3: "Daten verstehen")

Schreib den Code unter jedes TODO selbst. Ausführen: python phase1_puzzles/01_daten_kennenlernen.py
"""
import pandas as pd
import matplotlib.pyplot as plt
import chess

DATA = "data/lichess_db_puzzle.csv.zst"

# TODO 1: Lade die ersten 50_000 Zeilen mit pd.read_csv (Tipp: Parameter nrows).
#         Gib .shape, .head() und .dtypes aus.
data = pd.read_csv(DATA, nrows=50000)
print("SHAPE:")
print(data.shape)
print("HEAD:")
print(data.head())
print("DTYPES:")
print(data.dtypes)

# TODO 2: Schau dir die Spalte "Rating" an: .describe() und ein Histogramm (plt.hist, bins=50).
#   ❓ Vorher raten: Zwischen welchen Werten liegen die meisten Puzzles?
print("DESCRIBE")
print(data.describe())

print(plt.hist(data["Rating"], bins=50))
plt.show()
# TODO 3: Die Spalte "Themes" enthält mehrere Themen, getrennt durch Leerzeichen.
#         Zähle, welche 15 Themen am häufigsten vorkommen.
#         Tipp: .str.split() und dann .explode() und .value_counts()
themen_listen = data["Themes"].str.split()     # jede Zeile wird zu einer Liste: [fork, middlegame, short]
alle_themen = themen_listen.explode()          # jedes Thema bekommt eine eigene Zeile
top15 = alle_themen.value_counts().head(15)    # zählen, absteigend sortiert, die ersten 15
print(top15)

# TODO 4: Nimm die FEN der ersten Zeile und erzeuge ein Brett:  board = chess.Board(fen)
#         print(board) zeigt es als Text an. Wer ist am Zug (board.turn)?
#         Achtung: Laut Lichess ist der ERSTE Zug in "Moves" der Zug des Gegners,
#         erst danach beginnt die eigentliche Aufgabe. Spiel ihn mit board.push_uci(...) und print erneut.
erstes_rating = data["FEN"].iloc[0]
print(erstes_rating)

board = chess.Board(erstes_rating)

erster_zug = data["Moves"].iloc[0].split()[0]
print(erster_zug) 
print(board)
print()
board.push_uci(erster_zug)
print(board)
print("Weiß" if board.turn == chess.WHITE else "Schwarz")

# TODO 5: Länge der Lösung = Anzahl Züge in "Moves". Erzeuge eine neue Spalte "n_moves".
#   ❓ Vorher raten: Sind Puzzles mit mehr Zügen schwerer? Prüfe es mit df.groupby("n_moves")["Rating"].mean()
data["n_moves"] = data["Moves"].str.split().str.len()
print(data.groupby("n_moves")["Rating"].mean())

print(data.head())

# ❓ Denkfrage für später (schon mal notieren!):
#   Wir wollen "Rating" vorhersagen. Welche Spalten dürfen wir als Features NICHT benutzen,
#   weil das Data Leakage wäre oder weil sie erst NACH dem Lösen durch viele Spieler entstehen?
