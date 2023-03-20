# python3

def parallel_processing(n, m, data):
    output = []    
    jobs=[(data[i], i) for i in range(m)]
    threads= [0]*n
    for darbs in jobs:
        thread= threads.index(min(threads))
        start_time=threads[thread]
        output.append((thread, start_time))
        threads[thread]+= darbs[0]
   
    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    # TODO: create the function
    result = parallel_processing(n, m, data)
    for threads, time in result:
        print(threads, time)


if __name__ == "__main__":
    main()