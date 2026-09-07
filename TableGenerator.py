print("====Table Generator=====")
def tablegenerator(table):

    for i in range(1,11):
        print(f"{table}X{i}={table*i}")
table=int(input("which Number oftable you want to generate?..."))
tablegenerator(table)
