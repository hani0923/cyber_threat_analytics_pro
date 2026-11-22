# Cyber Threat Intelligence & Analytics Dashboard

A portfolio project combining Python, SQL, and Power BI to analyze network-flow records.

**Dataset note:** The included CSV is synthetic demo data, not live monitoring or verified threat intelligence. For a research-grade version, replace it with a properly attributed public dataset such as CICIDS2017 and document its source/license.

## Run
```bash
pip install -r requirements.txt
python src/analyze.py
```
Generated summaries and chart are saved in `outputs/`.

## Power BI dashboard
Import `data/network_traffic_sample.csv` and create:
- KPI cards: total records, suspicious records, suspicious share
- Line chart: daily total vs suspicious records
- Bar chart: records by activity label
- Bar chart: suspicious records by destination port
- Slicers: date, protocol, label

## Skills demonstrated
Data cleaning, exploratory analysis, SQL aggregation, KPI design, trend analysis, and dashboard storytelling.

## Resume description
Built a cybersecurity analytics workflow using Python, SQL, and Power BI to summarize network-flow records and visualize activity-category, time, and destination-port trends. Only report results you personally verified.
