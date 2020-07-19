from atlassian import Jira

jira = Jira(
    url='https://diwo.atlassian.net/browse/DCP-911',
    username='ddunga@getdiwo.com',
    password='Apple@99')

# rkGBVqFzYX3SexlOGO3K7927

JQL = 'project = DEMO AND status IN ("To Do", "In Progress") ORDER BY issuekey'
data = jira.jql(JQL)
print(data)