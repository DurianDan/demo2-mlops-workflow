- TODO: 
  - automate this in Ci/CD: 
    - [grant permission][1]: `data/grafana`
        ```bash
        sudo chown 472:472 data/grafana 
        sudo chown 1000:1000 data/grafana 
        ```
    - connect grafana to postgres db (docker-compose services)

[1]: https://community.grafana.com/t/mkdir-cant-create-directory-var-lib-grafana-plugins-permission-denied/68342