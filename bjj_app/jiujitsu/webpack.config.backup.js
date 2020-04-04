// const path = require('path');
// const HtmlWebpackPlugin = require('html-webpack-plugin');
// const { CleanWebpackPlugin } = require('clean-webpack-plugin');

// module.exports = {
//     devtool: 'inline-source-map',
//     devServer: {
//         contentBase: path.resolve(__dirname, './reservations/static/dist'),
//         historyApiFallback: {
//             index: 'index.html'
//           },
//         hot: true,
//         inline: true,
//         port: 8001,
//         watchContentBase: true,
//     },
//     entry: './reservations/static/js/index.js',
//     mode: 'development',
//     output: {
//         path: path.resolve(__dirname, './reservations/static/dist')
//     },
//     plugins: [
//         new HtmlWebpackPlugin({
//             title: 'Hot Module Replacement',
//             template: path.resolve(__dirname, './reservations/templates/reservations/home.html'),
//         }),
//         new CleanWebpackPlugin(),
//     ],
// };