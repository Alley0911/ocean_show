module.exports = {
	devServer: {
		proxy: 'http://10.28.16.192:80'
	},
	publicPath: process.env.NODE_ENV === 'production'
		? "/ocean_show/"
		: '/'
}
