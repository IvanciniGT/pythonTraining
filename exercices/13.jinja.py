# In order to use jinja... first thing is to install it:
# $ python -m pip install jinja2

# Then... we have to import the module
from jinja2 import Template, Environment, FileSystemLoader

# Jinja is a template engine for python
# It allows us to define templates with not only placeholders but also control structures (loops, conditionals, etc)
# Then we can render the template with actual data that we want to use in the template

jinja_template_text = """
Hi {{ name | default("there") }}!

This is a message from the {{ company  | upper }} company.
We are using jinja to render this message.

{%- if age >= 21 %}
You are old enough to drive a car and vote and drink alcohol.
{% elif age >= 18 %}
You are old enough to drive a car and vote.
{% elif age >= 16 %}
You are old enough to drive a car.
{% else %}
You are too young to drive a car. Come back in {{ 16 - age }} years.
{% endif -%}

Thanks for your attention.
See you soon!
"""

# Jinja defines a class called Template
# We can create an instance of that class with the template text
jinja_template = Template(jinja_template_text)

my_actual_data = {
    #"name": "Brenda",
    "company": "Your Company",
    "age": 21
}

# We can render the template with the actual data
rendered_text = jinja_template.render(my_actual_data)

print(rendered_text)

# Right here we have used jinja to write the contents of an email.
# We can also:
# - Write the contents of a file (config files, etc)
# - Write the contents of a log file
# - Create the command that needs to be executed under certain conditions


docker_command = """docker container create --name {{containerName}} {% if ports -%}
    {%- for port in ports %}-p {{port}} {% endfor -%}
{%- endif -%}

{{image}}:{{tag}}"""

docker_template = Template(docker_command)

docker_data = {
    "containerName": "my_container",
    "ports": [ "80:80", "443:443" ],
    "image": "nginx",
    "tag": "1.24"
}

docker_command = docker_template.render(docker_data)

print(docker_command)


## In order to read the template text from a file... 
# We could just read that text, as any other text file
# And then create the jinja template with that text

# As an alternative... we can use the FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("my_template.j2")
docker_command = template.render(docker_data)

print(docker_command)

# https://j2live.ttl255.com/
# That kind of web pages allow us to test jinja templates online