# TODO Найдите количество книг, которое можно разместить на дискете
stran=100
stro=50
symb=25
one=4
ob=1.44
kniga=stran*stro*symb*one/1024/1024
colvo=ob//kniga
int_colvo=int(colvo)
print("Количество книг, помещающихся на дискету:",int_colvo)
