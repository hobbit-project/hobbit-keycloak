# Information

This is the prepared Keycloak 2.3.0 Docker image for usage with the gui of the HOBBIT platform.

# build docker image

```bash
docker build -t hobbit-keycloak .
```

# set permissions for db directory
```bash
chmod 777 db
chmod 666 db/*
```

# Add image to platform-controler
Add the following section to your `docker-compose.yml` of the platform-controler. If the name of the image is different, this need to be changed in the  `docker-compose.yml` as well.
```yaml
  keyclock:
    image: hobbit-keycloak
    restart: always
    ports:
      - "8181:8080"
    networks:
      - hobbit
    volumes:
      - ../hobbit-keycloak/db:/opt/jboss/keycloak/standalone/data/db
```

# User administration
To manage users, groups and/or roles:
- login to the Keycloak Administration Console http://localhost:8181/auth/admin (user: admin, default password: 'H16obbit')
- select the realm `Hobbit`

For new users do not forget to check/assign the role mappings (tab 'Role Mappings')

# Roles
The Hobbit-gui application uses following roles (see User / 'Role Mappings').
- `system-provider`
- `guest`
- `challenge-organiser`

The preconfigured Keycloak image has following users:
- user `testuser` with the roles `system-provider`, `guest`,  `challenge-organiser`
- user `system-provider` has role `system-provider`
- user `guest` has role `guest`
- user `challenge-organiser` has role `challenge-organiser`

Default password for all these users is `hobbit`

# Self registration
User via self registration have roles `guest` and `system-provider`


