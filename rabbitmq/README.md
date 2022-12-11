# RabbitMQ kubernetes deployment

Both the yaml files are reference from the tutorial at - https://www.rabbitmq.com/kubernetes/operator/quickstart-operator.html

To deploy the rabbitmq service run ```make deploy``` and once the services are up run ```make createuser``` to create new user and set vhost permission for it. This user is required by the API's celery service to connect to rabbitmq. 

### Logging
to check logs run the following command 
``` sh
kubectl logs pod/rabbitmq-server-0
```

### Use
To use within another service, use the host as `rabbitmq` and port `5672` with user name ```vuln_glance``` and password as ```password```