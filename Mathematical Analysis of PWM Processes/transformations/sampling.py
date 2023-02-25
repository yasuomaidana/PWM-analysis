from signals.Signal import CarrierSignal, Signal


def natural_sampling(carrier_signal: Signal, modulated_signal: Signal):
    output = [-1 if carrier > modulated else 1 for carrier, modulated in zip(carrier_signal.out, modulated_signal.out)]
    return output


def symmetrical_sampling(carrier_signal: Signal, modulated_signal: Signal):
    output = []
    old_value = 0
    old_delta = 0
    hold = 0
    output.append(0)
    sampled = [0]
    read = False
    for i, y in enumerate(carrier_signal.out):
        delta = y - old_value

        if old_delta == 0:
            old_delta = delta
            continue
        if delta * old_delta < 0:
            if y > 0:
                read = True
        if read:
            ym = modulated_signal.out[i]
            if old_value > ym > y:
                hold = modulated_signal.out[i]
                read = False
        state = 1
        if hold < y:
            state = -1

        old_delta = delta
        old_value = y
        sampled.append(hold)
        output.append(state)
    return output, sampled

def uniform_sampling(carrier_signalL: Signal, modulated_signal: Signal, enable_read, read):
    pass

def asymmetrical_sampling(carrier_signal: Signal, modulated_signal: Signal):
    output = []
    old_value = 0
    old_delta = 0
    hold = 0
    output.append(0)
    sampled = [0]
    read = False
    for i, y in enumerate(carrier_signal.out):
        delta = y - old_value

        if old_delta == 0:
            old_delta = delta
            continue
        if delta * old_delta < 0:
            read = True
        if read:
            ym = modulated_signal.out[i]
            if old_value > ym > y or old_value < ym < y:
                hold = modulated_signal.out[i]
                read = False
        state = 1
        if hold < y:
            state = -1

        old_delta = delta
        old_value = y
        sampled.append(hold)
        output.append(state)
    return output, sampled