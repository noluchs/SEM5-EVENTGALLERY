const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: [
      'gallery.luchsphoto.ch',
      'localhost'
    ],
    port: 3000
  }
});