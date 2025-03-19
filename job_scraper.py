import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_govt_jobs():
    url = "https://www.upsc.gov.in/recruitment-advertisement"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job in soup.find_all("tr")[1:6]:  # Fetch first 5 job listings
        cols = job.find_all("td")
        if len(cols) > 1:
            job_title = cols[1].text.strip()
            apply_link = cols[1].find("a")["href"] if cols[1].find("a") else "#"
            jobs.append({"Title": job_title, "Apply Link": apply_link})
    
    return pd.DataFrame(jobs)
