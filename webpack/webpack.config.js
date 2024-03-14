const { merge } = require('webpack-merge');
const resolve = require('./resolve.config.js');

// noinspection JSCheckFunctionSignatures
module.exports = merge(resolve, {
  entry: {
    bundle: './src/application/main.jsx',
  },
  output: {
    filename: '[name].js',
  },
  devtool: 'source-map',
  plugins: [
  ],
  performance: {
    maxAssetSize: 1024 * 1024, // 1mb
    maxEntrypointSize: 1024 * 1024, // 1mb
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        use: {
          loader: 'babel-loader',
        },
      },
    ]
  }
});
