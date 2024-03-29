const { defineConfig } = require('@vue/cli-service')

const BundleTracker = require("webpack-bundle-tracker");

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: "http://127.0.0.1:8080/",
  outputDir: "./dist/",

  chainWebpack: (config) => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    config.output.filename("bundle.js");
    config.optimization.splitChunks(false);
    config.resolve.alias.set("__STATIC__", "static");
  },

  devServer: {
    devMiddleware: {
      publicPath: "http://127.0.0.1:8080",
    },
    hot: "only",
    headers: { "Access-Control-Allow-Origin": "*" },
  },

  css: {
    extract: {
      filename: 'bundle.css',
      chunkFilename: 'bundle.css',
    },
  }
})