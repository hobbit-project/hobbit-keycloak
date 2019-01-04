# Information

This is the prepared Keycloak 2.4.0 Docker image for usage with the gui of the HOBBIT platform.

# Build docker image

```bash
docker build -t hobbitproject/hobbit-keycloak .
```

# Configure Privacy Policy

You need to create a directory with a file named `privacypolicy.ftl`
with HTML content containing link to your policy:
```html
Read our <a href="https://...">Privacy Policy</a>.
```

Then configure that directory as a volume for keycloak:
```yml
volumes:
  - ./your_directory:/opt/jboss/keycloak/themes/hobbit/login/hobbit
```
