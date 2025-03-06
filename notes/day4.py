docker container create --name {{containerName}} 

{% if ports %}
    {% for port in ports %}
        -p {{port}}
    {% endfor %}
{% endif %}

{{image}}:{{image}}