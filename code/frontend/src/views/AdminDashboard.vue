<template>
  <div class="container mt-5">
    <h1>Admin Dashboard</h1>

    <form @submit.prevent="createGallery" class="mb-5">
      <div class="mb-3">
        <label for="galleryName" class="form-label">Gallery Name</label>
        <input type="text" class="form-control" id="galleryName" v-model="newGallery.name" required>
      </div>
      <button type="submit" class="btn btn-primary">Create Gallery</button>
    </form>

    <div v-if="galleries.length">
      <h2>Galleries</h2>
      <div v-for="gallery in galleries" :key="gallery.id" class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">{{ gallery.name }}</h5>
          <button @click="deleteGallery(gallery.id)" class="btn btn-danger">Delete Gallery</button>
          <input type="file" @change="uploadImage(gallery.id, $event)" class="form-control mt-3">
        </div>
      </div>
    </div>
    <p v-else>No galleries available</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const galleries = ref([]);
const newGallery = ref({ name: '' });

async function fetchGalleries() {
  try {
    const response = await axios.get('http://localhost:5001/api/api/gallery', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value = response.data;
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

async function createGallery() {
  try {
    const response = await axios.post('http://localhost:5001/api/api/gallery', newGallery.value, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value.push(response.data);
    newGallery.value.name = '';
  } catch (error) {
    console.error('Error creating gallery:', error);
  }
}

async function deleteGallery(galleryId) {
  try {
    await axios.delete(`http://localhost:5001/api/api/gallery/${galleryId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value = galleries.value.filter(gallery => gallery.id !== galleryId);
  } catch (error) {
    console.error('Error deleting gallery:', error);
  }
}

async function uploadImage(galleryId, event) {
  const file = event.target.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);
  formData.append('gallery_id', galleryId);

  try {
    await axios.post('http://backend:5001/api/api/image', formData, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'multipart/form-data'
      }
    });
    alert('Image uploaded successfully');
  } catch (error) {
    console.error('Error uploading image:', error);
  }
}

onMounted(() => {
  fetchGalleries();
});
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}
</style>