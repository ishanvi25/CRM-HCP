interface Props {
  label: string;
  value?: string;
}

function FormField({ label, value = "" }: Props) {
  return (
    <div className="form-group">
      <label>{label}</label>

      <input
        type="text"
        value={value}
        placeholder="AI will populate this field"
        readOnly
      />
    </div>
  );
}

export default FormField;
