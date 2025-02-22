# NTP Monitor ⏰
**Solution de surveillance NTP professionnelle pour Alpine Linux**

[![CI/CD](https://github.com/valorisa/ntp-monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/valorisa/ntp-monitor/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-red)](https://opensource.org/licenses/MIT)

![Architecture NTP](https://via.placeholder.com/800x400.png?text=NTP+Monitoring+Architecture)

## Fonctionnalités Clés ✨
- Surveillance multi-serveurs avec basculement automatique
- Métriques Prometheus (offset, stratum, jitter)
- Conformité RFC 1305
- Sécurité NTS (Network Time Security)
- Dashboard Grafana intégré

## Installation 🚀
Sur Alpine Linux
```bash
apk add python3 py3-pip gcc musl-dev
git clone https://github.com/valorisa/ntp-monitor.git
cd ntp-monitor
pip install -r requirements.txt
```


## Configuration ⚙️
config/servers.yaml
servers:
```
host: pool.ntp.org
stratum: 2

host: time.google.com
stratum: 1

alert_thresholds:
offset_ms: 50
delay_ms: 200
```

## Test Rapide 🧪
lancer la commande : 
```bash
python
```

```python
>>> from src.core.ntp_client import NTPClient
>>> client = NTPClient()
>>> print(client.get_servers())
['pool.ntp.org', 'time.google.com']

```


## Utilisation 💻
Mode standard
```
python -m src --config config/servers.yaml
```

Avec monitoring
```
python -m src --prometheus-port 9100 --web-dashboard 8000
```

## Déploiement 🐳
Docker
```
docker run -d
-p 8000:8000
-v $(pwd)/config:/app/config
ghcr.io/valorisa/ntp-monitor:latest
```
Kubernetes
```
helm install ntp-monitor ./helm-chart
--set replicaCount=3
```


## Structure du Projet 📂
```
ntp-monitor/
├── src/
│ ├── core/ # Client NTP et algorithmes RFC
│ ├── adapters/ # Connecteurs Prometheus/Grafana
│ └── utils/ # Helpers de configuration
├── config/ # Fichiers YAML
└── tests/ # Tests unitaires et d'intégration
```

## Contribution 🤝
1. Forkez le dépôt
2. Créez une feature branch :
```
git checkout -b feat/nouvelle-fonctionnalite
```
4. Lancez les tests :
```
pytest --cov=src --cov-report=html
```
5. Ouvrez une Pull Request

## Sécurité 🔐
```python
from cryptography.hazmat.primitives import hashes, hmac

Génération de clé HMAC-SHA256
h = hmac.HMAC(key, hashes.SHA256())
h.update(ntp_packet)
signature = h.finalize()
```

## Licence 📄
Ce projet est sous licence MIT - voir [LICENSE](LICENSE) pour plus de détails.

---
**Maintenu par valorisa** - [Documentation Technique](docs/API.md)
