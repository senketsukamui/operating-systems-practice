import threading
import numpy as np
import random


class ThreadingMatrixMultiplicator(threading.Thread):
    def __init__(self, A, B, i):
        super(ThreadingMatrixMultiplicator, self).__init__()
        self.A = A
        self.B = B.transpose()
        self.i = i
        self.result = 0

    def run(self):
        print(f'Multiplying: {self.i}')
        result = np.zeros(self.A.shape[0])
        for x in range(self.A.shape[0]):
            for y in range(self.A.shape[0]):
                result[x] += self.A[self.i, y] * self.B[x, y]
        self.result = result
        print(f'Multiplying {self.i} completed')


def multiply(n):
    A = np.zeros((n, n))
    B = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = random.randrange(0, 100)
            B[i, j] = random.randrange(0, 100)
    print('Matrixes')
    print('Matrix A:')
    print(A)
    print('------')
    print('Matrix B:')
    print(B)
    print('------')
    threads = []
    for i in range(n):
        t = ThreadingMatrixMultiplicator(A, B, i)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    C = np.zeros((n, n))
    for index, t in enumerate(threads):
        C[index] = t.result
    return C


if __name__ == '__main__':
    print('Result:', multiply(3))
