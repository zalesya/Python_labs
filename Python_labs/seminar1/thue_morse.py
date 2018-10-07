def get_sequence_item(n):
    def thue_morse(k):
        if k == 0:
            return 0
        else:
            import math
            left = thue_morse(k - 1)
            order = int(math.log2(left) + 1) if left else 0
            right = ((2 << order) - 1) ^ left
        return (left << order + 1) + right
    return bin(thue_morse(n))


#if __name__ == '__main__':
    #print(get_sequence_item(int(input())))
