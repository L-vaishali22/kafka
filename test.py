from confluent_kafka.admin import AdminClient

try:
    admin = AdminClient({'bootstrap.servers': 'localhost:9092'})
    topics = admin.list_topics(timeout=5)
    print("✅ Connected!")
    print("Topics:", list(topics.topics.keys()))
except Exception as e:
    print("❌ Error:", e)