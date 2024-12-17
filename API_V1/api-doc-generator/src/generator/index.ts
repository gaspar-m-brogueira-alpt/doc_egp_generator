export class Generator {
    generateOpenAPIDocumentation(endpoints: any[]): string {
        const openAPIDocumentation = {
            openapi: "3.0.0",
            info: {
                title: "Generated API Documentation",
                version: "1.0.0",
            },
            paths: {},
        };

        endpoints.forEach(endpoint => {
            const { path, method, parameters, responses } = endpoint;
            if (!openAPIDocumentation.paths[path]) {
                openAPIDocumentation.paths[path] = {};
            }
            openAPIDocumentation.paths[path][method] = {
                parameters: parameters.map(param => ({
                    name: param.name,
                    in: param.in,
                    required: param.required,
                    schema: {
                        type: param.type,
                    },
                })),
                responses: responses.reduce((acc, response) => {
                    acc[response.status] = {
                        description: response.description,
                        content: {
                            "application/json": {
                                schema: {
                                    type: response.type,
                                },
                            },
                        },
                    };
                    return acc;
                }, {}),
            };
        });

        return JSON.stringify(openAPIDocumentation, null, 2);
    }
}