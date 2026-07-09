interface Props {
  label: string;
  value?: string;
}

function TextAreaField({ label, value = "" }: Props) {
  return (
    <div className="form-group">
      <label>{label}</label>

      <textarea
        value={value}
        placeholder="AI will populate this field"
        readOnly
      />
    </div>
  );
}

export default TextAreaField;
