import model_mult as model_mult
import model_sum as model_sum


def ch_operation():
    operation=int(input("Choose operation:\n 1 - sum\n 2 - sub\n 3 - mult\n 4 - div\n 5 - pow\n 6 - sqrt\n 0 - previouse menu\n" ))
    # dict_operation=dict([(1,'sum'),(2,'sub'),(3,'mult'),(4,'div'),(5,"pow"),(6,'sqrt'),(0,'previose menu')])
    dict_models=dict([(1,model_sum),(2,'model_sub'),(3,model_mult),(4,'model_div'),(5,"model_pow"),(6,'model_sqrt')])
    print(operation)
    return dict_models.get(operation)

print(ch_operation())
