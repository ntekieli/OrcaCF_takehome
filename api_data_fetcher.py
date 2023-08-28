import requests
import pandas as pd

# Define the API endpoint
agency_str = ["DOE", "NSF", "USDA", "EPA"]
base_endpoint = "https://www.sbir.gov/api/awards.json"

# Define a list to store all data
all_data = []

# Define a variable to track the starting offset
offset = 0

# Define the number of rows per request
rows_per_request = 100  # You can adjust this value as needed

while offset < 15000:
    print(offset)
    # Update the endpoint to include the rows and start parameters
    endpoint = f"{base_endpoint}?start={offset}"
    
    # Fetch data from the API
    response = requests.get(endpoint)
    data = response.json()

    # Check if data is returned
    if not data or not isinstance(data, list):
        break  # Exit the loop if no more data is available

    all_data.extend(data)  # Add the fetched data to the all_data list
    offset += rows_per_request  # Increment the offset for the next request


# Define a list to store filtered data
filtered_data = []

# Extract relevant data from each award
for item in all_data:
    if item.get("agency", "") in agency_str:
        award_info = {
            "Firm": item.get("firm", ""),
            "Award Title": item.get("award_title", ""),
            "Agency": item.get("agency", ""),
            "Branch": item.get("branch", ""),
            "Phase": item.get("phase", ""),
            "Award Amount": item.get("award_amount", ""),
            "Award Year": item.get("award_year", ""),
            "Proposal Award Date": item.get("proposal_award_date", ""),
            "Abstract": item.get("abstract", ""),
            "Number of Employees": item.get("number_employees", ""),
            "Hubzone Owned": item.get("hubzone_owned", ""),
            "Socially Economically Disadvantaged": item.get("socially_economically_disadvantaged", ""),
            "Women Owned": item.get("women_owned", ""),
        }

        filtered_data.append(award_info)

# Convert the filtered data to a DataFrame
df = pd.DataFrame(filtered_data)

# Save the data to a CSV file
df.to_csv("sbir_awards.csv", index=False)

# Optionally, view the first few rows of the DataFrame
print(df.head())
print(df.shape)
print(df['Agency'].unique())