import { useState } from "react";
import { useDispatch } from "react-redux";

import "./ChatPanel.css";

import ChatInput from "./ChatInput";
import ChatMessage from "./ChatMessage";

import { sendMessage } from "../../services/chatService";
import { updateInteraction } from "../../redux/interactionSlice";

interface Message {
  sender: "assistant" | "user";
  message: string;
}

function ChatPanel() {
  const dispatch = useDispatch();

  const [messages, setMessages] = useState<Message[]>([
    {
      sender: "assistant",
      message:
        "Hello! Tell me about your interaction with the healthcare professional.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  async function handleSend(message: string) {
    if (!message.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        message,
      },
    ]);

    setLoading(true);

    try {
      const response = await sendMessage(message);

      // Update Redux if backend returns interaction data
      if (response.interaction) {
        dispatch(updateInteraction(response.interaction));
      }

      let aiMessage = "Done.";

      if (response.reply) {
        aiMessage = response.reply;
      } else if (response.messages && response.messages.length > 0) {
        const last = response.messages[response.messages.length - 1];
        aiMessage = last.content || JSON.stringify(last, null, 2);
      }

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          message: aiMessage,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          message: "Unable to connect to the backend.",
        },
      ]);
    }

    setLoading(false);
  }

  return (
    <div className="chat-panel">
      <div className="chat-header">
        <h2>AI Assistant</h2>

        <p>
          Describe the interaction naturally. The AI will complete the form
          automatically.
        </p>
      </div>

      <div className="chat-body">
        {messages.map((msg, index) => (
          <ChatMessage key={index} sender={msg.sender} message={msg.message} />
        ))}

        {loading && <ChatMessage sender="assistant" message="Thinking..." />}
      </div>

      <div className="chat-footer">
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default ChatPanel;
