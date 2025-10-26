import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import AnimalCard from '../components/AnimalCard';
import ContinentSelector from '../components/ContinentSelector';
import { Headphones } from 'lucide-react';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const HomePage = () => {
  const [selectedContinent, setSelectedContinent] = useState('africa');
  const [soundVariants, setSoundVariants] = useState({});
  const [continents, setContinents] = useState([]);
  const [animals, setAnimals] = useState({});
  const [loading, setLoading] = useState(true);
  const audioRef = useRef(null);

  // Fetch animals data from backend
  useEffect(() => {
    const fetchAnimals = async () => {
      try {
        const response = await axios.get(`${API}/animals`);
        setContinents(response.data.continents);
        setAnimals(response.data.animals);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching animals:', error);
        setLoading(false);
      }
    };

    fetchAnimals();
  }, []);

  const currentAnimals = animals[selectedContinent] || [];

  const handleAnimalPlay = (animal) => {
    // Get the current variant index for this animal, or start at 0
    const currentVariantIndex = soundVariants[animal.id] || 0;
    const nextVariantIndex = (currentVariantIndex + 1) % animal.sounds.length;
    
    // Update the variant index for next time
    setSoundVariants(prev => ({
      ...prev,
      [animal.id]: nextVariantIndex
    }));

    // Play the actual sound
    const soundUrl = animal.sounds[currentVariantIndex];
    console.log(`Playing sound: ${soundUrl} for ${animal.name}`);
    
    // Create and play audio
    if (audioRef.current) {
      audioRef.current.pause();
    }
    
    const audio = new Audio(soundUrl);
    audioRef.current = audio;
    
    audio.play().catch(error => {
      console.log('Audio playback failed:', error);
      // Fallback: still show animation even if sound fails
    });
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-cyan-400 via-blue-500 to-purple-600 flex items-center justify-center">
        <div className="text-white text-2xl font-bold">Cargando animales...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-cyan-400 via-blue-500 to-purple-600">
      {/* Header */}
      <header className="bg-gradient-to-r from-yellow-400 via-pink-500 to-purple-500 shadow-lg">
        <div className="container mx-auto px-6 py-6">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <Headphones className="w-10 h-10 text-white" />
              <h1 className="text-4xl md:text-5xl font-bold text-white drop-shadow-lg">
                Sonidos de Animales
              </h1>
            </div>
            <ContinentSelector
              continents={continents}
              selectedContinent={selectedContinent}
              onSelectContinent={setSelectedContinent}
            />
          </div>
        </div>
      </header>

      {/* Info banner */}
      <div className="bg-yellow-300 border-b-4 border-yellow-400 py-3">
        <div className="container mx-auto px-6">
          <p className="text-center text-lg font-semibold text-purple-900">
            ¡Haz clic en los animales para escuchar sus sonidos! 🎵
          </p>
        </div>
      </div>

      {/* Main content */}
      <main className="container mx-auto px-6 py-12">
        {/* Continent title */}
        <div className="mb-8 text-center">
          <h2 className="text-4xl font-bold text-white drop-shadow-lg mb-2">
            {continents.find(c => c.id === selectedContinent)?.name}
          </h2>
          <div className="h-2 w-32 bg-yellow-400 mx-auto rounded-full shadow-lg" />
        </div>

        {/* Animal grid */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {currentAnimals.map((animal) => (
            <AnimalCard
              key={animal.id}
              animal={animal}
              onPlay={handleAnimalPlay}
            />
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gradient-to-r from-purple-600 to-pink-600 mt-12 py-6">
        <div className="container mx-auto px-6 text-center">
          <p className="text-white text-lg font-semibold">
            🌍 Explora los animales de todos los continentes 🌍
          </p>
        </div>
      </footer>
    </div>
  );
};

export default HomePage;
