## Agentic-Vehicle-Maintenance

## 🧠 System Overview

The platform consists of:
- **Frontend**: React-based dashboards for owners, service centers, and manufacturers
- **Backend**: FastAPI-powered agentic system for predictions, RCA, and scheduling
- **Supabase**: Database, auth, edge functions, and triggers
- **Voice Interface**: Speech-to-text driven agent interaction

---



## 📁 Project Structure

```text
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
│   │   ├── main.py
│   │   ├── config/
│   │   ├── db/
│   │   ├── routes/
│   │   ├── agents/
│   │   ├── ml/
│   │   ├── services/
│   │   └── utils/
│   └── requirements.txt
│
├── supabase/
│   ├── migrations/
│   ├── edge-functions/
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
