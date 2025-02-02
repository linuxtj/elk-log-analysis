# ELK Stack Log Analysis Platform

## Overview
A scalable, real-time log analysis platform built with the ELK (Elasticsearch, Logstash, Kibana) Stack. This project demonstrates the implementation of a production-grade logging system with real-time visualization and analysis capabilities.

![ELK Stack Architecture](https://via.placeholder.com/800x400?text=ELK+Stack+Architecture)

## Key Features
- Real-time log ingestion and processing
- Multi-threaded log simulation for testing
- Custom Logstash parsing patterns
- Interactive Kibana dashboards
- Docker-based deployment
- Scalable architecture
- Comprehensive monitoring

## Tech Stack
- Elasticsearch 8.12.0: Search and analytics engine
- Logstash 8.12.0: Log collection and processing
- Kibana 8.12.0: Visualization platform
- Python 3.x: Log simulation
- Docker & Docker Compose: Containerization
- TCP Socket Communication

## Prerequisites
- Docker and Docker Compose
- Python 3.x
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/linuxtj/elk-log-analysis.git
cd elk-log-analysis
```

2. Start the ELK Stack:
```bash
docker-compose up -d
```

3. Run the log generator:
```bash
cd sample-app
pip install -r requirements.txt
python log_generator.py
```

4. Access Kibana at http://localhost:5601

## Project Structure
```
elk-log-analysis/
├── docker-compose.yml          # Docker composition configuration
├── config/                     # Configuration files
│   ├── elasticsearch/         
│   ├── logstash/              
│   └── kibana/                
├── sample-app/                 # Log generator application
└── dashboards/                # Kibana dashboard exports
```

## Configuration
- Elasticsearch: `config/elasticsearch/elasticsearch.yml`
- Logstash: `config/logstash/pipeline/logstash.conf`
- Kibana: `config/kibana/kibana.yml`

## Monitoring & Visualization
The project includes pre-configured Kibana dashboards for:
- Log level distribution
- Service activity monitoring
- Error rate tracking
- Performance metrics

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
