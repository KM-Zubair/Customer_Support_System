import re

def parse_log(log_line):
    """
    Parses a single log line into a structured dictionary.
    """
    log_pattern = re.compile(
        r'\[(.*?)\] (\d+\.\d+\.\d+\.\d+) (\S+) (\S+) "(.*?)" "(.*?)"'
    )
    match = log_pattern.match(log_line)
    if match:
        return {
            "timestamp": match.group(1),
            "ip_address": match.group(2),
            "tls_version": match.group(3),
            "cipher_suite": match.group(4),
            "request": match.group(5),
            "response": match.group(6)
        }
    else:
        raise ValueError(f"Log line does not match pattern: {log_line}")

def preprocess_logs(logs):
    """
    Preprocesses raw log lines into structured JSON format.
    """
    structured_logs = []
    for log in logs:
        try:
            structured_logs.append(parse_log(log))
        except ValueError as e:
            print(f"Error parsing log: {e}")
    return structured_logs
