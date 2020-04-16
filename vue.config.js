module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api*': {
        target: 'http://127.0.0.1:8000'
       // target: 'https://eithleithya-api.herokuapp.com/'
      }
    }
  },
  transpileDependencies: [
    'vuetify'
  ]
}
