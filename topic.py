from confluent_kafka.admin import AdminClient, NewTopic

admin = AdminClient({'bootstrap.servers': 'localhost:9092'})

# Naya topic banao
try:
  new_topic = NewTopic('my-first-topic2', num_partitions=1, replication_factor=1)
  admin.create_topics([new_topic])

  print("✅ Topic ban gaya!")
except:
   print("error")
# Verify karo
topics = admin.list_topics(timeout=5)
print("Topics:", list(topics.topics.keys()))
