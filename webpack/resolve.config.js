const path = require('path');

module.exports = {
    resolve: {
        alias: {
            '@': path.resolve(__dirname, '../src/application/'),
            '~': path.resolve(__dirname, '../src/application/'),
        },
        extensions: ['*', '.js', '.jsx']
    }
};
