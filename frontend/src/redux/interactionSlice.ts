import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { Interaction } from "../types/interaction";

const initialState: Interaction = {
  hcpName: "",
  interactionType: "",
  date: "",
  time: "",
  attendees: "",
  topicsDiscussed: "",
  materialsShared: "",
  samplesDistributed: "",
  sentiment: "",
  outcomes: "",
  followUpActions: "",
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    updateInteraction: (state, action: PayloadAction<Partial<Interaction>>) => {
      Object.assign(state, action.payload);
    },

    clearInteraction: () => initialState,
  },
});

export const { updateInteraction, clearInteraction } = interactionSlice.actions;

export default interactionSlice.reducer;
