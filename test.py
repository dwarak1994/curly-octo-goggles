

'''

def even_odd(x):
	
	if(x%2==0):
		return 0
	else:
		return 1

def length(x):
	y=0
	for i in x:
		y=y+1
	return y


	
def sum_odds(x):
	y=0
	for i in range(length(x)):
		if even_odd(x[i])==1:
			y=y+x[i]
	return y


x=[1,2,3,4,5,9]
y=[412,452,346,635,45,65363,5425,78]

print(sum_odds(x))
print(sum_odds(y))

'''

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "HELLO WORLD"

if __name__=='__main__':
    app.run(debug=True)


## REST API