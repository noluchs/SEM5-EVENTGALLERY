<template>
  <div id="app">
    <MenuBar />
    <router-view></router-view>
  </div>
</template>

<script setup>
import MenuBar from '@/components/MenuBar.vue';
</script>

<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>