def fnv1a(str):
    fnv_prime = 0x01000193;
    hval      = 0x811c9dc5;
    uint32Max = 2 ** 32;

    for c in str:
        hval = hval ^ ord(c);
        hval = (hval * fnv_prime) % uint32Max;
    return hval


out1 = fnv1a("GpuProfilerConfig.StartFrame")
print(out1)
out1 = fnv1a("GpuProfilerConfig_StartFrame")
print(out1)
out1 = fnv1a("StartFrame")
print(out1)
out1 = fnv1a(format(out1))
print(out1)