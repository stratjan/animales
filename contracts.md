# Animal Sounds Website - Backend Integration Contract

## Overview
This document outlines the backend implementation plan for the Animal Sounds educational website. The frontend is complete with mock data, and we need to integrate real animal sound files.

## Current Frontend State

### Mock Data Location
- File: `/app/frontend/src/data/mockAnimals.js`
- Contains: 84 animals across 7 continents (12 animals per continent)
- Each animal has: id, name (Spanish), image URL, sounds array (2-3 variations)

### Frontend Features Already Implemented
1. Continent selector dropdown (7 continents)
2. Animal grid display (responsive)
3. Click handling on animal cards
4. Sound variation rotation logic (cycles through different sounds)
5. Visual animations during sound playback

## Backend Requirements

### 1. Sound File Management

**Approach: Use Public Animal Sound APIs**
- Primary source: Freesound.org API or similar public sound libraries
- Alternative: Pre-download and store sound files in `/app/backend/static/sounds/`
- File format: MP3 (web-compatible, good compression)

**Directory Structure:**
```
/app/backend/static/sounds/
  ├── elephant1.mp3
  ├── elephant2.mp3
  ├── tiger1.mp3
  ├── lion1.mp3
  └── ... (all animal sounds)
```

### 2. API Endpoints Needed

#### GET /api/animals
**Purpose:** Return all animals data with sound URLs
**Response:**
```json
{
  "continents": [
    {"id": "africa", "name": "África"},
    ...
  ],
  "animals": {
    "africa": [
      {
        "id": "af-1",
        "name": "Elefante",
        "image": "https://...",
        "sounds": [
          "http://backend-url/api/sounds/elephant1.mp3",
          "http://backend-url/api/sounds/elephant2.mp3"
        ]
      },
      ...
    ]
  }
}
```

#### GET /api/sounds/{filename}
**Purpose:** Serve sound files
**Parameters:** filename (e.g., "elephant1.mp3")
**Response:** Audio file stream
**Headers:** Content-Type: audio/mpeg

### 3. Data Model (MongoDB)

**Collection: animals**
```python
{
  "_id": ObjectId,
  "animal_id": "af-1",
  "name": "Elefante",
  "continent": "africa",
  "image_url": "https://...",
  "sound_files": ["elephant1.mp3", "elephant2.mp3"],
  "created_at": datetime
}
```

### 4. Frontend Integration Changes

**File: `/app/frontend/src/pages/HomePage.jsx`**

**Current (Mock):**
```javascript
import { continents, animals } from '../data/mockAnimals';
```

**After Integration:**
```javascript
const [animals, setAnimals] = useState({});
const [continents, setContinents] = useState([]);

useEffect(() => {
  fetch(`${API}/animals`)
    .then(res => res.json())
    .then(data => {
      setContinents(data.continents);
      setAnimals(data.animals);
    });
}, []);
```

**Sound Playback Integration:**
```javascript
const handleAnimalPlay = (animal) => {
  const currentVariantIndex = soundVariants[animal.id] || 0;
  const nextVariantIndex = (currentVariantIndex + 1) % animal.sounds.length;
  
  setSoundVariants(prev => ({
    ...prev,
    [animal.id]: nextVariantIndex
  }));

  // Play actual sound
  const audio = new Audio(animal.sounds[currentVariantIndex]);
  audio.play();
};
```

## Implementation Steps

### Phase 1: Backend Setup
1. Create `/app/backend/static/sounds/` directory
2. Download representative sound samples for key animals (8-10 animals as proof of concept)
3. Create MongoDB model for animals
4. Seed database with animal data

### Phase 2: API Implementation
1. Implement GET /api/animals endpoint
2. Implement GET /api/sounds/{filename} endpoint with static file serving
3. Test endpoints with curl/Postman

### Phase 3: Frontend Integration
1. Remove mock data import
2. Add API fetch in HomePage component
3. Update sound playback to use real audio URLs
4. Test across different continents

### Phase 4: Sound Library Expansion
1. Add sounds for all 84 animals (if time/resources permit)
2. Add error handling for missing sounds
3. Add loading states

## Sound File Sources

**Freesound.org:**
- Free sound library with API access
- Requires API key (free registration)
- License: Creative Commons

**Alternative Sources:**
- Pixabay Audio (royalty-free)
- BBC Sound Effects Archive
- Zapsplat (free tier available)

## Technical Notes

### CORS Configuration
Backend must allow audio streaming:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Audio File Serving
Use FastAPI's StaticFiles for efficient serving:
```python
from fastapi.staticfiles import StaticFiles
app.mount("/api/sounds", StaticFiles(directory="static/sounds"), name="sounds")
```

### Performance Considerations
- Audio files should be compressed (MP3, 64-128 kbps sufficient for animal sounds)
- Consider caching headers for frequently accessed sounds
- File size target: <200KB per sound file

## Success Criteria

- [ ] Backend serves animal data via API
- [ ] Sound files are accessible via URL
- [ ] Frontend fetches data from backend (no more mock data)
- [ ] Clicking animals plays real audio
- [ ] Sound variations work (multiple clicks = different sounds)
- [ ] Works across all 7 continents
- [ ] No console errors
- [ ] Audio playback duration: 5-7 seconds per animal sound
