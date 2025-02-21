# src/core/ntp_analyzer.py
import math
from collections import deque
from statistics import mean, stdev

class NTPAnalyzer:
    def __init__(self, window_size=8):
        self.window = deque(maxlen=window_size)
        self.min_stratum = 16

    def add_sample(self, offset: float, delay: float, stratum: int):
        self.window.append({
            'offset': offset,
            'delay': delay,
            'stratum': stratum
        })
        self.min_stratum = min(stratum, self.min_stratum)

    def _marzullo(self):
        # RFC 1305 Appendix A.5.1
        intervals = [(s['offset'] - s['delay']/2, s['offset'] + s['delay']/2) 
                    for s in self.window]
        
        best = 0
        best_interval = (0.0, 0.0)
        
        for low, high in intervals:
            count = sum(1 for interval in intervals 
                       if interval[0] <= high and interval[1] >= low)
            if count > best:
                best = count
                best_interval = (low, high)
        
        return (best_interval[0] + best_interval[1]) / 2

    def analyze(self):
        if not self.window:
            return None
            
        dispersion = mean(s['delay'] for s in self.window)
        offsets = [s['offset'] for s in self.window]
        
        return {
            'offset': self._marzullo(),
            'stratum': self.min_stratum + 1,
            'dispersion': dispersion + math.sqrt(sum((o - self._marzullo())**2 for o in offsets)),
            'jitter': stdev(offsets) if len(offsets) > 1 else 0.0
        }
