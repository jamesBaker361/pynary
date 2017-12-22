import sys

def mrp(sharperatio,impvol):
	print(sharperatio*impvol)
	return(sharperatio*impvol)

def main():
	return(mrp(float(sys.argv[1]),float(sys.argv[2])))

if __name__ == '__main__':
	main()