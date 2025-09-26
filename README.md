# Contact Form Application

## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the backend directory:
```env
HUBSPOT_ACCESS_TOKEN=your_hubspot_token_here
BASE_URL=https://api.hubapi.com/crm/v3/objects/contacts
CORS_ORIGINS=http://localhost:5173
CORS_METHODS=GET,POST,PUT,DELETE,OPTIONS
CORS_HEADERS=*
```

```bash
python main.py
```
Backend runs on: http://localhost:8000

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on: http://localhost:5173

