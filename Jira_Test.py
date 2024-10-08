import requests
from atlassian import Jira

jira = Jira(
 
    url='https://devex-issuehub.at.sky/',
    username='pnt989',
    #pavithra.narayanamurthy@sky.uk
    password='HigiVBIes0gCxg0WmKex4BoJ1xDjG8dgSLH7QS',
    cloud=True)
jql_query ='project = CTR AND "Dev Teams Required" = "Eagle" AND  (status = "New" or status= "Open") AND assignee is EMPTY'
issues = jira.jql(jql_query)
dev_team_group = 'Eagle'
def get_group_members(group_name):
    url = f'https://devex-issuehub.at.sky/rest/api/2/group?groupname={group_name}'
    response = requests.get(url, auth=(jira.username, jira.password))

    if response.status_code == 200:
        return response.json().get('members', [])
    else:
        print(f"Failed to fetch group members: {response.status_code} - {response.text}")
        return []
try:
    team_members = get_group_members(dev_team_group)

    # Print team member usernames for testing
    print("Team Members in 'Eagle':")
    for member in team_members:
        print(f"Username: {member['name']}")  # Display only the username

    # Extract usernames of team members
    eagle_team_usernames = [member['name'] for member in team_members]
except Exception as e:
    print(f"An error occurred: {e}")
    
    #for issue in issues['issues']:
    #issue_key = issue["key"]
    #summary = issue["fields"]["summary"]
    
    
    #print(f'{issue_key}: {summary}')#/