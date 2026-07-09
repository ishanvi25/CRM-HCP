export interface Interaction {
  hcpName: string;
  interactionType: string;
  date: string;
  time: string;
  attendees: string;
  topicsDiscussed: string;
  materialsShared: string;
  samplesDistributed: string;
  sentiment: "Positive" | "Neutral" | "Negative" | "";
  outcomes: string;
  followUpActions: string;
}
