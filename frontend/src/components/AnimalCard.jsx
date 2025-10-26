import React, { useState } from 'react';
import { Volume2 } from 'lucide-react';
import { Card } from './ui/card';

const AnimalCard = ({ animal, onPlay }) => {
  const [isPlaying, setIsPlaying] = useState(false);

  const handleClick = () => {
    setIsPlaying(true);
    onPlay(animal);
    setTimeout(() => setIsPlaying(false), 6000);
  };

  return (
    <Card
      onClick={handleClick}
      className={
        `relative overflow-hidden cursor-pointer group transition-all duration-300 hover:scale-105 hover:shadow-2xl border-4 ${
          isPlaying ? 'ring-4 ring-yellow-400 scale-105 shadow-2xl' : 'border-white'
        }`
      }
      style={{ borderRadius: '20px' }}
    >
      <div className="aspect-square relative">
        <img
          src={animal.image}
          alt={animal.name}
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        
        {/* Sound icon */}
        <div className={
          `absolute top-3 right-3 bg-white rounded-full p-2 transition-all duration-300 ${
            isPlaying ? 'animate-pulse scale-110' : 'opacity-0 group-hover:opacity-100'
          }`
        }>
          <Volume2 className="w-5 h-5 text-purple-600" />
        </div>

        {/* Playing indicator */}
        {isPlaying && (
          <div className="absolute inset-0 flex items-center justify-center bg-black/40">
            <div className="flex space-x-2">
              <div className="w-3 h-8 bg-yellow-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
              <div className="w-3 h-8 bg-yellow-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
              <div className="w-3 h-8 bg-yellow-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
            </div>
          </div>
        )}
      </div>
      
      {/* Animal name */}
      <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/90 to-transparent p-4">
        <h3 className="text-white text-xl font-bold text-center">{animal.name}</h3>
      </div>
    </Card>
  );
};

export default AnimalCard;
