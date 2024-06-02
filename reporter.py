# reporter.py

def generate_report(vulnerabilities):
    with open('report.txt', 'w') as report_file:
        for vulnerability in vulnerabilities:
            report_file.write(f"{vulnerability}\n")
