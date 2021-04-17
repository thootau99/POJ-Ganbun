const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = (app) => {
	app.use(createProxyMiddleware('/api/v1', { target: 'http://localhost:5000'}));
}