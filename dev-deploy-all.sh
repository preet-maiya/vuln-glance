
# RabbitMQ deployment steps
kubectl apply -f rabbitmq/cluster-operator.yaml
kubectl apply -f rabbitmq/rabbitmq.yaml
kubectl port-forward --address 0.0.0.0 service/rabbitmq 5672:5672 &