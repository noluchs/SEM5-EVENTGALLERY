<template>
  <div>
    <h1>Galleries</h1>
    <div class="row">
      <div class="col-md-4" v-for="gallery in galleries" :key="gallery.id" @click="openGallery(gallery.id)">
        <div class="card mb-4">
          <img :src="getCoverImageUrl(gallery.cover_image)" class="card-img-top" alt="Gallery Cover" @error="handleImageError">
          <div class="card-body">
            <h5 class="card-title">{{ gallery.name }}</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const galleries = ref([]);
const router = useRouter();

async function fetchGalleries() {
  try {
    const response = await fetch(`${process.env.VUE_APP_ROOT_API}/gallery`);
    if (response.ok) {
      const data = await response.json();
      console.log('Fetched galleries:', data); // Debugging: Log API response
      galleries.value = data;
    } else {
      console.error('Failed to fetch galleries');
    }
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

function getCoverImageUrl(filename) {
  if (!filename) {
    console.error('Cover image filename is undefined or empty');
    return ''; // Optionally return a placeholder or leave empty to avoid a broken image
  }
  return `https://msvc-gallery.s3.eu-central-1.amazonaws.com/${filename}`;
}

function openGallery(id) {
  router.push(`/gallery/${id}`);
}

function handleImageError(event) {
  console.error(`Error loading image: ${event.target.src}`);
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