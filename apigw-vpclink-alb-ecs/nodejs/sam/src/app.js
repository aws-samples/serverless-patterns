// Main application entry point
const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Hardcoded product data for demonstration
const products = [
  {
    id: "1",
    name: "Sample Product",
    description: "A demo product for testing",
    price: 29.99,
    category: "Electronics"
  },
  {
    id: "2", 
    name: "Demo Widget",
    description: "Another test product",
    price: 15.50,
    category: "Gadgets"
  },
  {
    id: "3",
    name: "Test Item",
    description: "Third demo product",
    price: 99.99,
    category: "Tools"
  }
];

// Routes
app.get('/products', (req, res) => {
  try {
    res.status(200).json({
      products: products
    });
  } catch (error) {
    res.status(500).json({
      error: {
        code: "INTERNAL_ERROR",
        message: "An unexpected error occurred"
      }
    });
  }
});

app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString()
  });
});

// Handle method not allowed for products endpoint
app.all('/products', (req, res) => {
  if (req.method !== 'GET') {
    return res.status(405).json({
      error: {
        code: "METHOD_NOT_ALLOWED",
        message: "Only GET method is allowed"
      }
    });
  }
});

// Handle 404 for unknown routes
app.use('*', (req, res) => {
  res.status(404).json({
    error: {
      code: "NOT_FOUND",
      message: "Endpoint not found"
    }
  });
});

// Start server only if not being required as a module
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}

module.exports = app;