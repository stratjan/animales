import React from 'react';
import { Globe } from 'lucide-react';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from './ui/select';

const ContinentSelector = ({ continents, selectedContinent, onSelectContinent }) => {
  return (
    <div className="flex items-center gap-3">
      <Globe className="w-6 h-6 text-white" />
      <Select value={selectedContinent} onValueChange={onSelectContinent}>
        <SelectTrigger className="w-[250px] bg-white/90 border-2 border-white text-lg font-semibold hover:bg-white transition-colors">
          <SelectValue placeholder="Selecciona un continente" />
        </SelectTrigger>
        <SelectContent>
          {continents.map((continent) => (
            <SelectItem key={continent.id} value={continent.id} className="text-lg">
              {continent.name}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
};

export default ContinentSelector;
