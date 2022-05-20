class Funciones:

    def __init__(self,lista):
        self.lista=lista

    def prime(self):
        for i in self.lista:
            if self._prime(i) == True:
                print(f'El {i} es primo') 
            else:
                print(f'El {i} no es primo') 

    def _prime(self,number):

        if type(number)==int:
            answer=True
            if number!=1:
                for i in range(2,number):
                    if number%i==0:
                        answer=False
                        break
            else:
                answer=False

            return (answer)

        else:
            print('The function only accepts int inputs')




    def _counter1(self,rule):

        ''' 
        This function with rule=True give the most repeated number,
        and with rule=False the less repeated 
        '''

        if type(self.lista)==list and rule==True:
            dic_test=[]
            cou_test=[]
            test_coun=0
            for i in self.lista:

                if i in dic_test:
                    continue

                else:
                    coun=self.lista.count(i)
                    dic_test.append(i)
                    cou_test.append(coun)
                    
                    

            for k , e in enumerate(cou_test):
                if e>test_coun:
                    test_coun=e
                    value=dic_test[k]
                    answer=[value,test_coun]

            return (answer[0], 'repeated', answer[1])
        
        elif type(self.lista)==list and rule==False:
            dic_test=[]
            cou_test=[]
            test_coun=1000
            for i in self.lista:

                if i in dic_test:
                    continue

                else:
                    coun=self.lista.count(i)
                    dic_test.append(i)
                    cou_test.append(coun)
                    
                    

            for k , e in enumerate(cou_test):
                if e<test_coun:
                    test_coun=e
                    value=dic_test[k]
                    answer=[value,test_coun]

            return (answer[0], 'repeated', answer[1])

        else:
            print('The function only accepts list inputs') 

    def conversions(self,scale_temp1,scale_temp2):
        for i in self.lista:
            print(f'{i} {scale_temp1} son {self._conversions(i,scale_temp1,scale_temp2)} {scale_temp2}')


    def _conversions(self,value,scale_temp1,scale_temp2):

        if type(value) == float or type(value) == int:
            #if scale_temp1!=scale_temp2:

                if scale_temp1 == '°C':
                    if scale_temp2 == '°F':
                        answer = (value * (9/5)) + 32

                    elif scale_temp2 == '°C':
                        answer=value

                    else:
                        answer= value + 273.15  

                    return(answer) 

                elif scale_temp1 == '°F':
                    if scale_temp2 == '°C':
                        answer = ((value - 32)*5)/9

                    elif scale_temp2 == '°F':
                        answer=value

                    else:
                        answer= (((value - 32)*5)/9) + 273.15

                    return(answer) 

                else:
                    if scale_temp2 == '°C':
                        answer = value-273.15

                    elif scale_temp2 == 'K':
                        answer=value

                    else:
                        answer= ((value-273.15) * (9/5)) + 32

                    return(answer) 
        else:
            print('The value must be a number')


    def factorial(self):
        for i in self.lista:
            print(f'El factorial de {i} seria {self._factorial(i)}')

    def _factorial(self,number):
        if type(number)==int and number>1:
            numb=number
            facto=number
            while numb>1:
                numb-=1
                facto=facto*numb
            
            return(facto)
        
        else:
            print('Input data type must be integer greater than 0')