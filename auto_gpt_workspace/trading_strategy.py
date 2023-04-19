import datetime

def generate_signals(asset, time_frame):
    # Define your trading strategy here
    # Example: Buy signal if the 10-day moving average crosses above the 20-day moving average
    
    # Implement your trading strategy to generate binary options trading signals
    signals = []
    for i in range(len(asset)):
        if asset[i] > asset[i - 1]:
            signals.append(1)
        else:
            signals.append(0)
    
    return signals
