import api from "./api";

export async function sendMessage(message: string) {
  const response = await api.post("/chat/", {
    message,
  });

  return response.data;
}

export async function getInteractions() {
  const response = await api.get("/interactions/");

  return response.data;
}
