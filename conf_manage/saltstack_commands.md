# Saltstack commands

some useful saltstack commands

### Salt Master

```bash

# Update salt master config from git repo.
sudo salt-run fileserver.update

# Salt master service
/etc/init.d/salt-master status (stop/start/restart)

# Salt report
salt --versions-report

# Salt logs
tail /var/log/salt/master

```
### Salt Minion

```bash

# Apply state in debug level
sudo salt-call -l debug state.apply ci

# Apply state from specific branch
sudo salt-call state.apply saltenv=my-branch

# Salt logs
tail /var/log/salt/minion

```