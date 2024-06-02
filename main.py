# main.py

from crawler import crawl
from vulnerability_scanner import check_sql_injection, check_xss
from reporter import generate_report

def main(start_url):
    print(f"Starting crawl on: {start_url}")
    links = crawl(start_url)
    print(f"Found links: {links}")
    vulnerabilities = []

    for link in links:
        print(f"Checking link: {link}")
        if check_sql_injection(link):
            vulnerabilities.append(f"SQL Injection at {link}")
        if check_xss(link):
            vulnerabilities.append(f"XSS at {link}")

    
    generate_report(vulnerabilities)
    print("Scan complete. Report saved to report.txt.")

if __name__ == "__main__":
    main('https://0a400038039116aa81fb665800cf00c8.web-security-academy.net/')
