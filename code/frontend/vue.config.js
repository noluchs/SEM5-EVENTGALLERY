const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:5001', // Replace 'backend' with your backend service name in the Docker network
        changeOrigin: true
      }
    }
  }
});