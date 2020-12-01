# import time
# start_time = time.time()

with open("promote.in","r") as f_in:
    bronze_before, bronze_after = map(int,f_in.readline().strip("\n").split())
    silver_before, silver_after = map(int, f_in.readline().strip("\n").split())
    gold_before, gold_after = map(int, f_in.readline().strip("\n").split())
    platinum_before, platinum_after = map(int, f_in.readline().strip("\n").split())

gold_to_platinum =  platinum_after - platinum_before
silver_to_gold = gold_after - gold_before + gold_to_platinum
bronze_to_silver = silver_after - silver_before + silver_to_gold

with open("promote.out", "w") as f_out:
    f_out.write(str(bronze_to_silver) + "\n")
    f_out.write(str(silver_to_gold) + "\n")
    f_out.write(str(gold_to_platinum) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
