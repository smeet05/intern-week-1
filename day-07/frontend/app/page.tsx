"use client"; 
import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("Loading...");
  const [inputValue, setInputValue] = useState("");
  const [serverResponse, setServerResponse] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/message")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => setMessage("Failed to connect to backend"));
  }, []);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); 
    try {
      const res = await fetch("http://localhost:5000/api/data", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userInput: inputValue }),
      });
      const data = await res.json();
      setServerResponse(data.reply);
      setInputValue(""); 
    } catch (err) {
      setServerResponse("Error sending data");
    }
  };

  return (
    <main style={{ fontFamily: "sans-serif" }}>
      {/* The Navbar was removed from here because layout.tsx handles it now */}
      <div style={{ padding: "40px" }}>
        <h1>My First Full-Stack App</h1>
        <p>Initial connection: <strong>{message}</strong></p>
        
        <hr style={{ margin: "20px 0" }} />
        
        <h2>Send Data to the Server</h2>
        <form onSubmit={handleSubmit}>
          <input 
            type="text" 
            value={inputValue} 
            onChange={(e) => setInputValue(e.target.value)} 
            placeholder="Type a message..."
            style={{ padding: "8px", marginRight: "10px", color: "black" }}
            required
          />
          <button type="submit" style={{ padding: "8px 16px" }}>Send</button>
        </form>
        
        {serverResponse && (
          <p style={{ marginTop: "20px", color: "green" }}>
            <strong>{serverResponse}</strong>
          </p>
        )}
      </div>
    </main>
  );
}