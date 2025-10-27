# 🦁 Sonidos de Animales - Animal Sounds Website

Eine kinderfreundliche, interaktive Website zum Lernen von Tierstimmen aus der ganzen Welt.

## 🌍 Features

- **84 Tiere** aus 7 Kontinenten
- **Echte Tierstimmen** von Wikimedia Commons (Public Domain)
- **7 Kontinente**: África, Asia, Europa, América del Norte, América del Sur, Australia, Antártida
- **Mehrfache Soundvarianten** pro Tier
- **Responsive Design** für alle Geräte
- **Spanische UI** - perfekt für Kinder
- **100% statisch** - kein Backend benötigt

## 🔊 Troubleshooting - Keine Sounds?

Wenn du keine Sounds hörst auf Netlify, hier sind die Lösungen:

### Problem 1: Browser-Kompatibilität (.ogg Format)

**Lösung**: Verwende **Chrome** oder **Firefox**. Safari unterstützt .ogg nicht gut.

### Problem 2: Browser blockiert Audio

**Lösung**: 
1. Überprüfe in den Browser-Einstellungen, ob Audio erlaubt ist
2. Klicke auf den "Prueba de Audio" Button auf der Seite
3. Erlaube Audio-Wiedergabe wenn der Browser fragt

### Problem 3: CORS-Policy von Wikimedia

**Wenn Wikimedia URLs blockiert sind**, kannst du die Sound-URLs ersetzen:

Öffne `/frontend/src/data/animalsData.js` und ersetze die Wikimedia URLs durch lokale Dateien oder andere Public Domain Quellen wie:
- https://www.zapsplat.com (nach Registration)
- https://freesound.org (mit API key)

### Problem 4: Browser Dev Tools zeigt Fehler

Öffne die Browser-Konsole (F12) und schaue nach Fehlermeldungen. Die App zeigt jetzt detaillierte Debug-Informationen.

### Schnell-Test:

1. Öffne deine Netlify-Seite
2. Klicke auf "Probar Sonido de Elefante" 
3. Wenn das funktioniert, funktionieren alle Sounds
4. Wenn nicht, siehst du die Fehlermeldung

---

## 🚀 Deployment auf Netlify

### Option 1: Via GitHub

1. Pushe das Repository auf GitHub
2. Verbinde dein Netlify-Konto mit GitHub
3. Wähle das Repository aus
4. Netlify erkennt automatisch die `netlify.toml` Konfiguration
5. Klicke auf "Deploy"

### Option 2: Drag & Drop

1. Baue das Projekt lokal:
   ```bash
   cd frontend
   yarn build
   ```

2. Ziehe den `build` Ordner auf Netlify's Deploy-Bereich

### Konfiguration

Die `netlify.toml` ist bereits konfiguriert:
```toml
[build]
  base = "frontend"
  command = "yarn build"
  publish = "build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## 📂 Wichtige Dateien für Netlify

- `/netlify.toml` - Netlify Build-Konfiguration
- `/frontend/public/index.html` - HTML Entry Point
- `/frontend/src/data/animalsData.js` - Alle Tierdaten & Sound-URLs
- `/frontend/package.json` - Dependencies

## 🔊 So funktioniert es

Alle Tierstimmen werden direkt von Wikimedia Commons geladen (Public Domain):
```javascript
sounds: ['https://upload.wikimedia.org/wikipedia/commons/5/57/Lion_roar.ogg']
```

## 🎨 Technologie

- **Frontend**: React 19 mit Hooks
- **UI Components**: Shadcn UI
- **Styling**: TailwindCSS
- **Sounds**: Wikimedia Commons (.ogg Format)
- **Hosting**: Netlify (empfohlen)

---

**Website läuft komplett ohne Backend - perfekt für Netlify! 🎉**
