const path = require('path');
const { merge } = require('webpack-merge');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
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
      new MiniCssExtractPlugin({
        filename: "[name].css"
      }),
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
      {
        test: /\.scss$/,
        use: [
          {loader: MiniCssExtractPlugin.loader},
          {loader: 'css-loader', options: {
            url: false,
            modules: 'icss',
          }},
          {
            loader: 'sass-loader',
            options: {
              sassOptions: {
                includePaths: [path.resolve(__dirname, '../src/sass')],
              }
            }
          }
        ],
      },
      {
        test: /\.css$/,
        use: [
          {loader: MiniCssExtractPlugin.loader},
          'css-loader'
        ]
      },
    ]
  }
});
