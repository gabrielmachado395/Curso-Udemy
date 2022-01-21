from cp import ContaPoupanca
from cc import ContaCorrente

cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

cc = ContaCorrente(agencia=111, conta=222, saldo=0, limite=500)
cc.depositar(501)
cc.sacar(502)
