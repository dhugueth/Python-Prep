import re
from typing import final


class Funciones:

    def __init__(self,lista):
        if (type(lista)!= list):
            self.lista=[]
            raise ValueError ('Se esperaba una lista de numeros eneteros de entrada. Se ha creado una lista vacía')
        else:
            self.lista=lista

    def prime(self):
        
        final_answer=[]

        for i in self.lista:
            if self.__prime(i) == True:
                final_answer.append(True)
            else:
                final_answer.append(False)
                
        return final_answer

    def __prime(self,number):

        if type(number)==int:
            answer=True
            if -1<number>1:
                for i in range(2,number):
                    if number%i==0:
                        answer=False
                        break
            else:
                answer=False

            return (answer)

        else:
            print('The function only accepts int inputs')




    def counter1(self,rule):

        ''' 
        This function with rule=True give the most repeated number,
        and with rule=False the less repeated 
        '''

        if type(rule)!=bool:
            rule=None
            raise TypeError('Se esperaba un valor booleano para determinar si se desea el numero mas o menos repetido')
        
        else: 

            if rule==True:
                dic_test=[]
                cou_test=[]
                test_coun=0
                for i in self.lista:

                    if i in dic_test:
                        continue

                    elif type(i)!=int:
                        raise TypeError('Se esperan solo numeros enteros')

                    else:
                        coun=self.lista.count(i)
                        dic_test.append(i)
                        cou_test.append(coun)
                        
                        

                for k , e in enumerate(cou_test):
                    if e>test_coun:
                        test_coun=e
                        value=dic_test[k]
                        answer=[value,test_coun]

                return answer[0], answer[1]
            
            elif rule==False:
                dic_test=[]
                cou_test=[]
                test_coun=1000
                for i in self.lista:

                    if i in dic_test:
                        continue

                    elif type(i)!=int:
                        raise TypeError('Se esperan solo numeros enteros')

                    else:
                        coun=self.lista.count(i)
                        dic_test.append(i)
                        cou_test.append(coun)
                        
                        

                for k , e in enumerate(cou_test):
                    if e<test_coun:
                        test_coun=e
                        value=dic_test[k]
                        answer=[value,test_coun]

                return answer[0], answer[1]
 

    def conversions(self,scale_temp1,scale_temp2):
        final_answer=[]
        if scale_temp1=='°C' or scale_temp1=='°F' or scale_temp1=='K':
            if scale_temp2=='°C' or scale_temp2=='°F' or scale_temp2=='K':    
                for i in self.lista:
                    final_answer.append(self.__conversions(i,scale_temp1,scale_temp2))

                return final_answer

            else:
                raise ValueError ('Se espera recibir alguna de las representaciones siguientes para las temperaturas: °C --> para Celsius ; °F --> para Fahrenheit ; K --> para Kelvin')
        else:
            raise ValueError ('Se espera recibir alguna de las representaciones siguientes para las temperaturas: °C --> para Celsius ; °F --> para Fahrenheit ; K --> para Kelvin')
    
    def __conversions(self,value,scale_temp1,scale_temp2):

        if type(value) == float or type(value) == int:

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
        final_answer=[]
        for i in self.lista:
            final_answer.append(self.__factorial(i))

        return final_answer

    def __factorial(self,number):
        if type(number)==int and number>1:
            numb=number
            facto=number
            while numb>1:
                numb-=1
                facto=facto*numb
            
            return(facto)
        
        else:
            print('Input data type must be integer greater than 0')