<template>
  <div>
    <h1>Galleries</h1>
    <div class="row">
      <div class="col-md-4" v-for="gallery in galleries" :key="gallery.id" @click="openGallery(gallery.id)">
        <div class="card mb-4">
          <img :src="getCoverImageUrl(gallery.cover_image)" class="card-img-top" alt="Gallery Cover">
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
    const response = await fetch('http://localhost:5001/api/gallery/');
    if (response.ok) {
      galleries.value = await response.json();
    } else {
      console.error('Failed to fetch galleries');
    }
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

function getCoverImageUrl(filename) {
  if (!filename) {
    return '/path/to/default/image.png';  // Update the path to your default image
  }
  return `https://msvc-gallery.s3.eu-central-1.amazonaws.com/${filename}`;
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
</style>