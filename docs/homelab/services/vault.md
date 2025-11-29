# Vault
    
    

## Description

Vault is a popular homelab service that securely stores and manages sensitive data like passwords, API keys, and certificates. Its main purpose is to provide a centralized secrets management system, making it easy to rotate credentials, manage access, and keep your homelab secure. Vault offers features like dynamic secrets generation, encryption, and fine-grained access control, giving you full control over who can access your sensitive data. By using Vault, you can simplify your homelab's security and reduce the risk of credential leaks and unauthorized access.

## Docker Compose File

```yaml
services:
  vault:
    image: hashicorp/vault
    container_name: vault
    environment:
      VAULT_ADDR: "https://0.0.0.0:8200"
      VAULT_API_ADDR: "https://0.0.0.0:8200"
      VAULT_ADDRESS: "https://0.0.0.0:8200"
      # VAULT_UI: true
      # VAULT_TOKEN:
    ports:
      - "8200:8200"
      - "8201:8201"
    restart: always
    volumes:
      - ~/storage/vault/logs:/vault/logs/:rw
      - ~/storage/vault/data:/vault/data/:rw
      - ~/storage/vault/config:/vault/config/:rw
      - ~/storage/vault/certs:/certs/:rw
      - ~/storage/vault/file:/vault/file/:rw
    cap_add:
      - IPC_LOCK
    entrypoint: vault server -config /vault/config/config.hcl
```

## Notes

- Access `vault` at [http://cheeselab:8200](http://cheeselab:8200) (Local Network Only)