create table vehicles (
  id uuid primary key default gen_random_uuid(),
  vin text,
  owner_id text
);
