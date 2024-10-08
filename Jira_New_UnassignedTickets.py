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
for issue in issues['issues']:
    issue_key = issue["key"]
    summary = issue["fields"]["summary"]
    print(f'{issue_key}: {summary}')