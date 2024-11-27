
docker original

```docker
services:
  keycloak:
    image: quay.io/keycloak/keycloak:22.0.1
    container_name: keycloak
    environment:
      DB_VENDOR: postgres
      DB_ADDR: postgres
      DB_DATABASE: keycloak
      DB_USER: keycloak
      DB_PASSWORD: changeme
      KEYCLOAK_ADMIN: admin
      KEYCLOAK_ADMIN_PASSWORD: admin
    ports:
      - "8080:8080"
    depends_on:
      - postgres
    command: start-dev

  postgres:
    image: postgres:14
    container_name: postgres
    environment:
      POSTGRES_DB: keycloak
      POSTGRES_USER: keycloak
      POSTGRES_PASSWORD: changeme
    volumes:
      - postgres_data:/var/lib/postgresql/infrastructure

volumes:
  postgres_data:
```

Docker modificado