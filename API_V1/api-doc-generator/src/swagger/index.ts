export function setupSwaggerUI(app: any, swaggerDocument: any) {
    const swaggerUi = require('swagger-ui-express');
    app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
}