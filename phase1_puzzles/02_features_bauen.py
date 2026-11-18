"""
Phase 1 · Schritt 2: Features bauen
===================================
Ziel: Aus FEN und Zügen eigene Zahlen-Spalten (Features) machen, mit denen ein Modell
später das Rating vorhersagen kann. Ein Modell kann mit dem Text "r6k/pp2r2p/..." nichts anfangen,
aber mit Zahlen wie "Materialvorteil = +3".
(Data-Science-Prozess Schritt 4: Datenaufbereitung, nur Berechnungen INNERHALB einer Zeile)

Am Ende speicherst du eine Tabelle mit deinen Features. Die brauchen wir in Schritt 03.
"""
import pandas as pd
import chess

DATA = "data/lichess_db_puzzle.csv.zst"

# TODO 1: Lade wieder 50_000 Zeilen und erzeuge "n_moves" wie in 01.
#         Gib aus, wie oft jeder Wert vorkommt: .value_counts().sort_index()
#   ❓ Vorher raten: Fällt dir an den Werten etwas auf? Warum ist das so?
#      (Tipp: Wer spielt den ersten Zug, und wer den letzten?)


# TODO 2: Baue eine Spalte "n_loesungszuege" = Anzahl der Züge, die DU als Löser selbst spielen musst.
#         Tipp: Das ist eine einfache Rechnung mit n_moves, kein .apply nötig.


# TODO 3: Schreib eine Funktion  material(fen)  die den Materialstand berechnet.
#         Figurenwerte: Bauer=1, Springer=3, Läufer=3, Turm=5, Dame=9, König=0
#         Tipp 1: Der erste Teil der FEN (fen.split()[0]) enthält die Figuren.
#                 GROSSBUCHSTABEN = Weiß, kleinbuchstaben = Schwarz. Ziffern = leere Felder, "/" = neue Reihe.
#         Tipp 2: Ein Dictionary {"p": 1, "n": 3, ...} und eine Schleife über die Zeichen reichen.
#         Rückgabe: (material_weiss, material_schwarz)
#         Teste sie zuerst mit der Grundstellung:  chess.STARTING_FEN  → Erwartung: (39, 39)


# TODO 4: Wichtig: Für das Puzzle zählt die Perspektive des LÖSERS, nicht Weiß/Schwarz.
#         Schreib eine Funktion  features(fen, moves)  die:
#           a) ein Brett aus der FEN baut und board.turn VOR dem ersten Zug ausgibt (nur zum Testen, später löschen)
#           b) den ersten Zug spielt (Zug des Gegners)
#           c) prüft, wer jetzt am Zug ist = der Löser (board.turn)
#           d) den Materialvorteil AUS SICHT DES LÖSERS berechnet (positiv = Löser hat mehr)
#           e) die Anzahl Figuren auf dem Brett zählt (Tipp: len(board.piece_map()))
#           f) prüft, ob der erste Lösungszug ein Schach gibt bzw. etwas schlägt
#              Tipp: zug = chess.Move.from_uci(...), dann board.gives_check(zug) und board.is_capture(zug)
#         Rückgabe: ein Dictionary, z.B. {"material_diff": ..., "n_figuren": ..., "loeser_weiss": ..., ...}
#         Teste die Funktion an der ERSTEN Zeile, bevor du sie auf alle anwendest!


# TODO 5: Wende features() auf alle Zeilen an.
#         Tipp: data.apply(lambda row: features(row["FEN"], row["Moves"]), axis=1) liefert eine Spalte
#               voller Dictionaries. pd.DataFrame(liste_von_dicts) macht daraus Spalten.
#         Füge die neuen Spalten an data an (pd.concat(..., axis=1)) und print(data.shape).
#   ❓ Vorher raten: Wie lange dauert das bei 50_000 Zeilen? Miss es mit  import time; start = time.time()


# TODO 6: Welches Feature hängt am stärksten mit dem Rating zusammen?
#         Tipp: data[[deine Feature-Spalten + "Rating"]].corr()["Rating"]
#   ❓ Vorher raten: Welches Feature gewinnt? Gibt es eins, das gar nichts bringt?
#         Schau dir das stärkste Feature auch mit groupby an, so wie in 01.


# TODO 7: Speichere PuzzleId, deine Features und Rating als  data/features_50k.csv  (index=False).
#         Nur diese Spalten! Warum nicht einfach alle Spalten mitspeichern?
#         → Das klären wir in Schritt 05 (Data Leakage). Überleg schon mal.


# 🧪 Experiment (optional): Denk dir ein eigenes Feature aus, das ein Schachspieler für
#    "schwer" halten würde (z.B. Anzahl legaler Züge des Lösers: board.legal_moves). Bringt es was?
