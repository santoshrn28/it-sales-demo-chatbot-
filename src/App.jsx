import React from "react";
import ChatWidget from "./ChatWidget";

function App() {
  return (
    <div style={{ fontFamily: "Arial", padding: "30px" }}>
      <h1>IT Sales Customer Care Chatbot Demo</h1>
      <p>
        Ask about endpoint security, cloud backup, cloud migration,
        managed IT support, or request a sales demo.
      </p>
      <ChatWidget />
    </div>
  );
}

export default App;
