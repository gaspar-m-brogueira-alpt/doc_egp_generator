import { Analyzer } from './analyzer';
import { Generator } from './generator';
import { setupSwaggerUI } from './swagger';

const analyzer = new Analyzer();
const generator = new Generator();

// Initialize the tool
async function init() {
    try {
        const endpoints = await analyzer.analyzeEndpoints();
        const parameters = analyzer.extractParameters(endpoints);
        const responses = analyzer.extractResponses(endpoints);
        
        const openAPIDocumentation = generator.generateOpenAPIDocumentation(endpoints, parameters, responses);
        
        setupSwaggerUI(openAPIDocumentation);
    } catch (error) {
        console.error('Error initializing API Doc Generator:', error);
    }
}

init();