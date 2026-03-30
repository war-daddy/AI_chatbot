# Sachin's AI Portfolio Chatbot

A production-grade, Next.js/React-compatible AI assistant backend built with FastAPI and an optional OpenAI integration.

## Getting Started

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables:**
   Create a `.env` file in the root directory and add your OpenAI Key (optional - without it, the bot will use a local fallback resume-data mode).
   ```env
   OPENAI_API_KEY="sk-..."
   ```
3. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

## Attaching to Your Portfolio Website

Since your portfolio is built in Next.js/React, you have two primary ways to attach this bot. First, you need to deploy this FastAPI application to a hosting provider. Good free/low-cost options for Python FastAPI backends are **Render** (`render.com`), **Railway**, or **Fly.io**.

Once deployed, you will get a URL like `https://sachin-chat-api.onrender.com`.

### Option 1: The UI iFrame Approach (Fastest)
Currently, this backend natively serves a beautiful, glassmorphism UI from the root route. You can embed the entire UI inside your portfolio site instantly using an iframe:

```jsx
// In your Next.js file (e.g., app/page.tsx or components/ChatWidget.tsx)
export default function ChatWidget() {
  return (
    <div style={{ width: '400px', height: '600px', borderRadius: '24px', overflow: 'hidden' }}>
      <iframe 
        src="https://sachin-chat-api.onrender.com" 
        width="100%" 
        height="100%" 
        style={{ border: 'none' }}
        title="Sachin AI Assistant"
      />
    </div>
  );
}
```

### Option 2: The Custom API Approach (Recommended for Next.js)
If you prefer to build the UI entirely inside your Next.js application (using Tailwind, Framer Motion, etc.), you can simply write a function that interacts with your deployed API:

```javascript
// Example helper function for a Next.js component
const fetchChatbotResponse = async (userMessage) => {
  try {
    const response = await fetch('https://sachin-chat-api.onrender.com/api/v1/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        user_id: 'user_portfolio', // You can optionally generate a random session ID here
        message: userMessage 
      })
    });
    
    const data = await response.json();
    return data.response; // "Hello! I am Sachin Kumar's AI assistant..."
    
  } catch (error) {
    console.error("Chat API Failed", error);
  }
};
```
