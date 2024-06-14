import React, {useState, useEffect} from 'react';
import axios from 'axios';

const PhotoManager = () => {
    const [galleries, setGalleries] = useState([]);
    const [selectedGallery, setSelectedGallery] = useState('');
    const [photos, setPhotos] = useState([]);
    const [file, setFile] = useState(null);
    const [description, setDescription] = useState('');

    useEffect(() => {
        const fetchGalleries = async () => {
            try {
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/galleries`);
                setGalleries(response.data);
            } catch (error) {
                console.error('Error fetching galleries:', error);
            }
        };

        fetchGalleries();
    }, []);

    useEffect(() => {
        if (selectedGallery) {
            const fetchPhotos = async () => {
                try {
                    const response = await axios.get(`${import.meta.env.VITE_API_URL}/photos/${selectedGallery}`);
                    setPhotos(response.data);
                } catch (error) {
                    console.error('Error fetching photos:', error);
                }
            };

            fetchPhotos();
        }
    }, [selectedGallery]);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('photo', file);
        formData.append('description', description);

        try {
            const response = await axios.post(`${import.meta.env.VITE_API_URL}/photos/${selectedGallery}`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setPhotos([...photos, response.data]);
            setFile(null);
            setDescription('');
        } catch (error) {
            console.error('Error uploading photo:', error);
        }
    };

    const handleDeletePhoto = async (id) => {
        try {
            await axios.delete(`${import.meta.env.VITE_API_URL}/photos/${id}`);
            setPhotos(photos.filter(photo => photo._id !== id));
        } catch (error) {
            console.error('Error deleting photo:', error);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 py-8">
            <div className="container mx-auto">
                <h2 className="text-2xl font-bold text-center mb-8">Manage Photos</h2>
                <div className="mb-8">
                    <label className="block text-sm font-medium text-gray-700">Select Gallery</label>
                    <select
                        value={selectedGallery}
                        onChange={(e) => setSelectedGallery(e.target.value)}
                        className="w-full p-2 border border-gray-300 rounded mt-1"
                    >
                        <option value="">Select a gallery</option>
                        {galleries.map(gallery => (
                            <option key={gallery._id} value={gallery._id}>{gallery.title}</option>
                        ))}
                    </select>
                </div>
                {selectedGallery && (
                    <>
                        <form onSubmit={handleSubmit} className="space-y-4 mb-8">
                            <div>
                                <label className="block text-sm font-medium text-gray-700">Photo</label>
                                <input
                                    type="file"
                                    onChange={handleFileChange}
                                    className="w-full p-2 border border-gray-300 rounded mt-1"
                                    required
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700">Description</label>
                                <input
                                    type="text"
                                    value={description}
                                    onChange={(e) => setDescription(e.target.value)}
                                    className="w-full p-2 border border-gray-300 rounded mt-1"
                                    placeholder="Description"
                                    required
                                />
                            </div>
                            <button type="submit"
                                    className="w-full py-2 text-white bg-blue-500 rounded hover:bg-blue-600">
                                Upload Photo
                            </button>
                        </form>
                        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                            {photos.map(photo => (
                                <div key={photo._id} className="p-4 bg-white rounded shadow">
                                    <img src={photo.url} alt={photo.description}
                                         className="w-full h-48 object-cover rounded"/>
                                    <p className="mt-2 text-sm text-gray-600">{photo.description}</p>
                                    <button
                                        onClick={() => handleDeletePhoto(photo._id)}
                                        className="mt-4 py-2 px-4 bg-red-500 text-white rounded hover:bg-red-600"
                                    >
                                        Delete Photo
                                    </button>
                                </div>
                            ))}
                        </div>
                    </>
                )}
            </div>
        </div>