var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: './src/app/index',

    output: {
        path: path.resolve('./dist/app/'),
        filename: 'bundle.js',
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],

    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', "es2015"]
                }
            }
        ]
    },

    resolve: {
        extensions: ['.js', '.jsx'],
        modules: ['node_modules']
    }
};