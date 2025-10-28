# 🔊 SOUNDS LOKAL HOSTEN - ANLEITUNG

## Problem: CORS blockiert externe Audio-URLs

SoundBible.com und andere Seiten blockieren CORS für externe Websites. 

## ✅ Lösung: Sounds lokal hosten

### Schritt 1: Sounds herunterladen

Gehe zu diesen kostenlosen Quellen und lade MP3s herunter:

**Empfohlene Quellen:**
1. **Pixabay Audio** - https://pixabay.com/sound-effects/search/animal/
   - 100% kostenlos, keine Attribution nötig
   - Direkter Download als MP3
   - Sehr gute Qualität

2. **Freesound.org** - https://freesound.org/browse/tags/animal/
   - Kostenlos mit Attribution
   - Große Auswahl
   - Registrierung erforderlich

3. **Mixkit** - https://mixkit.co/free-sound-effects/animals/
   - Kostenlos, keine Attribution
   - Gute Qualität

### Schritt 2: Dateien benennen

Lade mindestens diese Tiere herunter und benenne sie so:

```
elephant.mp3
lion.mp3
tiger.mp3
bear.mp3
wolf.mp3
monkey.mp3
bird.mp3
horse.mp3
cow.mp3
dog.mp3
cat.mp3
pig.mp3
owl.mp3
eagle.mp3
duck.mp3
seal.mp3
whale.mp3
frog.mp3
snake.mp3
camel.mp3
```

### Schritt 3: In Projekt kopieren

Kopiere alle MP3-Dateien in:
```
frontend/public/sounds/
```

Beispiel:
```
frontend/public/sounds/elephant.mp3
frontend/public/sounds/lion.mp3
frontend/public/sounds/tiger.mp3
...
```

### Schritt 4: animalsData.js anpassen

Die Datei `/app/frontend/src/data/animalsData.js` muss angepasst werden.

**Aktuell (funktioniert NICHT wegen CORS):**
```javascript
sounds: ['https://soundbible.com/mp3/Elephant-SoundBible.com-1498791621.mp3']
```

**Neu (funktioniert lokal):**
```javascript
sounds: ['/sounds/elephant.mp3']
```

### Schritt 5: animalsData.js vollständig ersetzen

Ersetze ALLE URLs mit lokalen Pfaden:

```javascript
export const animals = {
  'africa': [
    { id: 'af-1', name: 'Elefante', image: '...', sounds: ['/sounds/elephant.mp3'] },
    { id: 'af-2', name: 'León', image: '...', sounds: ['/sounds/lion.mp3'] },
    { id: 'af-3', name: 'Cebra', image: '...', sounds: ['/sounds/horse.mp3'] },
    // ... usw
  ]
}
```

### Schritt 6: Push & Deploy

1. Commit alle Changes inkl. der MP3-Dateien
2. Push zu GitHub
3. Netlify deployed automatisch
4. **Fertig!** Die Sounds funktionieren jetzt

## 📁 Dateistruktur

```
frontend/
├── public/
│   ├── sounds/           ← NEUE SOUNDS HIER
│   │   ├── elephant.mp3
│   │   ├── lion.mp3
│   │   ├── tiger.mp3
│   │   └── ...
│   └── index.html
└── src/
    └── data/
        └── animalsData.js  ← URLs anpassen
```

## ⚠️ Wichtig

- **Dateigröße**: Halte MP3s klein (<500KB pro Datei)
- **Format**: Nur MP3 (nicht .ogg, .wav)
- **Namen**: Keine Leerzeichen, nur Kleinbuchstaben

## 🎯 Quick Start (minimale Version)

Wenn du nicht alle 84 Tiere brauchst, lade nur diese 10 herunter:

1. elephant.mp3
2. lion.mp3
3. tiger.mp3
4. bear.mp3
5. wolf.mp3
6. monkey.mp3
7. bird.mp3
8. horse.mp3
9. dog.mp3
10. whale.mp3

Und verwende diese für alle Tiere (weniger authentisch, aber funktioniert).

## 🔗 Schnelle Pixabay Links

- Elefant: https://pixabay.com/sound-effects/search/elephant/
- Löwe: https://pixabay.com/sound-effects/search/lion/
- Tiger: https://pixabay.com/sound-effects/search/tiger/
- Bär: https://pixabay.com/sound-effects/search/bear/
- Wolf: https://pixabay.com/sound-effects/search/wolf/

**Klicke auf Download → MP3 → Speichern**
