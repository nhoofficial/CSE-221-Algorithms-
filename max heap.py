class heap:
    def max_heapify(self,arr, i):
        largest=i
        left = 2 * i  # when heap starts from index1
        right = left + 1
        if left < len(arr) and arr[largest] < arr[left]:  # n is size of the heap here
            largest = left
        else:
            largest=i
        if right < len(arr) and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.max_heapify(arr,largest)

    def heap_increase(self,arr, i, key):  # key the new value of index i
        if key < arr[i]:
            raise Exception('new key is smaller than the current key')
        arr[i] = key
        while i > 1 and arr[i // 2] < arr[i]:
            arr[i // 2], arr[i] = arr[i], arr[i // 2]
            i //= 2

    def max_heap_insert(self,arr, key):
        arr.append(key)
        i = len(arr)-1
        while i > 1 and arr[i // 2] < arr[i]:
            arr[i // 2], arr[i] = arr[i], arr[i // 2]
            i //= 2

    def heap_deletion(self,arr, idx):
        arr[idx], arr[len(arr)-1] = arr[len(arr)-1], arr[idx]
        arr.pop()
        self.max_heapify(arr,idx//2)

    def heapsort(self,arr):
        new=[0]*len(arr)
        for i in range(len(arr)-1,0,-1):
            arr[i], arr[1] = arr[1], arr[len(arr) - 1]
            a=arr.pop()
            new[i]=a
            self.max_heapify(arr, 1)
        return new
    def build_max_heap(self,arr):
        n=len(arr)
        for i in range(n//2-1,0,-1):
            self.max_heapify(arr,i)



a=[0,16,4,10,14,7,9,3,2,8,1]
n=heap()
#n.max_heapify(a,2)
#print(a)

b=[0,16,14,10,8,7,9,3,2,4,1]
#n.heap_increase(b,9,15)
#n.max_heap_insert(b,17)
n.heap_deletion(b,2)
print(n.heapsort(b))
#print(b)
#c=[0,4,1,3,2,16,9,10,14,8,7]
#n.build_max_heap(c)
#print(c)


