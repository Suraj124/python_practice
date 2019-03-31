from My_Main_package import Main_Module_Animal
from My_Main_package.My_Sub_Package import Sub_Module_Calc

Main_Module_Animal.cat('Flixi')
Main_Module_Animal.dog('Tulli')

print('sum(a,b)',Sub_Module_Calc.sum(10,10))
print('sub(a,b)',Sub_Module_Calc.sub(20,10))
print('mul(a,b)',Sub_Module_Calc.mul(10,10))
print('div(a,b)',Sub_Module_Calc.div(50,10))
print('mod(a,b)',Sub_Module_Calc.mod(10,10))