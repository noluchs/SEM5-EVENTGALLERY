import React from 'react';
import { Link } from 'react-router-dom';

const GalleryCard = ({ gallery }) => {
  return (
    <Link to={`/galleries/${gallery._id}`} className="block p-4 bg-white rounded shadow hover:shadow-lg transition-shadow duration-300">
      <img src={gallery.coverImage} alt={gallery.title} className="w-full h-48 object-cover rounded" />
      <h3 className="mt-4 text-lg font-bold">{gallery.title}</h3>
    </Link>
  );
};

export default GalleryCard;