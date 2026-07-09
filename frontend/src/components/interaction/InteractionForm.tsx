import { useSelector } from "react-redux";
import type { RootState } from "../../redux/store";

import "./InteractionForm.css";

import FormField from "./FormField";
import TextAreaField from "./TextAreaField";
import SentimentSelector from "./SentimentSelector";

import { createInteraction } from "../../services/interactionService";

function InteractionForm() {
  const interaction = useSelector((state: RootState) => state.interaction);

  const handleSave = async () => {
    try {
      await createInteraction({
        hcp_name: interaction.hcpName,
        interaction_type: interaction.interactionType,
        date: interaction.date,
        time: interaction.time,
        attendees: interaction.attendees,
        topics_discussed: interaction.topicsDiscussed,
        materials_shared: interaction.materialsShared,
        samples_distributed: interaction.samplesDistributed,
        sentiment: interaction.sentiment,
        outcomes: interaction.outcomes,
        follow_up_actions: interaction.followUpActions,
      });

      alert("Interaction saved successfully!");
    } catch (error) {
      console.error(error);
      alert("Failed to save interaction.");
    }
  };

  return (
    <div className="interaction-form">
      <h2>Interaction Details</h2>

      <FormField label="HCP Name" value={interaction.hcpName} />

      <FormField label="Interaction Type" value={interaction.interactionType} />

      <FormField label="Date" value={interaction.date} />

      <FormField label="Time" value={interaction.time} />

      <TextAreaField label="Attendees" value={interaction.attendees} />

      <TextAreaField
        label="Topics Discussed"
        value={interaction.topicsDiscussed}
      />

      <TextAreaField
        label="Materials Shared"
        value={interaction.materialsShared}
      />

      <TextAreaField
        label="Samples Distributed"
        value={interaction.samplesDistributed}
      />

      <SentimentSelector value={interaction.sentiment} />

      <TextAreaField label="Outcomes" value={interaction.outcomes} />

      <TextAreaField
        label="Follow-up Actions"
        value={interaction.followUpActions}
      />

      <button className="save-button" onClick={handleSave}>
        Save Interaction
      </button>
    </div>
  );
}

export default InteractionForm;
