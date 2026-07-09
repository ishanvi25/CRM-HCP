interface Props {
  value?: string;
}

function SentimentSelector({ value = "" }: Props) {
  return (
    <div className="form-group">
      <label>Sentiment</label>

      <div className="sentiment-group">
        <label>
          <input type="radio" checked={value === "Positive"} readOnly />
          Positive
        </label>

        <label>
          <input type="radio" checked={value === "Neutral"} readOnly />
          Neutral
        </label>

        <label>
          <input type="radio" checked={value === "Negative"} readOnly />
          Negative
        </label>
      </div>
    </div>
  );
}

export default SentimentSelector;
