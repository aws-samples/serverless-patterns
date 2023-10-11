package com.aws.cqrs.infrastructure.redis;

import com.aws.cqrs.domain.model.Order;
import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.Jedis;

public class OrderReadRepository {

    HostAndPort hostAndPort = new HostAndPort(System.getenv("redisClusterEndpoint"), 6379);

    public void saveOrder(Order order) {
        try (Jedis jedis = new Jedis(hostAndPort)) {
            jedis.set(order.getOrderId(), order.toString());
        }
    }

    public String getOrder(String orderId) {
        try (Jedis jedis = new Jedis(hostAndPort)) {
            System.out.println(jedis.get(orderId));
            return jedis.get(orderId);
        }
    }
}
