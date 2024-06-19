<template>
  <div>
    <h1>{{ gallery.name }}</h1>
    <div class="row">
      <div class="col-md-4" v-for="image in gallery.images" :key="image.id">
        <img :src="image.url" alt="Gallery Image" class="img-thumbnail">
      </div>
    </div>
    <ImageFilter :galleryId="gallery.id" />
  </div>
</template>

<script>
import ImageFilter from './ImageFilter.vue';

export default {
  props: ['gallery'],
  components: {
    ImageFilter
  }
}
</script>

<style scoped>
.img-thumbnail {
  margin-bottom: 15px;
}
</style>