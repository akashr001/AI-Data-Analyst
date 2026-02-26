from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

from engine import app as agent_graph

api = FastAPI(title="AI Data Analyst")

# ---------------- CSV LOADER ----------------

def read_csv_safely(file):
    for enc in ["utf-8", "latin1", "ISO-8859-1"]:
        try:
            file.seek(0)
            return pd.read_csv(
                file,
                encoding=enc,
                engine="python",
                on_bad_lines="skip"
            )
        except Exception:
            continue
    raise ValueError("Invalid CSV file")

# ---------------- BASIC ANALYTICS (FIXED) ----------------

def basic_analytics(df: pd.DataFrame) -> dict:
    analytics = {}

    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        analytics[col] = {
            "mean": float(round(df[col].mean(), 2)),
            "median": float(round(df[col].median(), 2)),
            "min": float(df[col].min()),
            "max": float(df[col].max())
        }

    for col in df.select_dtypes(include=["object"]).columns:
        analytics[col] = {
            "mode": str(df[col].mode().iloc[0]) if not df[col].mode().empty else None,
            "unique_values": int(df[col].nunique())
        }

    return analytics

# ---------------- FRONTEND ----------------

api.mount("/static", StaticFiles(directory="../frontend"), name="static")

@api.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("../frontend/index.html", encoding="utf-8") as f:
        return f.read()

# ---------------- ANALYZE ----------------

@api.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):
    df = read_csv_safely(file.file)

    analytics = basic_analytics(df)

    result = agent_graph.invoke({
        "json_data": df.head(10).to_dict(orient="records"),
        "analytics": analytics
    })

    return {
        "plan": result["plan"],
        "understanding": result["understanding"],
        "analysis": result["analysis"],
        "monitor_feedback": result["monitor_feedback"],
        "report": result["report"],
        "analytics": analytics
    }
