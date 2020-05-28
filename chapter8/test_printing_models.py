import printing_models
from printing_models import print_models as pm

unprinted = ["datta", "Rama", "Krishna", "Guru"]
printed = []

printing_models.print_models(unprinted[:], printed)
for printed in printed:
    print(f"{printed}")



print("\nTesting unprinted designs using alias\n")
print(unprinted)
printed_new = []
pm(unprinted[:], printed_new)

for printed in printed_new:
    print(printed)
