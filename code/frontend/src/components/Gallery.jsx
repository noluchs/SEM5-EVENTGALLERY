import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Gallery = () => {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    const fetchPhotos = async () => {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/photos`);
      setPhotos(response.data);
    };

    fetchPhotos();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <h2 className="text-2xl font-bold text-center mb-8">Gallery</h2>
      <div className="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {photos.map((photo) => (
          <div key={photo._id} className="p-2 bg-white rounded shadow">
            <img src={photo.url} alt="Uploaded" className="w-full rounded" />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Gallery;