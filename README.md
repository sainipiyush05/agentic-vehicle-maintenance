## Agentic-Vehicale-maintenance

agentic-vehicle-maintenance/
│
├── frontend/
│   ├── web-dashboard/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── VehicleCard.jsx
│   │   │   │   ├── AlertCard.jsx
│   │   │   │   └── ScheduleTable.jsx
│   │   │   ├── pages/
│   │   │   │   ├── Login.jsx
│   │   │   │   ├── OwnerDashboard.jsx
│   │   │   │   ├── ServiceCenterDashboard.jsx
│   │   │   │   └── ManufacturerDashboard.jsx
│   │   │   ├── services/
│   │   │   │   └── supabaseClient.js
│   │   │   ├── utils/
│   │   │   │   └── authHelpers.js
│   │   │   └── App.jsx
│   │   └── package.json
│   │
│   └── voice-interface/
│       ├── speech_to_text.py
│       └── agent_voice_handler.py
│
├── backend/
│   ├── api/
│   │   ├── main.py                  # FastAPI entry
│   │   ├── config/
│   │   │   ├── env.py
│   │   │   └── settings.py
│   │   │
│   │   ├── db/
│   │   │   ├── supabase.py           # Supabase client
│   │   │   └── schemas.py            # Pydantic models
│   │   │
│   │   ├── routes/
│   │   │   ├── vehicles.py
│   │   │   ├── telematics.py
│   │   │   ├── predictions.py
│   │   │   ├── scheduling.py
│   │   │   └── feedback.py
│   │   │
│   │   ├── agents/
│   │   │   ├── master_agent.py       # Orchestrator
│   │   │   ├── prediction_agent.py
│   │   │   ├── scheduling_agent.py
│   │   │   ├── rca_agent.py
│   │   │   └── ueba_agent.py
│   │   │
│   │   ├── ml/
│   │   │   ├── model.py
│   │   │   ├── feature_engineering.py
│   │   │   └── inference.py
│   │   │
│   │   ├── services/
│   │   │   ├── notification_service.py
│   │   │   └── logging_service.py
│   │   │
│   │   └── utils/
│   │       ├── auth.py
│   │       └── validators.py
│   │
│   └── requirements.txt
│
├── supabase/
│   ├── migrations/
│   │   ├── 001_init_tables.sql
│   │   ├── 002_rls_policies.sql
│   │   └── 003_triggers.sql
│   │
│   ├── edge-functions/
│   │   ├── auto_schedule/
│   │   │   └── index.ts
│   │   ├── send_alert/
│   │   │   └── index.ts
│   │   └── ueba_monitor/
│   │       └── index.ts
│   │
│   └── seed.sql
│
├── docs/
│   ├── architecture.md
│   ├── agent-flow.md
│   └── api-contracts.md
│
├── .env.example
├── .gitignore
├── README.md
└── docker-compose.yml


Agentic AI platform for predictive vehicle maintenance using Supabase, FastAPI, and ML.

## Run Backend
pip install -r backend/requirements.txt
uvicorn backend.api.main:app --reload

## Run Frontend
cd frontend/web-dashboard
npm install
npm run dev


uvicorn backend.api.main:app --reload