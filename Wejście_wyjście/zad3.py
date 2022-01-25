# Lukasz Piasecki
# Programowanie w języku Python
# 09.11.2021

zamek_szyfrowy = [1,2,3,4,5]
cyfry = []



while(1):                                                                    
    print( 'Podaj %s-cyfrowy kod:' % len(zamek_szyfrowy)   )                 
    code = input()                                                           
                                                                         
    if len(code) !=len(zamek_szyfrowy) :                                     
        print('Niepoprawny kod. Zła liczba znaków.')                         
                                                                       
    else :                                                                   
        if not(code.isdigit()) :                                             
            print('Niepoprawny kod. Kod nie jest liczbą.')                   
        else:                                                                
            code_text = str(code)                                            
            for element in  code_text :                                      
                cyfry.append( int(element) )                                 
                                                                         
            if zamek_szyfrowy ==cyfry :                                      
                print('sukces')                                              
                break                                                        
            else: cyfry.clear()



















