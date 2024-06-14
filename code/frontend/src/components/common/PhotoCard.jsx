import React from 'react';

const PhotoCard = ({ photo }) => {
  return (
    <div className="p-4 bg-white rounded shadow hover:shadow-lg transition-shadow duration-300">
      <img src={photo.url} alt={photo.description} className="w-full h-48 object-cover rounded" />
      <p className="mt-2 text-sm text-gray-600">{photo.description}</p>
    </div>
  );
};

export default PhotoCard;