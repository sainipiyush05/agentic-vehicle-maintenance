import { useEffect, useState } from "react";
import { supabase } from "../services/supabaseClient";
import VehicleCard from "../components/VehicleCard";

export default function OwnerDashboard() {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    supabase
      .from("vehicles")
      .select("*")
      .then(({ data }) => setVehicles(data));
  }, []);

  return (
    <>
      <h2>Your Vehicles</h2>
      {vehicles?.map(v => (
        <VehicleCard key={v.id} vin={v.vin} />
      ))}
    </>
  );
}
