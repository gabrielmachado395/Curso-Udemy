from cp import ContaPoupanca
from cc import ContaCorrente
from tdb import TesteDeBanco

tdb = TesteDeBanco()


cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
