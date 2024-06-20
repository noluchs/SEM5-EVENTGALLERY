<template>
  <div>
    <GalleryView :gallery="gallery" />
  </div>
</template>

<script>
import GalleryView from '../components/GalleryView.vue';

export default {
  name: 'GalleryPage',
  data() {
    return {
      gallery: {}
    }
  },
  created() {
    this.fetchGallery();
  },
  methods: {
    async fetchGallery() {
      const galleryId = this.$route.params.id;
      try {
        const response = await fetch(`http://localhost:5001/api/galleries/${galleryId}`);
        if (response.ok) {
          this.gallery = await response.json();
        } else {
          console.error('Failed to fetch gallery details');
        }
      } catch (error) {
        console.error('Error fetching gallery details:', error);
      }
    }
  },
  components: {
    GalleryView
  }
}
</script>