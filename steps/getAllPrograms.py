import json

from behave import *
import requests

global response
url = "http://lms-backend-service.herokuapp.com/lms/"

@given(u'body specifications with a Service URL')
def step_impl(context):
   url = "http://lms-backend-service.herokuapp.com/lms/allPrograms"

@when(u'GET request is made')
def step_impl(context):
   context.response = requests.get(url+"/allPrograms")
   #json_response = json.loads(response.text)
  # context.response =response
   #print(json_response)



@then(u'Validate status code for getting all programs')
def step_impl(context):
   print(context.response.status_code)
   expected_status_code = 200 #context.
   assert expected_status_code == context.response.status_code