export interface Endpoint {
    path: string;
    method: string;
    parameters: Parameter[];
    responses: Response[];
}

export interface Parameter {
    name: string;
    in: 'query' | 'header' | 'path' | 'cookie';
    required: boolean;
    type: string;
    description?: string;
}

export interface Response {
    statusCode: number;
    description: string;
    schema?: any; // This can be further defined based on the response structure
}