# API Documentation Generator

This project is a tool that automatically analyzes the source code of a RESTful API, extracts information about endpoints, parameters, and responses, and generates detailed documentation in OpenAPI format. The generated documentation can be displayed using Swagger UI.

## Features

- Automatically scans source code for RESTful API endpoints.
- Extracts parameters and responses for each endpoint.
- Generates OpenAPI documentation.
- Displays documentation using Swagger UI.

## Project Structure

```
api-doc-generator
├── src
│   ├── index.ts          # Entry point of the application
│   ├── analyzer          # Contains logic for analyzing API endpoints
│   │   └── index.ts
│   ├── generator         # Responsible for generating OpenAPI documentation
│   │   └── index.ts
│   ├── swagger           # Configures and serves Swagger UI
│   │   └── index.ts
│   └── types             # Defines data structures used in the application
│       └── index.ts
├── package.json          # npm configuration file
├── tsconfig.json         # TypeScript configuration file
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd api-doc-generator
   ```
3. Install the dependencies:
   ```
   npm install
   ```

## Usage

1. Run the tool:
   ```
   npm start
   ```
2. Access the Swagger UI at `http://localhost:3000/docs` to view the generated OpenAPI documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.