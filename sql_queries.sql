-- Import the CSV into a table named network_traffic.
-- Executive KPIs
SELECT COUNT(*) total_records,
 SUM(CASE WHEN UPPER(label)<>'BENIGN' THEN 1 ELSE 0 END) suspicious_records
FROM network_traffic;

-- Activity category comparison
SELECT label, COUNT(*) records, AVG(packets) avg_packets, AVG(bytes) avg_bytes
FROM network_traffic GROUP BY label ORDER BY records DESC;

-- Suspicious activity by destination port
SELECT dst_port, COUNT(*) records
FROM network_traffic WHERE UPPER(label)<>'BENIGN'
GROUP BY dst_port ORDER BY records DESC;

-- Daily trend
SELECT DATE(timestamp) activity_date, COUNT(*) total_records,
 SUM(CASE WHEN UPPER(label)<>'BENIGN' THEN 1 ELSE 0 END) suspicious_records
FROM network_traffic GROUP BY DATE(timestamp) ORDER BY activity_date;
