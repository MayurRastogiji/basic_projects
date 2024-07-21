# Implementing Best fit algorithm for memory management
def best_fit(memory_blocks, process_list):
    for i in process_list:
        space = list()
        for j in memory_blocks:
            space.append(j-i)
        # print(space)
        num = None
        for k in space:
            if k>=0:
                if num == None:
                    num = k
                elif k<num:
                    num = k
        
        return space.index(num), process_list.index(i)

def worst_fit(memory_blocks, process_list):
    for i in process_list:
        for j in memory_blocks:
            if j-i>=0:
                return memory_blocks.index(j), process_list.index(i)

def check_input(memory_blocks, process_list):
    if memory_blocks == None or process_list == None:
        return False
    
def check_values(memory_blocks, process_list):
    for i in process_list:
        if i > max(memory_blocks):
            return process_list.index(i)
        else:
            return None

dic = {
    "1": best_fit,
    "2": worst_fit
}
def alocation(memory_blocks, proceses_list, choice, dic):
    allocation = dict()
    memory_blocks.sort()
    for i in range(len(proceses_list)):
        # best_fit(memory_blocks, proceses_list)
        index_m, index_p = dic[choice](memory_blocks, proceses_list)
        allocation [memory_blocks[index_m]]= (proceses_list[index_p]) 
        del memory_blocks[index_m]
        del proceses_list[index_p]
    print("memory slot : process")
    print(allocation)

proceses_list = list(map(int, input("Enter the processes list").split()))
memory_blocks = list(map(int, input("Enter the memory blocks").split()))
if check_input(memory_blocks, proceses_list):
    print("Please enter valid inputs")
    exit()
index_pro = check_values(memory_blocks, proceses_list)
if index_pro != None:
    print(f"{proceses_list[index_pro]} cannot be allocated")
    del proceses_list[index_pro]
# print("Processes list", proceses_list)
# print("Memory blocks", memory_blocks)
choice = input("Enter the choice of algorithm\n1. Best fit\n2. Worst fit\n")
if choice == '1':
    alocation(memory_blocks, proceses_list, choice, dic)
elif choice == '2':
    alocation(memory_blocks, proceses_list, choice, dic)
