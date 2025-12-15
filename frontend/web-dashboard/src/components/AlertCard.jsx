export default function AlertCard({ risk }) {
    return (
      <div style={{ color: risk > 0.7 ? "red" : "green" }}>
        Failure Risk: {risk}
      </div>
    );
  }
  