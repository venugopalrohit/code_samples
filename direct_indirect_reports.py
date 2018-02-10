#https://www.careercup.com/question?id=5638836259389440
# Program does not deal with cycles in the graph (employees reporting to multiple managers)

# Hash to store the manager (key) and direct reports array/list(value)
emp_hash = {}
file_handle = open("emp-list.txt", "r")
# manager number whose direct reports need to be found
boss_to_follow = 10

for line in file_handle:
    # Split input line into boss and direct reports strings
    boss_name, slaves = line.split(":")
    boss_name = int(boss_name)
    # Split direct reports string into int array/list
    slaves = [int(x) for x in slaves.split(",")]
    emp_hash[boss_name] = slaves

print(emp_hash)

direct_reports = []
proc_queue = [boss_to_follow]

# Use a queue that will hold the managers. we will pop one manager (element) at a time and then push his/her
# direct reports into the queue. Do until queue is empty.
while(proc_queue):
    manager = proc_queue.pop(0)
    if(emp_hash.get(manager)):
        for emp in emp_hash.get(manager):
            direct_reports.append(emp)
            proc_queue.append(emp)

print(direct_reports)
