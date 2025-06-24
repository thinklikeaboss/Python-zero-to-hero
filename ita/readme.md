# Python Zero to Hero

> Una roadmap pratica e full-stack per padroneggiare Python, dalle basi fino alle web app, agli strumenti CLI, al packaging e oltre.

**Autore:** Luca Bocaletto  
**Repo:** https://github.com/bocaletto-luca/python-zero-to-hero  

[![Test Online](https://img.shields.io/badge/Test%20Online-Visit%20Site-brightgreen?style=for-the-badge)](https://bocaletto-luca.github.io/Python-zero-to-hero/index.html)

---

## 📖 Indice

1. [Panoramica](#panoramica)  
2. [Caratteristiche](#caratteristiche)  
3. [Struttura del progetto](#struttura-del-progetto)  
4. [Primi passi](#primi-passi)  
   - [Prerequisiti](#prerequisiti)  
   - [Installazione](#installazione)  
   - [Servire le lezioni HTML](#servire-le-lezioni-html)  
   - [Eseguire gli script demo](#eseguire-gli-script-demo)  
5. [Capitoli & Contenuti](#capitoli--contenuti)  
6. [Contribuire](#contribuire)  
7. [Licenza](#licenza)  
8. [Ringraziamenti](#ringraziamenti)  

---

## 🌟 Panoramica

**Python Zero to Hero** è il tuo compagno dal primo approccio a Python fino alle applicazioni reali.  
Ogni capitolo include:

- Una **lezione HTML autonoma** (`chapterXX.html`) con stile Bootstrap & Highlight.js.  
- Uno **script demo eseguibile** (`src/chapterXX.py`) che illustra passo passo ogni concetto.  
- **Esercizi** alla fine della lezione per consolidare l’apprendimento.

Che tu preferisca leggere, sperimentare o creare progetti collaterali, questo repo fa al caso tuo.

---

## 🔧 Caratteristiche

- **Fondamenti:** Sintassi, tipi di dato, flusso di controllo, funzioni, moduli, pacchetti.  
- **Intermedio:** OOP, debugging, logging, testing, assertion.  
- **Argomenti avanzati:** Concorrenza (thread, processi, asyncio), API HTTP, JSON/XML, analisi dati (NumPy, pandas), decorator, context manager, type hint.  
- **Tooling:** Packaging & distribuzione (setuptools, wheel, PyPI), accesso a database (sqlite3, SQLAlchemy Core & ORM, Alembic), profiling & ottimizzazione, framework web (Flask, FastAPI), framework CLI (argparse, Click, Typer).  
- **Approccio full-stack:** Dagli esempi di codice ai comandi di deployment.  

---

## 📂 Struttura del progetto

```text
python-zero-to-hero/
├── chapter01.html      ← Lezione HTML 1: Hello, variabili & tipi
├── chapter02.html      ← Lezione HTML 2: Controllo di flusso & cicli
│   …
├── chapter22.html      ← Lezione HTML 22: argparse, Click & Typer
├── README.md           ← Questo documento
└── src/
    ├── chapter01.py    ← Script demo 1
    ├── chapter02.py    ← Script demo 2
    │   …
    └── chapter22.py    ← Script demo 22
```

- **Cartella root:** contiene le lezioni HTML e il README.  
- **src/:** gli script Python corrispondenti a ogni capitolo.  

---

## 🚀 Primi passi

### Prerequisiti

- **Python** 3.8+  
- **Git** (per clonare)  
- (Opzionale) Browser moderno  

### Installazione

```bash
git clone https://github.com/bocaletto-luca/python-zero-to-hero.git
cd python-zero-to-hero
```

### Servire le lezioni HTML

Per migliori risultati, servi i file via HTTP:

```bash
# server HTTP rapido (Python 3.x)
python -m http.server 8000
```

Visita `http://localhost:8000/chapter01.html`, `chapter02.html`, … fino a `chapter22.html`.

### Eseguire gli script demo

Tutti i demo si trovano in `src/`. Per eseguire:

```bash
python src/chapter14.py    # es. demo JSON, XML & HTTP Requests
python src/chapter20.py    # es. demo Database & ORM
```

Ogni script stampa output commentati per seguirli interattivamente.

---

## 📚 Capitoli & Contenuti

| Capitolo | Argomento                                                | Lezione HTML       | Script Demo         |
| -------- | -------------------------------------------------------- | ------------------ | ------------------- |
| 01       | Hello, Variabili & Tipi                                  | chapter01.html     | src/chapter01.py    |
| 02       | Controllo di Flusso & Cicli                              | chapter02.html     | src/chapter02.py    |
| 03       | Funzioni & Moduli                                        | chapter03.html     | src/chapter03.py    |
| 04       | Strutture Dati: Liste, Tuple, Set, Dict                  | chapter04.html     | src/chapter04.py    |
| 05       | File I/O & Eccezioni                                     | chapter05.html     | src/chapter05.py    |
| 06       | Programmazione Orientata agli Oggetti                    | chapter06.html     | src/chapter06.py    |
| 07       | OOP Avanzato: Ereditarietà, Dunder Methods               | chapter07.html     | src/chapter07.py    |
| 08       | Functional Programming: Lambda, map/filter, Comprensioni | chapter08.html     | src/chapter08.py    |
| 09       | Moduli, Pacchetti & Virtual Env                          | chapter09.html     | src/chapter09.py    |
| 10       | Packaging & Distribuzione di base                        | chapter10.html     | src/chapter10.py    |
| 11       | Debugging, Logging & Testing                             | chapter11.html     | src/chapter11.py    |
| 12       | Concorrenza & Parallelismo                               | chapter12.html     | src/chapter12.py    |
| 13       | JSON, XML & HTTP Requests                                | chapter13.html     | src/chapter13.py    |
| 14       | Data Analysis con pandas & NumPy                         | chapter14.html     | src/chapter14.py    |
| 15       | Decorator & Context Manager                              | chapter15.html     | src/chapter15.py    |
| 16       | Type Hints & Typing Statico                              | chapter16.html     | src/chapter16.py    |
| 17       | Packaging & Distribuzione PyPI                           | chapter17.html     | src/chapter17.py    |
| 18       | Profiling & Ottimizzazione delle Prestazioni              | chapter18.html     | src/chapter18.py    |
| 19       | Accesso DB (sqlite3) & SQLAlchemy Core & ORM             | chapter19.html     | src/chapter19.py    |
| 20       | Sviluppo Web: Flask & FastAPI                            | chapter20.html     | src/chapter20.py    |
| 21       | Strumenti CLI: argparse, Click & Typer                   | chapter21.html     | src/chapter21.py    |
| 22       | (Futuro) Argomenti Avanzati…                             | chapter22.html     | src/chapter22.py    |

> **Suggerimento:** Vai a un capitolo aprendo il corrispondente HTML o eseguendone lo script demo.

---

## 🤝 Contribuire

I contributi sono più che benvenuti!  
1. Forka il repo.  
2. Crea un branch per la feature: `git checkout -b feature/nuovo-argomento`.  
3. Committa le modifiche: `git commit -m "Aggiungi capitolo XX: nuovo argomento"`.  
4. Pusha sul tuo branch: `git push origin feature/nuovo-argomento`.  
5. Apri una Pull Request.  

Per favore:

- Segui le convenzioni di naming (`chapterXX.html`, `src/chapterXX.py`).  
- Includi demo di codice, lezione HTML ed esercizi.  
- Aggiorna l’indice del README.

---

## 📄 Licenza

Questo progetto è rilasciato sotto **GPL License**.  
Vedi [LICENSE](LICENSE) per i dettagli.

---

## 🙏 Ringraziamenti

- **Bootstrap** per il layout responsivo e moderno  
- **Highlight.js** per la sintassi del codice  
- La vivace comunità Python per ispirazione e best practice  

---

Buono studio! 🚀  
— _Luca Bocaletto_
