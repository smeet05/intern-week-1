require('dotenv').config();
const express = require('express');
const cors = require('cors');

const app = express();
// Using port 5000 so it doesn't conflict with Next.js later
const PORT = process.env.PORT || 5000;

// Middleware to allow cross-origin requests and parse JSON
app.use(cors());
app.use(express.json());

// A simple test route
app.get('/api/message', (req, res) => {
  res.json({ message: "Hello from the Node.js backend!" });
});

// POST route to receive data
app.post('/api/data', (req, res) => {
  const { userInput } = req.body; // Extract data sent from the frontend
  console.log("Received from frontend:", userInput); // Logs in your backend terminal
  
  // Send a confirmation back to the frontend
  res.json({ success: true, reply: `The server successfully received: "${userInput}"` });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});