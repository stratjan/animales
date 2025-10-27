import React, { useState } from 'react';
import { Button } from './ui/button';
import { Volume2, VolumeX, AlertCircle } from 'lucide-react';

const AudioTester = () => {
  const [testResult, setTestResult] = useState(null);
  const [testing, setTesting] = useState(false);

  const testAudio = async () => {
    setTesting(true);
    setTestResult(null);

    // Test URL - Elephant sound from SoundBible (MP3 format)
    const testUrl = 'https://soundbible.com/mp3/Elephant-SoundBible.com-1498791621.mp3';

    try {
      const audio = new Audio();
      audio.src = testUrl;

      audio.addEventListener('canplaythrough', () => {
        setTestResult({ success: true, message: '✅ Audio funciona correctamente!' });
        audio.play().catch(e => {
          setTestResult({ success: false, message: `❌ Error al reproducir: ${e.message}` });
        });
        setTesting(false);
      });

      audio.addEventListener('error', (e) => {
        setTestResult({ 
          success: false, 
          message: `❌ No se puede cargar el audio. Por favor, verifica tu conexión a internet.` 
        });
        setTesting(false);
      });

      audio.load();
    } catch (error) {
      setTestResult({ success: false, message: `❌ Error: ${error.message}` });
      setTesting(false);
    }
  };

  return (
    <div className="bg-white/90 rounded-lg p-4 shadow-lg max-w-md mx-auto mb-6">
      <div className="flex items-center gap-3 mb-3">
        <Volume2 className="w-6 h-6 text-purple-600" />
        <h3 className="font-bold text-lg">Prueba de Audio</h3>
      </div>
      
      <Button 
        onClick={testAudio} 
        disabled={testing}
        className="w-full bg-purple-600 hover:bg-purple-700"
      >
        {testing ? 'Probando...' : 'Probar Sonido de Elefante'}
      </Button>

      {testResult && (
        <div className={`mt-3 p-3 rounded ${testResult.success ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
          <p className="font-semibold flex items-center gap-2">
            {testResult.success ? <Volume2 className="w-4 h-4" /> : <VolumeX className="w-4 h-4" />}
            {testResult.message}
          </p>
        </div>
      )}

      <div className="mt-3 text-sm text-gray-600 space-y-1">
        <p className="flex items-start gap-2">
          <AlertCircle className="w-4 h-4 mt-0.5 flex-shrink-0" />
          <span>Si no funciona, intenta usar <strong>Chrome</strong> o <strong>Firefox</strong></span>
        </p>
        <p className="flex items-start gap-2">
          <AlertCircle className="w-4 h-4 mt-0.5 flex-shrink-0" />
          <span>Safari puede tener problemas con archivos .ogg</span>
        </p>
      </div>
    </div>
  );
};

export default AudioTester;
