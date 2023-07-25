

## System Load Testing

```bash
sudo amazon-linux-extras install epel -y
sudo yum install stress -y
```

Execute the stress test:

```bash
stress --cpu 16 --io 8 --vm 4 --vm-bytes 128M
```

