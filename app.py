def calculate_uptime(total_hours, downtime_hours):
    if total_hours <= 0:
        raise ValueError("Total hours must be positive")
    return ((total_hours - downtime_hours) / total_hours) * 100

if __name__ == '__main__':
    uptime = calculate_uptime(720, 0.5)
    print(f"Service Monthly Availability: {uptime:.2f}%")
