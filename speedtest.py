#!/usr/bin/env python3
"""Run speedtest-cli and save the results to a CSV file."""
import csv
import json
import pathlib
import subprocess


def flatten_json(record: dict, prefix: str = "", separator: str = "_") -> dict:
    data = {}
    for key, value in record.items():
        if prefix:
            key = f"{prefix}{separator}{key}"
        if isinstance(value, dict):
            child_data = flatten_json(value, prefix=key)
            data.update(child_data)
        else:
            data[key] = value
    return data


response_bytes = subprocess.check_output(["speedtest", "-f", "json", "--accept-license"])
response_json = json.loads(response_bytes)
response_dict = flatten_json(response_json)
headers = [
    "timestamp", "ping_jitter", "ping_latency", "ping_low", "ping_high", "download_bandwidth", "download_bytes",
    "download_elapsed", "download_latency_iqm", "download_latency_low", "download_latency_high",
    "download_latency_jitter", "upload_bandwidth", "upload_bytes", "upload_elapsed", "upload_latency_iqm",
    "upload_latency_low", "upload_latency_high", "upload_latency_jitter",
]
trimmed_dict = {key: response_dict.get(key, "") for key in headers}

path = pathlib.Path("/srv/isp-monitor/speedtest.csv")

with path.open("a", encoding="utf-8") as file:
    writer = csv.writer(file)
    if len(path.read_text(encoding="utf-8")) == 0:
        writer.writerow(headers)
    writer.writerow(trimmed_dict.values())
