const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
// vue.config.js
module.exports = {
   allowedHosts: [
      'gallery.luchsphoto.ch',
      'localhost'],
  devServer: {
    port: 3000
  }
}

