interface Props {
  message: string;
  sender: "user" | "assistant";
}

function ChatMessage({ message, sender }: Props) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: sender === "user" ? "flex-end" : "flex-start",
        marginBottom: "16px",
      }}
    >
      <div
        style={{
          maxWidth: "75%",
          padding: "12px",
          borderRadius: "10px",
          background: sender === "user" ? "#2563eb" : "#e5e7eb",
          color: sender === "user" ? "white" : "black",
        }}
      >
        {message}
      </div>
    </div>
  );
}

export default ChatMessage;
