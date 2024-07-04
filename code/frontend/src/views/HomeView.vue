<template>
  <div class="container mt-5">
    <h1>Galleries</h1>
    <div v-if="galleries.length" class="row">
      <div v-for="gallery in galleries" :key="gallery.id" class="col-md-4 mb-4" @click="openGallery(gallery.id)">
        <div class="card">
          <img :src="gallery.cover_image_url" class="card-img-top" alt="Gallery Cover" @error="handleImageError">
          <div class="card-body">
            <h5 class="card-title">{{ gallery.name }}</h5>
          </div>
        </div>
      </div>
    </div>
    <p v-else>No galleries available</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const galleries = ref([]);
const router = useRouter();

async function fetchGalleries() {
  try {
    const response = await axios.get(`${process.env.VUE_APP_ROOT_API}/gallery/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value = response.data;
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

function handleImageError(event) {
  console.error(`Error loading image: ${event.target.src}`);
  event.target.src = 'https://via.placeholder.com/150'; // Fallback image
}

function openGallery(id) {
  router.push(`/gallery/${id}`);
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
.card-img-top {
  max-height: 200px;
  object-fit: cover;
}
</style>