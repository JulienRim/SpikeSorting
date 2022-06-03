def zcr_features(spike_traces, wstart=20):
    """
    This fuction performs zero crossing feature extraction on the trace
    See Computationally Efficient Neural Feature Extraction for Spike Sorting in Implantable High-Density Recording Systems
    
    Inputs
    ------
    spike_traces : numpy array
        Contains the values of the spikes which passed the threshold (output of the get_spike_traces function)

    wstart : int
        Where the spike is centered
        Defaults to 20

    Outputs
    -------
    ZC1s : numpy array
        Sum of values before the first zero crossing of the spike after wstart
        
    ZC2s : numpy array 
        Sum of values after the first zero crossing of the spike after wstart
    """
    
    # NB fix this if using negative and positive
    ZC1s = np.empty(len(spike_traces))
    ZC2s = np.empty_like(ZC1s)

    for i in range(len(spike_traces)):
        trace = spike_traces[i]
        try:
            Z_index = np.where(trace[wstart:] <= 0)[0][0] + wstart
        except:
            Z_index = len(trace)
        ZC1s[i] = np.sum(trace[:Z_index])
        ZC2s[i] = np.sum(trace[Z_index:])
        
    return ZC1s, ZC2s