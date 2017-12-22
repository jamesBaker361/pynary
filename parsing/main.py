import sys

def main(f,w):
	convo=[]
	text=""
	for line in f:
		text=line
	for x in range(text.find("<p>"),len(text)):
		if(text[x:x+3]=="<p>"):
			line=text[x+3:3+x+text[x+3:len(text)].find("</p>")]
			#now we have to get rid of apostrophes/quotation marks
			for y in range(0,len(line)):
				if(line[y]=="&#039;" or line[y]=="&#034;"):
					print("got em")
					line=line[0:y]+line[y+1:len(line)]
				print(line)
			convo.append("\n"+line)
	for t in range(0,len(convo)):
		w.write(convo[len(convo)-(t+1)])
	w.close()

if __name__ == '__main__':
	if(len(sys.argv)==3):
		f=open(sys.argv[1],"r+")
		w=open(sys.argv[2],"w+")
		main(f,w)
	else:
		print("2 arguments required: file to read, file to write to")