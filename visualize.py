import datetime
import pytz

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import pandas as pd

df = pd.read_csv("speedtest.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df[df["timestamp"] >= datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=24)]
df.set_index("timestamp", inplace=True)

hourly_avg_download = df["download_bandwidth"].resample("h").mean()
hourly_avg_upload = df["upload_bandwidth"].resample("h").mean()
hourly_avg_ping = df["ping_latency"].resample("h").mean()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

hourly_avg_download.plot(kind="line", marker="o", ax=ax1, label="Download Bandwidth")
hourly_avg_upload.plot(kind="line", marker="o", ax=ax1, label="Upload Bandwidth")
ax1.set_ylabel("Bandwidth (GB/s)")

hourly_avg_ping.plot(kind="line", color="red", marker="s", ax=ax2, label="Ping Latency")
ax2.set_ylabel("Ping Latency (ms)")
ax2.set_xlabel("Hour")

formatter1 = ScalarFormatter(useMathText=True)
formatter1.set_scientific(True)
formatter1.set_powerlimits((8, 8))  # Force scientific notation for 1x10^8
ax1.yaxis.set_major_formatter(formatter1)

ax1.set_title("Hourly Average Bandwidth and Ping Latency")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="best")

ax1.grid(True)
ax2.grid(True)
plt.tight_layout()
plt.savefig("plots/latest.png")
plt.savefig(f"plots/{datetime.datetime.now().strftime('%Y-%m-%d')}.png")
