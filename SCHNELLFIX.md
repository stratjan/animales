# 🚨 SCHNELLFIX: Sounds funktionieren nicht wegen CORS

## Problem
```
Access to audio has been blocked by CORS policy
```

## ✅ Lösung in 3 Schritten

### 1️⃣ Sounds herunterladen (15 Min)

Gehe zu **Pixabay**: https://pixabay.com/sound-effects/search/animal/

Lade diese MP3s herunter (klick "Download" → "MP3"):

| Dateiname | Suche bei Pixabay |
|-----------|-------------------|
| `elephant.mp3` | "elephant sound" |
| `lion.mp3` | "lion roar" |
| `tiger.mp3` | "tiger roar" |
| `bear.mp3` | "bear growl" |
| `wolf.mp3` | "wolf howl" |
| `monkey.mp3` | "monkey sound" |
| `bird.mp3` | "bird chirp" |
| `horse.mp3` | "horse neigh" |
| `cow.mp3` | "cow moo" |
| `dog.mp3` | "dog bark" |
| `cat.mp3` | "cat meow" |
| `pig.mp3` | "pig oink" |
| `owl.mp3` | "owl hoot" |
| `eagle.mp3` | "eagle screech" |
| `duck.mp3` | "duck quack" |
| `seal.mp3` | "seal bark" |
| `whale.mp3` | "whale sound" |
| `frog.mp3` | "frog croak" |
| `snake.mp3` | "snake hiss" |
| `camel.mp3` | "camel sound" |

### 2️⃣ Dateien kopieren

Kopiere alle MP3s in:
```
frontend/public/sounds/
```

### 3️⃣ Code anpassen

Ersetze `/app/frontend/src/data/animalsData.js` mit:
`/app/frontend/src/data/animalsData_LOCAL.js`

```bash
# Im Terminal:
cd /app/frontend/src/data/
rm animalsData.js
mv animalsData_LOCAL.js animalsData.js
```

Oder kopiere den Inhalt von `animalsData_LOCAL.js` nach `animalsData.js`.

### 4️⃣ Deploy

```bash
git add .
git commit -m "Add local sounds"
git push
```

Netlify deployed automatisch - **FERTIG!** 🎉

## Minimale Version (schneller)

Lade nur **5 Sounds** herunter und nutze sie mehrfach:

1. `animal1.mp3` (Elefant) → für alle großen Tiere
2. `animal2.mp3` (Löwe) → für alle Raubtiere  
3. `animal3.mp3` (Vogel) → für alle Vögel
4. `animal4.mp3` (Hund) → für alle kleinen Säugetiere
5. `animal5.mp3` (Frosch) → für alle Amphibien

Passe dann die Pfade in `animalsData.js` entsprechend an.

## ❓ Fragen?

Wenn es immer noch nicht funktioniert, prüfe:
1. Sind die MP3s in `frontend/public/sounds/`?
2. Heißen sie genau wie in der Datei (z.B. `elephant.mp3`)?
3. Deployed Netlify den neuen Code?
