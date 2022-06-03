import numpy as np
import datetime as dt
import pandas as pd

class Struct(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))
 
    def _wrap(self, value):
        # Recursively wrap through all nested items
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value

    def items(self):
        # equivalent to dict.items()
        [print(k) for k in vars(self) if not k.startswith('_')];
    
    def return_items(self):
        # returns equivalent to dict.items() in a list
        return [k for k in vars(self) if not k.startswith('_')];
    
    def get_times(self):
        # Create a time variable for each of the traces
        setattr(self.streams.BPre, 'time', np.linspace(0, len(self.streams.BPre.data), len(self.streams.BPre.data))/self.streams.BPre.fs)
        setattr(self.streams.EEG1, 'time', np.linspace(0, len(self.streams.EEG1.data), len(self.streams.EEG1.data))/self.streams.EEG1.fs)
        setattr(self.streams.LFP2, 'time', np.linspace(0, len(self.streams.LFP2.data), len(self.streams.LFP2.data))/self.streams.LFP2.fs)
        setattr(self.streams.SU_3, 'time', np.linspace(0, len(self.streams.SU_3.data), len(self.streams.SU_3.data))/self.streams.SU_3.fs)
    
    def get_timestamps(self):
        # Add timestamps for each of the traces
        # Creates a series of the start time of length time from 'get_times'
        # Add timedelta of the elapsed seconds from 'get_time'
        
        
        setattr(self.streams.BPre, 'timestamp', 
                (pd.Series(pd.to_datetime(self.info.start_date), index=range(len(self.streams.BPre.time))) + \
                 pd.to_timedelta(self.streams.BPre.time, unit='s')).values)
        
        setattr(self.streams.EEG1, 'timestamp', 
                (pd.Series(pd.to_datetime(self.info.start_date), index=range(len(self.streams.EEG1.time))) + \
                 pd.to_timedelta(self.streams.EEG1.time, unit='s')).values)
        
        setattr(self.streams.LFP2, 'timestamp', 
                (pd.Series(pd.to_datetime(self.info.start_date), index=range(len(self.streams.LFP2.time))) + \
                 pd.to_timedelta(self.streams.LFP2.time, unit='s')).values)
        
        setattr(self.streams.SU_3, 'timestamp', 
                (pd.Series(pd.to_datetime(self.info.start_date), index=range(len(self.streams.SU_3.time))) + \
                 pd.to_timedelta(self.streams.SU_3.time, unit='s')).values)
       
                
    def preprocess(self):
        self.get_times()
        self.get_timestamps()