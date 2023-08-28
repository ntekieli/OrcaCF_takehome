import requests
from bs4 import BeautifulSoup
import re

URL = "https://arpa-e.energy.gov/technologies/projects"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

print('got the soup')

# Extract all row items
rows = soup.find_all('div', class_='row', limit=5)

projects_data = []

for row in rows:
    project_info = {}
    
    # Extracting Status, State, Project Term, Program, and Award
    labels_section = row.find('p', class_='labels-section')
    if labels_section:
        status = labels_section.find('span', string='Status:').find_next_sibling('span').text if labels_section.find('span', string='Status:') else None
        state = labels_section.find('span', string='State:').find_next_sibling('span').text if labels_section.find('span', string='State:') else None
        project_term_start = labels_section.find('span', string='Project Term:').find_next_sibling('time').text if labels_section.find('span', string='Project Term:') else None
        project_term_end = labels_section.find('time', datetime=True).find_next_sibling('time').text if labels_section.find('time', datetime=True) else None
        program = labels_section.find('span', string='Program:').find_next_sibling('span').text if labels_section.find('span', string='Program:') else None
        
        # award = labels_section.find('span', string='Award: ').find_next_sibling('span').text if labels_section.find('span', string='Award: ') else None
        
        award_match = re.search(r'\$\d+,\d+', labels_section.text)
        award = award_match.group(0) if award_match else None

        project_info.update({
            'Status': status,
            'State': state,
            'Project Term Start': project_term_start,
            'Project Term End': project_term_end,
            'Program': program,
            'Award': award
        })
    
    # Extracting Organization Name and Project Title
    col_data = row.find('div', class_='col-xs-12 col-sm-9')
    if col_data:
        organization_name = col_data.find('h2').text if col_data.find('h2') else None
        project_title = col_data.find('a').text if col_data.find('a') else None
        
        project_info.update({
            'Organization Name': organization_name,
            'Project Title': project_title
        })
    
    projects_data.append(project_info)

# Print the extracted data
for project in projects_data:
    print(project)
