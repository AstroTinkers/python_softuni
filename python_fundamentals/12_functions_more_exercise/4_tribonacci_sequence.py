def tribonacci_sequence(number):
    sequence = [1]
    print(sum(sequence), end=" ")
    for i in range(0, number - 1):
        print(sum(sequence), end=" ")
        sequence.append(sum(sequence))
        if len(sequence) > 3:
            sequence.pop(0)


sequence_number = int(input())
tribonacci_sequence(sequence_number)
