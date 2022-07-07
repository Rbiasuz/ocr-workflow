


#exemplo de teste unitário (testes simples pra garantir que uma "unidade" do código funciona)

#assert sum([2, 2]) == 4,  "should be 4"
#assert sum([22]) == 4,  "should be 4"


def test_sum():
    assert sum([2, 2]) == 4,  "should be 4"

def test_sum2():
    assert sum([1, 1]) != 3,  "should not be 3"

def test_sum3():
    assert sum([3, 3]) == 7,  "should be 2"

def test_sum4():
    assert sum([15, 15]) == 30,  "should be 30"



def par_impar(num):
    if num%2 == 0:
        return num*num
    else:
        return num-10


def test_par_impar():
    assert par_impar(2) == 4,  "should be 4"

def test_par_impar2():
    assert par_impar(1) == -9,  "should be -9"

if __name__ == "__main__":
    test_sum()
    test_sum2()
    test_sum3()
    test_sum4()
    print("Everything passed")