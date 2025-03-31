kubectl exec -it redis-cluster-0 -- redis-cli --cluster create \
    redis-cluster-0.redis-service:6379 \
    redis-cluster-1.redis-service:6379 \
    redis-cluster-2.redis-service:6379 \
    redis-cluster-3.redis-service:6379 \
    redis-cluster-4.redis-service:6379 \
    redis-cluster-5.redis-service:6379 \
    --cluster-replicas 1
