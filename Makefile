CC = g++
CFLAGS = -o
FILE1 = main.cpp
OUT_FILE = cadd0000
IN = input.txt
OUT = output.txt
all: compile

	

compile: 
	 $(CC)  $(FILE1) $(CFLAGS) $(OUT_FILE)
	 ./$(OUT_FILE)  $(IN) $(OUT)



clean: 
	rm scanner
	rm $(C_FILE)