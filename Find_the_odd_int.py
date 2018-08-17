def find_it(seq):
    
    for i in range(0, len(seq)):
        counter = 0
        for j in range(0, len(seq)):
            if seq[i]==seq[j]:
                counter += 1
        if counter % 2 != 0:
            return seq[i]
