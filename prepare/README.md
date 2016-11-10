# Erstellung des konfigurierten Keycloak Images

Die Hobbit GUI benutzt Keycloak 2.3 für Identity and Access Management.
Hier wird beschrieben, wie das Docker Image vorbereitet wird.

## Docker Image erstellen
```
docker pull jboss/keycloak:2.3.0.Final
docker run -d --name keycloak -p 8181:8080 jboss/keycloak:2.3.0.Final
docker exec keycloak keycloak/bin/add-user-keycloak.sh --user admin --password H16obbit
docker restart keycloak
```

## Erstellung Hobbit Realm / Benutzer / Gruppen / Clients
Für die automatisierte Erstellung des Hobbit Realm ist zunächst ein Client in der Master Realm anzulegen:

- einloggen in keycloak (http://localhost:8181/auth/admin  user: admin, password: H16obbit)
- im master realm test client anlegen
   - Client ID: test
   - Access Type: confidential
   - Redirect URI: irgendwas (z.B. http://localhost:8080)
   
   - Client Secret kopieren und in der Datei `init-keycloak.py` ersetzen

- `init-keycloak.py` ausführen
  (benötigt requests, unter Centos mit `yum install python-requests` installieren oder `pip install requests`)

## manuelles Erstellen der Rollen-Zuordnung
Erstellung der Rollenzuordnung fehlt noch im Python-Skript und ist deshalb manuell zu erstellen:
- einloggen in Keycloak (http://localhost:8181/auth/admin  user: admin, password: H16obbit)
- Hobbit Realm auswählen
- Manage Users
- View All Users
- Für jeden Benutzer
  - Role Mappings setzen
    - admin: benchmark-provider, challenge-organiser, guest, system-provider
    - benchmark-provider: benchmark-provider
    - challenge-organiser: challenge-organiser
    - guest: guest
    - system-provider: system-provider


