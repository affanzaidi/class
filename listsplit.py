data = [2, 12, 17, 23, 21, 8, 4, 32, 12]


chunks = [data[x:x+100] for x in range(0, len(data), 100)]