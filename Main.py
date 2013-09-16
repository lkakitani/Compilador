from Automato import *

def main():
    print "Enter a file name:"
    filename = raw_input() 
    automato = Automato(filename)
    while True:
        print "Deseja testar se alguma palavra pertence ao automato? s/n"
        response = raw_input()
        if response is 'n' or response is 'N' :
            break
        else:
            print "Digite a palavra a ser testada"
            word = raw_input()
            if automato.checkWord(word):
                print "A palavra", word, "pertence a linguagem"
            else:
                print "A palavra", word, "nao pertence a linguagem"

if __name__ == "__main__":
    main()
