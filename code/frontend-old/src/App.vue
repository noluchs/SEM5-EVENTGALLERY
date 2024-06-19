<template>
  <div>
    <h1>Galleries</h1>
    <div v-for="gallery in galleries" :key="gallery.id" @click="openGallery(gallery.id)">
      <img :src="gallery.coverImage" alt="Gallery Cover">
      <h2>{{ gallery.name }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      galleries: []
    }
  },
  created() {
    this.fetchGalleries();
  },
  methods: {
    fetchGalleries() {
      // Fetch galleries from backend
    },
    openGallery(id) {
      this.$router.push(`/gallery/${id}`);
    }
  }
}
</script>