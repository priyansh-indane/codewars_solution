def ips_between(start, end):
    def ip_to_int(ip):
        parts = ip.split(".")
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    
    return ip_to_int(end) - ip_to_int(start)
