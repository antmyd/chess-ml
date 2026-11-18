# ♟️ Chess ML – ein Projekt durch das ganze USW-Modul

**Ziel:** Jedes Thema des Moduls einmal selbst an echten Schachdaten bauen, von pandas bis zum KI-Agenten.
**Regel Nr. 1:** Du schreibst den Code. Claude gibt Hinweise, Fragen und Reviews, aber keine fertigen Lösungen
(außer du hängst nach ehrlichem Versuch > 30 Min fest).

## Der Datensatz
**Lichess Puzzle-Datenbank** (kostenlos, ~5 Mio. Schachaufgaben): https://database.lichess.org/#puzzles
Datei `lichess_db_puzzle.csv.zst` herunterladen und in `data/` legen (nicht entpacken, pandas liest .zst direkt).

Spalten: `PuzzleId, FEN, Moves, Rating, RatingDeviation, Popularity, NbPlays, Themes, GameUrl, OpeningTags`
- **FEN** = die Stellung als Text, **Moves** = die Lösungszüge, **Rating** = wie schwer die Aufgabe ist,
  **Themes** = Taktikmotive (fork, pin, mateIn2, …)

Ein Datensatz für alle Phasen, so siehst du direkt, was jede Modellart besser kann.

## Fahrplan
| Phase | Modulthema | Aufgabe | Wann |
|---|---|---|---|
| 0 | Setup | venv, Pakete, Daten laden | jetzt |
| 1 | Data Science & ML | **Wie schwer ist ein Puzzle?** Rating vorhersagen aus selbst gebauten Features (Material, Anzahl Züge, Themen). Baseline → lineare Regression → Baum → Random Forest, sauberer Split, Kreuzvalidierung, Data Leakage finden | diese Woche, neben der Testvorbereitung |
| 2 | Deep Learning | Dasselbe mit einem Feed-Forward-Netz in PyTorch. Stellung als 768er-Vektor (12 Figurtypen × 64 Felder). Erst ein Neuron von Hand, dann das Netz | ab 25.11. |
| 3 | CNN | Brett als Bild: Tensor 12×8×8 → CNN. Ist es besser als das Dense-Netz? Warum? | danach |
| 4 | RNN / LSTM | Die Lösungszüge als Sequenz: Taktikmotiv aus der Zugfolge erkennen | danach |
| 5 | Transformer | Mini-„ChessGPT“: nächsten Zug vorhersagen, Attention auf Züge | danach |
| 6 | GenAI | **Schach-Coach-Agent:** LLM + Function Calling (python-chess, deine Modelle) + RAG; löst Puzzles, lernt aus Fehlern → Vorbild fürs Capstone „Self-Improving Agents“ | ab 01.12. |

## Lernroutine pro Schritt
1. Aufgabe lesen → **erst raten**, was rauskommt
2. Selbst coden, mit `print(...shape)` und kleinen Daten (`nrows=50_000`)
3. Ergebnis mit Vermutung vergleichen: Warum anders?
4. Claude um Review bitten
5. Ein Experiment: eine Sache ändern und beobachten
