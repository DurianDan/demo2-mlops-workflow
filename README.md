## Reference
- [fastapi-nginx-gunicorn][1]: Deploying a FastAPI web app to a Virtual Private Server (VPS) is tricky. If you're not familiar with technologies such as NGINX or Gunicorn, it can easily overwhelm you.

## How access the project folder on the provided EC2 instance (13.229.56.20)
- ssh into the default user, using the provided `.pem` file by the judges (search your email for title **[MLOps Marathon 2023] Server Credentials**)
    ```bash
    chmod 400 <path to .pem file>
    ssh -i <path to .pem file> ubuntu@13.229.56.20
    ```
- after in the terminal of the **EC2 instance**: log in the user '`fast-api`':
    ```bash
    su fast-api
    ```
- type the correct password

## Reload nginx to load changes in code
```bash
sudo supervisorctl restart fastapi-app
sudo systemctl restart nginx
```


[1]: https://dylancastillo.co/fastapi-nginx-gunicorn/