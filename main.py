# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    #free_next_time = [0] * n
    #assigned_threads = [-1] * m
    #next_free_time = [0]
    
    jobs=[(data[i], i) for i in range(m)]
    threads= [0]*n
    for darbs in jobs:
        thread= threads.index(min(threads))
        start_time=threads[thread]
        output.append((thread, start_time))
        threads[thread]+= darbs[0]
   
    return output


def main():
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    # TODO: create the function
    result = parallel_processing(n, m, data)
    for threads, time in result:
        print(threads, time)


if __name__ == "__main__":
    main()