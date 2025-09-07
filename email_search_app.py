
import streamlit as st
from datetime import datetime

# Sample email data
emails = [
    {"company": "Range Resources Corporation", "name": "David Lademan", "subject": "Low-Carbon Gas", "date": "2023-10-01", "region": "North America", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwBI_gAA"},
    {"company": "JBS/Seara", "name": "Jose Roberto Gomes", "subject": "Meals", "date": "2023-10-02", "region": "South America", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwBEMwAA"},
    {"company": "Removall Carbon", "name": "David Lademan", "subject": "Carbon", "date": "2023-10-03", "region": "Global", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAH2wAA"},
    {"company": "Voyager Midstream", "name": "David Lademan", "subject": "Natural Gas", "date": "2023-10-04", "region": "North America", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAHkgAA"},
    {"company": "IOC", "name": "David Lademan", "subject": "Ammonia", "date": "2023-10-05", "region": "Asia", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAGrwAA"},
    {"company": "Nobel Trading", "name": "David Lademan", "subject": "Urea", "date": "2023-10-06", "region": "Europe", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAGiAAA"},
    {"company": "Matium", "name": "David Lademan", "subject": "Recycled Polymers", "date": "2023-10-07", "region": "North America", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAGgwAA"},
    {"company": "Atlas Agro", "name": "David Lademan", "subject": "Urea", "date": "2023-10-08", "region": "South America", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAGdAAA"},
    {"company": "Babcock & Wilcox", "name": "David Lademan", "subject": "Recycled Polymers", "date": "2023-10-09", "region": "North America", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAGcQAA"},
    {"company": "Aditya Birla", "name": "David Lademan", "subject": "Phosphates", "date": "2023-10-10", "region": "Asia", "id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AEH7NXaKMBUiFZnrJ1BkFOAAHzwAGPQAA"}
]

# Streamlit UI
st.title("🔍 SEIG Meeting Notes Search")

# Sidebar filters
company_filter = st.text_input("Search by Company Name")
subject_filter = st.text_input("Search by Subject")
date_filter = st.date_input("Filter by Date", value=None)
region_filter = st.selectbox("Filter by Region", options=["", "North America", "South America", "Europe", "Asia", "Global"])

# Filter logic
filtered_emails = []
for email in emails:
    if company_filter and company_filter.lower() not in email["company"].lower():
        continue
    if subject_filter and subject_filter.lower() not in email["subject"].lower():
        continue
    if date_filter and email["date"] != date_filter.strftime("%Y-%m-%d"):
        continue
    if region_filter and email["region"] != region_filter:
        continue
    filtered_emails.append(email)

# Display results
st.markdown(f"### Results ({len(filtered_emails)} found)")
for email in filtered_emails:
    st.markdown(f"**Company**: {email['company']}  ")
    st.markdown(f"**Name**: {email['name']}  ")
    st.markdown(f"**Subject**: {email['subject']}  ")
    st.markdown(f"**Date**: {email['date']}  ")
    st.markdown(f"**Region**: {email['region']}  ")
    st.markdown(f"[🔗 View Email](https://outlook.office365.com/mail/inbox/id/{email['id']})")
    st.markdown("---")
