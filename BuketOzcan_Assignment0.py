k_glass=0.78 
k_air= 0.026
T_i= 20
T_o= -10
h_1= 10
h_2= 40
A= 1.2
L_glass= 0.004
L_air= 0.01
Rconv_1= 1/(h_1*A)
Rcond_1= L_glass/(k_glass*A)
Rcond_2= L_air/(k_air*A)
Rcond_3=Rcond_1
Rconv_2= 1/(h_2*A)
Rtotal=Rconv_1+Rcond_1+Rcond_2+Rcond_3+Rconv_2
Q=(T_i-T_o)/Rtotal
T_1=T_i-Q*Rconv_1
print("Total resistance (Rtotal) is "+str(Rtotal))
print("The heat transfer rate (Q) is "+ str(Q))
print("Temperature of inner surface is "+str(T_1))
print("buket")