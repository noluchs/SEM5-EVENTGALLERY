<template>
  <div>
    <Gallery :gallery="gallery" />
  </div>
</template>

<script>
import Gallery from '../components/Gallery.vue';

export default {
  data() {
    return {
      gallery: {}
    }
  },
  created() {
    this.fetchGallery();
  },
  methods: {
    fetchGallery() {
      const galleryId = this.$route.params.id;
      // Fetch gallery details from backend using galleryId
    }
  },
  components: {
    Gallery
  }
}
</script>