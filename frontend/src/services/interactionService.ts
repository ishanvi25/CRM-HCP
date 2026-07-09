import axios from "axios";

const API = "http://127.0.0.1:8000/interactions";

export const getInteractions = async () => {
  const response = await axios.get(API);
  return response.data;
};

export const createInteraction = async (data: any) => {
  const response = await axios.post(API + "/", data);
  return response.data;
};

export const updateInteraction = async (id: number, data: any) => {
  const response = await axios.put(`${API}/${id}`, data);
  return response.data;
};

export const deleteInteraction = async (id: number) => {
  const response = await axios.delete(`${API}/${id}`);
  return response.data;
};
