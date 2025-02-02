# sample-app/log_generator.py
import random
import time
import json
import socket
import datetime
from threading import Thread

class LogGenerator:
    def __init__(self):
        self.services = ['user-service', 'auth-service', 'payment-service', 'order-service']
        self.log_levels = ['INFO', 'WARN', 'ERROR', 'DEBUG']
        self.message_templates = {
            'INFO': [
                'Request processed successfully',
                'User authentication successful',
                'Payment transaction completed',
                'Order created successfully'
            ],
            'WARN': [
                'High API latency detected',
                'Rate limit approaching threshold',
                'Database connection pool running low',
                'Cache miss rate increasing'
            ],
            'ERROR': [
                'Database connection failed',
                'API request timeout',
                'Invalid authentication token',
                'Payment processing failed'
            ],
            'DEBUG': [
                'Processing request parameters',
                'Validating user input',
                'Checking cache status',
                'Executing database query'
            ]
        }

    def generate_log(self):
        service = random.choice(self.services)
        log_level = random.choice(self.log_levels)
        message = f"{log_level} [{service}] {random.choice(self.message_templates[log_level])}"
        
        log_entry = {
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'service': service,
            'level': log_level,
            'message': message
        }
        return json.dumps(log_entry)

    def send_log(self, sock):
        while True:
            log = self.generate_log()
            sock.send((log + '\n').encode())
            time.sleep(random.uniform(0.1, 2))

if __name__ == '__main__':
    generator = LogGenerator()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect(('localhost', 5000))
        print("Connected to Logstash")
        
        # Start multiple threads to simulate different services
        for _ in range(4):
            thread = Thread(target=generator.send_log, args=(sock,))
            thread.daemon = True
            thread.start()
        
        # Keep main thread running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping log generator...")
    finally:
        sock.close()
