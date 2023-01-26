import requests

job_name = ['TechWorkshop_orch','TechWorkshop_orch2']

for each in job_name:
  r = requests.post('http://'+env_url+'/rest/v1/group/name/'+group_name+'Matillion/project/name/'+project_name+'/version/name/default/job/name/'+each+'/run?environmentName='+demo_env, 
                 auth=(ec2_username,ec2_password))
                 print(r.status_code)
                 print(r.text)
