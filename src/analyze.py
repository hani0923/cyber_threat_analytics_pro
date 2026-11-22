from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/"data/network_traffic_sample.csv", parse_dates=["timestamp"])
df = df.drop_duplicates().dropna()
df["suspicious"] = df["label"].str.upper().ne("BENIGN")
out = ROOT/"outputs"
out.mkdir(exist_ok=True)

kpis = pd.DataFrame([{
    "total_records": len(df),
    "suspicious_records": int(df.suspicious.sum()),
    "suspicious_share_pct": round(df.suspicious.mean()*100, 2),
    "protocols": df.protocol.nunique(),
    "destination_ports": df.dst_port.nunique()
}])
kpis.to_csv(out/"kpi_summary.csv", index=False)
df.groupby("label").agg(records=("label","size"), avg_packets=("packets","mean"), avg_bytes=("bytes","mean")).round(2).to_csv(out/"category_summary.csv")
daily = df.assign(date=df.timestamp.dt.date).groupby("date").agg(total=("label","size"), suspicious=("suspicious","sum"))
daily.to_csv(out/"daily_trend.csv")
df.groupby("dst_port").agg(records=("label","size"), suspicious=("suspicious","sum")).sort_values("suspicious",ascending=False).to_csv(out/"port_summary.csv")
fig, ax = plt.subplots(1,2,figsize=(11,4))
df.label.value_counts().plot.bar(ax=ax[0],title="Records by activity category")
daily.plot(ax=ax[1],title="Daily activity trend")
plt.tight_layout(); plt.savefig(out/"analytics_overview.png",dpi=150)
print(kpis.to_string(index=False))
print("Done: see the outputs folder.")
