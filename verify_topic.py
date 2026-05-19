from confluent_kafka.admin import AdminClient
import time

admin = AdminClient({'bootstrap.servers': 'localhost:9092'})

# Thoda wait karo
time.sleep(2)

# Verify karo
topics = admin.list_topics(timeout=10)
print("Topics:", list(topics.topics.keys()))