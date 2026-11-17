def calculate_utilization(delta_octets, time_interval_seconds, interface_speed_bps):
    bps = (delta_octets * 8) / time_interval_seconds
    util_pct = (bps / interface_speed_bps) * 100
    return bps, util_pct

if __name__ == '__main__':
    bps, pct = calculate_utilization(12500000, 10, 1000000000)
    print(f'Current Traffic: {bps/1e6:.2f} Mbps ({pct:.2f}% utilization)')
