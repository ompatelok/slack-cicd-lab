from app import calculate_uptime

def test_uptime_calculation():
    # 720 hours total, 0 downtime -> 100%
    assert calculate_uptime(720, 0) == 100.0
    # 100 hours total, 1 hour downtime -> 99%
    assert calculate_uptime(100, 1) == 99.0
    print("All availability test assertions PASSED.")

if __name__ == '__main__':
    test_uptime_calculation()
