import shlex
from collections import defaultdict

if __name__ == "__main__":
    filename = "sample.log"

    agent_type_count = defaultdict(int) # store agent count

    # open file
    with open(filename) as f:
        
        # iterate through each line
        for line in f:
            cur_log = line.strip()
            agent_type = shlex.split(cur_log)[-1] # split on spaces but consider enclosed "" as a single element


            # verify if it is an agent 
            if agent_type.startswith('Mozilla'):
                agent_type_count[agent_type] += 1
    


    # print user agents and their count
    print("======== Agent types and their counts =========")
    for k, v in agent_type_count.items():
        print("Agent: ", k)
        print("count: ", v)
        print("\n")