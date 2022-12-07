deploy:
	kubectl apply -f cluster-operator.yaml
	kubectl apply -f rabbitmq.yaml

createuser:
	kubectl exec -it rabbitmq-server-0 -- rabbitmqctl add_user vuln_glance password
	kubectl exec -it rabbitmq-server-0 -- rabbitmqctl set_permissions -p / vuln_glance ".*" ".*" ".*"

stop:
	kubectl delete kubectl delete statefulset.apps/rabbitmq-server rabbitmqcluster.rabbitmq.com/rabbitmq
	kubectl delete --all all -n rabbitmq-system