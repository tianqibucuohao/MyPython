def fib(n):
	a,b=0,1
	while a<n:
		print(a,end=' ')
		a,b=b,a+b

def output(name, base,shuqiang, wuli, liliang,jineng,huangzi,baizi,baoji, zuizhong):
    outsum=base * shuqiang/(220) * (1+wuli/100) \
            * (1+liliang/100) \
            * (1+huangzi)   \
            * (1+baizi) \
            * (1+baoji) \
            * (1+jineng) \
            * (1+zuizhong)
    print(name, "output:",outsum)
		
def main():
    base=100
    shuqiang=100
    wuli=100
    liliang=100
    jineng=100

    huangzi=0.0
    baizi=0.0
    baoji=0.0
    zuizhong=0.0

    output("now",base,shuqiang, wuli,liliang,jineng,huangzi,baizi,baoji,zuizhong)
#    nowbaoji=baoji+0.5
#    nowhuangzi=huangzi+0.2+0.1
#    nowbaizi=baizi+0.33
#    nowwuli=wuli+0.22+0.1
#    nowzuizhong=zuizhong+0.2
#    nowjineng=jineng+0.1+0.1
#    nowshuqinag=shuqiang+60
#    nowliliang=liliang+0.15
#    output("90a",base,nowshuqinag,nowwuli,nowliliang,nowjineng,nowhuangzi, nowbaizi,nowbaoji,nowzuizhong)
#    
#    jineng95=jineng+0.17+0.1+0.1
#    baizi95=baizi+0.19+0.1
#    zuizhong95=zuizhong+0.2+0.2+0.1
#    liliang95=liliang+0.18+0.15
#    baoji95=baoji+0.19
#    wuli95=wuli+0.64+0.22+0.1
#    output("95a",base,nowshuqinag,wuli95,liliang95,jineng95,huangzi,baizi95,baoji95,zuizhong95)
        
if (__name__=="__main__")        :
    main()