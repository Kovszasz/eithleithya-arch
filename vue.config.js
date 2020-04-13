module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api*': {
        target: process.env.HOST + ': 8000'
      }
    }
  },
  transpileDependencies: [
    'vuetify'
  ]
}
