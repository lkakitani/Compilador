import re

class Automato:
    

    def __init__(self, text):
        self.automato = {}
        self.readDef(text)
        return
    
    def checkWord(self,word):
        state = self.attributes["q0"]
        for i in range(0, len(word)):
            print word[i]
            if word[i] in self.attributes["P"][state]:
                state = self.attributes["P"][state][word[i]]
            else:
                return False
        if state in self.attributes["F"]:
                return True
        return False
    
    def readDef(self, text):
        file = open(text,'r')
        splitText = file.read().replace('\n','').replace('\\n','\n').replace('\\t','\t').replace(' := ','@').split('@')
        #recebendo os atributos que foram definidos pelo texto.
        self.attributes = {splitText[0]:splitText[1], splitText[2]:splitText[3], splitText[4]:splitText[5],
                           splitText[6]:splitText[7], splitText[8]: splitText[9]}
        
        self.attributes["Q"] = self.attributes["Q"].split(', ') #Q: valores do estado
        self.attributes["S"] = self.attributes["S"].split(', ') #S: valores do alfabeto
        attAux = []
        for x in range(0, len(self.attributes["S"])):
            attAux.append(self.attributes["S"][x])
            if(self.attributes["S"][x].find('-') == 1):
                values = self.attributes["S"][x].split('-')
                for y in range(ord(values[0][0]),ord(values[1][0])+1):
                    attAux.append(chr(y))
                attAux.pop(x)
        self.attributes["S"] = attAux
        
        #P: valores das transicoes
        #algumas operacoes sao feitas para o mapeamento das transicoes em dicionarios
        self.attributes["P"] = self.attributes["P"][1:].replace('; (','@').replace(', ','@').replace(') -> ','@').split('@')
        
        attAux = []
        for x in range(0, len(self.attributes["P"])/3):
            if(self.attributes["P"][x*3 + 1].find('-') == 1):
                values = self.attributes["P"][x*3 + 1].split('-')
                for y in range(ord(values[0][0]),ord(values[1][0])+1):
                    attAux.append(self.attributes["P"][x*3])
                    attAux.append(chr(y))
                    attAux.append(self.attributes["P"][x*3 + 2])
            else:
                attAux.append(self.attributes["P"][3*x])
                attAux.append(self.attributes["P"][3*x + 1])
                attAux.append(self.attributes["P"][3*x + 2])               
        self.attributes["P"] = attAux
        
        states = []
        availableStates = []        
        for x in range(0, len(self.attributes["P"])/3):
            states.append(self.attributes["P"][3*x])

        transitions = []
        for x in range(0, len(self.attributes["Q"])):
            transitions.append([])
            while self.attributes["Q"][x] in states:
                index = states.index(self.attributes["Q"][x])
                #    print self.attributes["P"][3*index], self.attributes["P"][3*index + 1], self.attributes["P"][3*index + 2], "\n"
                transitions[x].append([self.attributes["P"][3*index + 1], self.attributes["P"][3*index + 2]])
                states.remove(self.attributes["Q"][x])
                self.attributes["P"].pop(3*index)
                self.attributes["P"].pop(3*index)
                self.attributes["P"].pop(3*index)
                  
        self.attributes["P"] = dict(zip(self.attributes["Q"][:], self.attributes["Q"][:])) 
        print self.attributes["P"]
        
        
        print self.attributes["Q"]
        for x in range(0, len(self.attributes["Q"])):
            if len(transitions[x][:]) > 1:
                transitionState = [item for sublist in transitions[x][:] for item in sublist]
                self.attributes["P"][self.attributes["Q"][x]] = dict(zip(transitionState[0::2],transitionState[1::2]))
            else:        
                self.attributes["P"][self.attributes["Q"][x]] = []

        
        for x in range(0, len(self.attributes["Q"])):
                print self.attributes["Q"][x], " ", self.attributes["P"][self.attributes["Q"][x]] 