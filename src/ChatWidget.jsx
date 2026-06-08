import React, { useState } from "react";

const API_URL = "http://localhost:8000";

function ChatWidget() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello! I am your IT sales assistant. How can I help you today?"
    }
  ]);

  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = input;

    setMessages(prev => [...prev, { sender: "user", text: userMessage }]);
    setInput("");

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
      });

      const data = await res.json();

      setMessages(prev => [...prev, { sender: "bot", text: data.reply }]);
    } catch (error) {
      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: "Sorry, backend is not reachable. Please check if the API is running."
        }
      ]);
    }
  };

  return (
    <div style={{ width: "520px", border: "1px solid #ccc", padding: "15px" }}>
      <div style={{ height: "350px", overflowY: "auto", marginBottom: "15px" }}>
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              textAlign: msg.sender === "user" ? "right" : "left",
              margin: "10px"
            }}
          >
            <span
              style={{
                background: msg.sender === "user" ? "#0078d4" : "#eeeeee",
                color: msg.sender === "user" ? "#ffffff" : "#000000",
                padding: "8px 12px",
                borderRadius: "10px",
                display: "inline-block",
                maxWidth: "80%"
              }}
            >
              {msg.text}
            </span>
          </div>
        ))}
      </div>

      <input
        style={{ width: "75%", padding: "8px" }}
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === "Enter" && sendMessage()}
        placeholder="Type your message..."
      />

      <button
        style={{ width: "20%", marginLeft: "5px", padding: "8px" }}
        onClick={sendMessage}
      >
        Send
      </button>
    </div>
  );
}

export default ChatWidget;
